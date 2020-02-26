# Bar Object for displaying integers


class Bar:

    def __init__(self, width, index, y, subscriber):
        """ initialise bar object """
        self.subscriber = subscriber
        self.width = width
        self.x1 = index * self.width
        self.x2 = self.x1 + self.width
        self._index = index
        self.value = y
        self.shape = None

    def __repr__(self):
        """ object string representation """
        return '<Bar: value \'{}\', index \'{}\'>'.format(self.value, self.index)

    @property
    def index(self):
        """ bar index propery """
        return self._index

    @index.setter
    def index(self, i):
        """ update coordinates when index changes """
        self._index = i
        self.x1 = self._index * self.width
        self.x2 = self.x1 + self.width
        self.dispatch()

    def dispatch(self):
        """ dispatch updates """
        self.subscriber.update_bar(self, render_time=0.01)
