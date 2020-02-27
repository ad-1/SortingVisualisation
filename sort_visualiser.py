# Sorting Algorithm Visualiser

import time
from bar import Bar
import tkinter as tk
from ttkthemes import themed_tk as theme
from tkinter import ttk as tkk
from random import sample
from algorithms.solver import Solver


class Visualiser:

    def __init__(self):
        """ initialise sorting algorithm visualiser """
        self.algorithms = ['Selection Sort', 'Insertion Sort', 'Bubble Sort', 'Merge Sort', 'Quick Sort']
        self.graph_width, self.graph_height = 1430, 810
        self.root = theme.ThemedTk()
        self.menu_frame = tkk.Frame(self.root, width=self.graph_width)
        self.canvas = tk.Canvas(self.root, height=self.graph_height, width=self.graph_width, bg='#424242')
        self.n_bars = 100
        self.bars = [None for _ in range(0, self.n_bars)]
        self.bar_width = self.graph_width / self.n_bars
        self.y_scale = 0
        self.solve_mode = 0
        self.is_solving = False
        self.config_root()
        self.config_menu()
        self.config_canvas()
        self.root.mainloop()

    def config_root(self):
        """ configure tkinter root object """
        self.root.title('Sorting Algorithm Visualisation')
        self.root.resizable(False, False)
        self.root.grid_propagate(True)
        self.root.get_themes()
        self.root.set_theme('radiance')
        self.root.config(background='#424242')
        self.root.bind('<Key>', self.key_press_event)

    def config_canvas(self):
        """ pack canvas on root and bind mouse event methods """
        self.canvas.bind('<Configure>', self.config_bars)
        self.canvas.grid(row=1, column=0)

    def config_bars(self, event=None):
        """ configure array of bars to sort """
        values = sample(range(self.n_bars), self.n_bars)
        self.y_scale = self.graph_height / max(values)
        for i, value in enumerate(values):
            bar = Bar(self.bar_width, i, value, self)
            self.bars[i] = bar
            self.render_bar(bar)

    def render_bar(self, bar):
        """ draw bar on canvas """
        bar.shape = self.canvas.create_rectangle(bar.x1, 0, bar.x2, bar.value * self.y_scale, fill='#2F7AE5')
        self.root.update()

    def update_bar(self, bar):
        """ update bar coordinates """
        self.canvas.coords(bar.shape, bar.x1, 0, bar.x2, bar.value * self.y_scale)
        self.canvas.itemconfig(bar.shape, fill='#D21F3C')
        self.root.update()
        self.canvas.itemconfig(bar.shape, fill='#2F7AE5')

    def config_menu(self):
        """ menu - user configurable settings for visualisation"""
        self.menu_frame.grid(row=0, column=0, sticky='n')
        self.tkk_btn(self.menu_frame, [('Visualise', self.validate_setup)], True)
        current_algo = tk.StringVar()
        current_algo.set(self.algorithms[self.solve_mode])
        algorithms_menu = tkk.OptionMenu(self.menu_frame, current_algo, self.algorithms[0], *self.algorithms, command=self.algorithm_change)
        algorithms_menu.config(width=15)
        self.tkk_label(self.menu_frame, ['Array Size'])
        self.tkk_scaler(100, 350, self.change_array_size)
        for r, child in enumerate(self.menu_frame.winfo_children()):
            pad = 0 if isinstance(child, tk.Button) else 5
            child.grid_configure(row=0, column=r, sticky='ew', padx=pad, pady=pad)

    def key_press_event(self, event):
        """ detect key press event """
        kp = repr(event.keysym)
        if kp == '\'v\'':
            self.validate_setup()

    def change_array_size(self, val):
        """ change graph size """
        self.n_bars = float(val)
        self.config_bars()

    @staticmethod
    def tkk_btn(parent, btns, is_tkk):
        """ create buttons given list of text and commands """
        for text, cmd in btns:
            if is_tkk:
                tkk.Button(parent, text=text, command=cmd)
            else:
                tk.Button(parent, text=text, highlightbackground=cmd, height=1, state='disabled')

    @staticmethod
    def tkk_label(parent, text):
        """ create labels from list of text """
        for t in text:
            tkk.Label(parent, text=t, anchor='e')

    def tkk_scaler(self, from_, to_, cmd):
        """ create themed scaler """
        tkk.Scale(self.menu_frame, from_=from_, to=to_, orient=tk.HORIZONTAL, command=cmd)

    def algorithm_change(self, *args):
        """ change solve mode """
        self.solve_mode = self.algorithms.index(args[0])

    def validate_setup(self):
        """ validate inputs to sort """
        if self.bars is None:
            return
        self.is_solving = True
        Solver(self.bars, self.n_bars, self.solve_mode, self)
        self.is_solving = False
