# Bar Object for displaying integers


class Bar:

    def __init__(self, width, index, value, subscriber):
        """ initialise bar object """
        self.subscriber = subscriber  # visualiser class listening to updtates on bars
        self.width = width  # width of the bar
        self.x1 = index * self.width  # fist horizontal coordinate
        self.x2 = self.x1 + self.width  # second horizontal coordinate
        self._index = index  # index in array
        self.value = value  # value of bar (height)
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

        # update horizontal coordinates
        self.x1 = self._index * self.width
        self.x2 = self.x1 + self.width

        self.dispatch()

    def dispatch(self, fill='#D21F3C'):
        """ dispatch updates to subscriber (visualiser) """
        self.subscriber.update_bar(self, fill)

    def __lt__(self, other):
        return self.value < other.value
