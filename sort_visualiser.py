# Sorting Algorithm Visualiser

from bar import Bar
import tkinter as tk
from ttkthemes import themed_tk as theme
from tkinter import ttk as ttk
from tkinter import messagebox
from random import sample
from solver import Solver


class Visualiser:

    def __init__(self):
        """ initialise sorting algorithm visualiser """
        self.algorithms = ['Selection Sort', 'Insertion Sort', 'Bubble Sort', 'Merge Sort', 'Quick Sort']
        self.graph_width, self.graph_height = 1430, 810
        self.root = theme.ThemedTk()
        self.menu_frame = ttk.Frame(self.root, width=self.graph_width / 2)
        self.status_frame = ttk.Frame(self.root, width=self.graph_width / 2)
        self.canvas = tk.Canvas(self.root, height=self.graph_height, width=self.graph_width, bg='#424242')
        self.n_bars = 100
        self.bars = []
        self.bar_width = 0
        self.y_scale = 0
        self.solve_mode = 0
        self.is_solving = False
        self.is_rendering = False
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
        if self.is_solving or self.n_bars < 2:
            self.is_rendering = False
            return
        self.bars = [None for _ in range(0, self.n_bars)]
        self.bar_width = self.graph_width / self.n_bars
        values = sample(range(self.n_bars), self.n_bars)
        self.y_scale = self.graph_height / max(values)
        for i, value in enumerate(values):
            bar = Bar(self.bar_width, i, value, self)
            self.bars[i] = bar
            self.render_bar(bar)
        self.is_rendering = False

    def clean_canvas(self):
        """ delete all bars from the canvas and redraw """
        if self.is_rendering or self.is_solving:
            return
        self.is_rendering = True
        for bar in self.bars:
            self.canvas.delete(bar.shape)
        self.config_bars()

    def change_array_size(self, val):
        """ change graph size """
        if self.is_rendering or self.is_solving:
            return
        self.n_bars = int(float(val))
        self.clean_canvas()

    def algorithm_change(self, *args):
        """ change solve mode """
        self.solve_mode = self.algorithms.index(args[0])

    def validate_setup(self):
        """ validate inputs to sort """
        if self.bars is None or self.is_solving or self.is_rendering:
            return
        self.is_solving = True
        Solver(self.bars, self.n_bars, self.solve_mode, self)
        self.is_solving = False

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
        self.menu_frame.grid(row=0, column=0, sticky='new')
        ttk.Button(self.menu_frame, text='Visualise', command=self.validate_setup)
        ttk.Button(self.menu_frame, text='Regenerate', command=self.clean_canvas)
        current_algo = tk.StringVar()
        current_algo.set(self.algorithms[self.solve_mode])
        algorithms_menu = ttk.OptionMenu(self.menu_frame, current_algo, self.algorithms[0], *self.algorithms, command=self.algorithm_change)
        algorithms_menu.config(width=15)
        ttk.Label(self.menu_frame, text='Array Size', anchor='e')
        callback = self.menu_frame.register(self.only_numeric_input)
        ttk.Entry(self.menu_frame, validate="key", validatecommand=(callback, "%P")).insert(0, str(self.n_bars))
        for r, child in enumerate(self.menu_frame.winfo_children()):
            pad = 0 if isinstance(child, tk.Button) else 5
            child.grid_configure(row=0, column=r, sticky='ew', padx=pad, pady=pad)

    def only_numeric_input(self, i):
        try:
            if i == '':
                self.n_bars = 100
            else:
                self.n_bars = int(i)
            return True
        except Exception as e:
            tk.messagebox.showerror('Array Size Error', 'Please enter a positive integer for the array size or leave blank 100')
            print(e)
            return False

    def key_press_event(self, event):
        """ detect key press event """
        kp = repr(event.keysym)
        if kp == '\'v\'':
            self.validate_setup()
