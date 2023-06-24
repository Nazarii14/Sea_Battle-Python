import random

MAP_SIZE = 10


class Ship:
    def __init__(self, length):
        self.length = length
        self.direction = random.randint(0, 1)
        self.rowCol = []
        self.numOfHits = 0
        self.isOnMap = False
        self.coords = []
        self.nearCellsCoords = []
        self.possiblePositions = []

    def __str__(self):
        to_return = "Direction: " + str(self._direction) + \
                    "\nLength: " + str(self._length) + \
                    "\nRowCol: " + str(self._rowCol) + \
                    "\nisOnMap: " + str(self._isOnMap) + \
                    "\nnumOfHits: " + str(self._numOfHits) + \
                    "\ncoords: " + str(self._coords) + \
                    "\nnearCellsCoords: " + str(self._nearCellsCoords) + \
                    "\npossiblePositions: " + str(self._possiblePositions)
        return to_return

    def __eq__(self, other):
        return self.length == other.length and self.rowCol == other.rowCol and self.isOnMap == other.isOnMap and self.direction == other.direction and self.numOfHits == other.numOfHits


    @property
    def direction(self):
        return self._direction

    @direction.setter
    def direction(self, value):
        self._direction = value


    @property
    def coords(self):
        return self._coords

    @coords.setter
    def coords(self, value):
        self._coords = value


    @property
    def nearCellsCoords(self):
        return self._nearCellsCoords

    @nearCellsCoords.setter
    def nearCellsCoords(self, value):
        value = [i for i in value if i[0] >= 0 and i[0] < MAP_SIZE and i[1] >= 0 and i[1] < MAP_SIZE]
        self._nearCellsCoords = value


    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, value):
        self._length = value


    @property
    def rowCol(self):
        return self._rowCol

    @rowCol.setter
    def rowCol(self, value):
        self._rowCol = value


    @property
    def isOnMap(self):
        return self._isOnMap

    @isOnMap.setter
    def isOnMap(self, value):
        self._isOnMap = value


    @property
    def numOfHits(self):
        return self._numOfHits

    @numOfHits.setter
    def numOfHits(self, value):
        self._numOfHits = value


    @property
    def possiblePositions(self):
        return self._possiblePositions

    @possiblePositions.setter
    def possiblePositions(self, value):
        self._possiblePositions = value


    def was_shoot(self, sht):
        for i in self.coords:
            if sht.row == i[0] and sht.col == i[1]:
                return True

        return False

    def is_dead(self):
        return self.length == self.numOfHits

    def set_possible_positions(self):
        all_cells = [[i, j] for j in range(MAP_SIZE) for i in range(MAP_SIZE)]

        if self._direction == 0:
            freeCells = [i for i in all_cells if i[0] >= self.length - 1]
        else:
            freeCells = [i for i in all_cells if MAP_SIZE - i[1] >= self.length]

        self.possiblePositions = freeCells

    def regenerate_rowCol(self):
        self.rowCol = self.possiblePositions[random.randint(0, len(self.possiblePositions) - 1)]
