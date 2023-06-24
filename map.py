import numpy as np
import ship
import result


class Map:
    def __init__(self):
        self.mtrx = np.zeros((ship.MAP_SIZE, ship.MAP_SIZE))
        self.ships = []
        self.shoots = []
        self.dead_ships_count = 0

    def __str__(self):
        to_return = ""
        for i in self.mtrx:
            to_return += str(i) + "\n"
        return to_return

    @property
    def mtrx(self):
        return self._mtrx

    @mtrx.setter
    def mtrx(self, value):
        self._mtrx = value

    @property
    def dead_ships_count(self):
        return self._deadShipsCount

    @dead_ships_count.setter
    def dead_ships_count(self, value):
        self._deadShipsCount = value


    def put_ship(self, shp):
        while not shp.isOnMap:
            shp.regenerate_rowCol()
            nearCells, new_coords = [], []

            if shp.direction == 0:
                for i in range(-1, shp.length + 1):
                    nearCells.append([shp.rowCol[0] - i, shp.rowCol[1] - 1])
                    nearCells.append([shp.rowCol[0] - i, shp.rowCol[1] + 1])

                nearCells.append([shp.rowCol[0] - shp.length, shp.rowCol[1]])
                nearCells.append([shp.rowCol[0] + 1, shp.rowCol[1]])

                new_coords = [[shp.rowCol[0] - i, shp.rowCol[1]] for i in range(shp.length)]
            if shp.direction == 1:
                for i in range(-1, shp.length + 1):
                    nearCells.append([shp.rowCol[0] - 1, shp.rowCol[1] + i])
                    nearCells.append([shp.rowCol[0] + 1, shp.rowCol[1] + i])

                nearCells.append([shp.rowCol[0], shp.rowCol[1] - 1])
                nearCells.append([shp.rowCol[0], shp.rowCol[1] + shp.length])

                new_coords = [[shp.rowCol[0], shp.rowCol[1] + i] for i in range(shp.length)]

            nearCells = [i for i in nearCells if 0 <= i[0] < ship.MAP_SIZE and 0 <= i[1] < ship.MAP_SIZE]

            coords_in_matrix = [self.mtrx[i[0]][i[1]] for i in new_coords]

            validCoords = True
            for i in coords_in_matrix:
                if i == 1 or i == -1:
                    validCoords = False
                    break

            if validCoords:
                shp.nearCellsCoords = nearCells
                shp.coords = new_coords
                shp.isOnMap = True

                self.mark_near_cells(shp)
                self.mark_coords(shp)

    def regenerate_ships(self):
        self.ships = []
        self.mtrx = np.zeros((ship.MAP_SIZE, ship.MAP_SIZE))

        for i in range(1, 5):
            for j in range(5 - i):
                shp = ship.Ship(j + 1)
                shp.set_possible_positions()
                shp.regenerate_rowCol()
                self.put_ship(shp)
                self.ships.append(shp)

    def increment_dead_ships_count(self):
        self.dead_ships_count += 1

    def is_game_ended(self):
        return self.dead_ships_count == 10

    def mark_as_missed(self, sht):
        self.mtrx[sht.row][sht.col] = -1

    def mark_as_wounded(self, sht):
        self.mtrx[sht.row][sht.col] = 1

    def mark_coords(self, shp):
        for i in shp.coords:
            self.mtrx[i[0]][i[1]] = 1

    def mark_near_cells(self, shp):
        for i in shp.nearCellsCoords:
            self.mtrx[i[0]][i[1]] = -1

    def mark_cells(self, shp):
        self.mark_coords(shp)
        self.mark_near_cells(shp)

    def handle_shoot(self, sht):
        shot_res = result.MISSED

        for i in self.ships:
            if not i.is_dead():
                if i.was_shoot(sht):
                    i.numOfHits += 1
                    shot_res = result.WOUNDED

                    if i.is_dead():
                        self.dead_ships_count += 1
                        shot_res = result.DEAD
                    break

        if self.is_game_ended():
            shot_res = result.END_GAME

        sht.res = shot_res

    def is_shot_into_used_cell(self, sht):
        return self.mtrx[sht.row][sht.col] in [-1, 1]

    @staticmethod
    def find_ship(sht, ships):
        for i in ships:
            if i.was_shoot(sht):
                return i
