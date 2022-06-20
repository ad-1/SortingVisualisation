# Sorting Algorithm Visualiser

from bar import Bar
import tkinter as tk
import random
from ttkthemes import themed_tk as theme
from tkinter import ttk as ttk
from tkinter import messagebox
from solver import Solver


class SortVisualiser:

    def __init__(self):
        """ initialise sorting algorithm visualiser """
        self.algorithms = ['Selection Sort', 'Insertion Sort', 'Bubble Sort', 'Merge Sort', 'Quick Sort']  # list of sorting algorithms implemented
        self.graph_width, self.graph_height = 1430, 810  # ui window width and height
        self.root = theme.ThemedTk()  # define themed root
        self.menu_frame = ttk.Frame(self.root, width=self.graph_width / 2)  # create menu frame
        self.canvas = tk.Canvas(self.root, height=self.graph_height, width=self.graph_width, bg='#222222')  # create tkinter canvas
        self.n_bars = 100  # starting number of items to sort
        self.bars = []  # initialise empty list to store bar objects
        self.bar_width = 0  # bar width -> calculated later depending on width and n_bars
        self.y_scale = 0  # scaling factor to fit heights on screen
        self.solve_mode = 0  # initially select selection sort, algorithms[0]
        self.colours = ['#FFE45C', '#2ECBE9', '#2F7AE5', '#797EF6', '#4ADEDE', '#1AA7EC']
        self.colour = random.sample(self.colours, k=1)

        # progress monitoring variables
        self.is_solving = False
        self.is_rendering = False

        # configure tkinter visual properties
        self.config_root()
        self.config_menu()
        self.config_canvas()

        # run ui visualisation loop
        self.root.mainloop()

    def config_root(self):
        """ configure tkinter root object """
        self.root.title('Sorting Algorithm Visualisation')  # set window title
        self.root.resizable(False, False)  # non-responsive window
        self.root.set_theme('radiance')  # set window style theme

    def config_menu(self):
        """ menu - user configurable settings for visualisation"""

        # create menu frame on top of screen
        self.menu_frame.grid(row=0, column=0, sticky='new')

        # create run button and reset buttons
        ttk.Button(self.menu_frame, text='Visualise', command=self.validate_setup)
        ttk.Button(self.menu_frame, text='Regenerate', command=self.clean_canvas)

        # track currently selected algorithm
        current_algo = tk.StringVar()
        current_algo.set(self.algorithms[self.solve_mode])

        # add algorithms option menu
        algorithms_menu = ttk.OptionMenu(self.menu_frame, current_algo, self.algorithms[0], *self.algorithms, command=self.algorithm_change)
        algorithms_menu.config(width=15)

        # allow user to define unsorted array size - only accept numeric input
        ttk.Label(self.menu_frame, text='Array Size', anchor='e')
        callback = self.menu_frame.register(self.only_numeric_input)
        ttk.Entry(self.menu_frame, validate="key", validatecommand=(callback, "%P")).insert(0, str(self.n_bars))

        # iterate over menu children and assign it a position in the grid
        for c, child in enumerate(self.menu_frame.winfo_children()):
            pad = 0 if isinstance(child, tk.Button) else 5
            child.grid_configure(row=0, column=c, sticky='ew', padx=pad, pady=pad)

    def config_canvas(self):
        """ pack canvas on root and bind mouse event methods """
        # once canvas is configured, configure bars
        self.canvas.bind('<Configure>', self.config_bars)
        self.canvas.grid(row=1, column=0)

    # event param is not used but it is required
    def config_bars(self, event=None):
        """ configure array of bars to sort """
        # check if program is running or bars is less than 2
        if self.is_solving or self.n_bars < 2:
            self.is_rendering = False  # stop rendering and end configuration
            return

        self.bars = []  # initialise list of bars
        self.bar_width = self.graph_width / self.n_bars  # calcualte bar width based on graph width and number of bars
        values = random.sample(range(0, self.n_bars), self.n_bars)  # create random sample of values - values from zero to the number of bars

        self.y_scale = self.graph_height / max(values)  # determine scaling factor to fit bars inside available height

        # iterate over the bars
        for i, value in enumerate(values):
            bar = Bar(self.bar_width, i, value * self.y_scale, self)
            self.bars.append(bar)
            self.render_bar(bar)

        # bar initial rendering complete
        self.is_rendering = False

    def clean_canvas(self):
        """ delete all bars from the canvas and redraw """
        # check if screen is already rendering or solving
        if self.is_rendering or self.is_solving:
            return
        self.is_rendering = True
        # delete all bars on canvas
        for bar in self.bars:
            self.canvas.delete(bar.shape)

        self.colour = random.sample(self.colours, k=1)

        # reconfigure bars
        self.config_bars()

    def change_array_size(self, value):
        """ change graph size """
        if self.is_rendering or self.is_solving:
            return

        # clean canvas and render updated array size
        self.n_bars = int(float(value))
        self.clean_canvas()

    def algorithm_change(self, *args):
        """ change solve mode """
        self.solve_mode = self.algorithms.index(args[0])

    def validate_setup(self):
        """ validate inputs to avoid unitialised errors """
        if self.bars is None or self.is_solving or self.is_rendering:
            return

        self.is_solving = True

        # create sorting solver object
        Solver(self.bars, self.n_bars, self.solve_mode, self)

        self.is_solving = False

    def render_bar(self, bar):
        """ draw bar on canvas """
        # render bar shape blue rectangle
        bar.shape = self.canvas.create_rectangle(bar.x1, 0, bar.x2, bar.value, fill=self.colour)
        self.root.update()

    def update_bar(self, bar, fill):
        """ update bar coordinates """

        # update bar is called from bar object when coordinates change
        self.canvas.coords(bar.shape, bar.x1, 0, bar.x2, bar.value)

        # show updating bar as red
        self.canvas.itemconfig(bar.shape, fill=fill)
        self.root.update()

        # after move complete, change colour back to blue
        self.canvas.itemconfig(bar.shape, fill=self.colour)

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


# Program Driver for sorting visualisation
if __name__ == '__main__':
    visualiser = SortVisualiser()
