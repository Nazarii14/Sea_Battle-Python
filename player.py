import map
import shoot


class Player:
    def __init__(self, playerNumber):
        self.playerNumber = playerNumber
        self.myMap = map.Map()
        self.myMap.regenerate_ships()
        self.enemyMap = map.Map()
        self.myShoots = []

    def __str__(self):
        print("Matrix: ")
        self.myMap.print_matrix()
        return "PlayerNumber: " + str(self.playerNumber) + "\nmyShoots: " + str(self.myShoots) + "\nenemyMap: " + str(self.enemyMap)

    @property
    def playerNumber(self):
        return self._playerNumber

    @playerNumber.setter
    def playerNumber(self, value):
        self._playerNumber = value


    @property
    def myMap(self):
        return self._myMap

    @myMap.setter
    def myMap(self, value):
        self._myMap = value


    @property
    def myShoots(self):
        return self._myShoots

    @myShoots.setter
    def myShoots(self, value):
        self._myShoots = value


    @property
    def enemyMap(self):
        return self._enemyMap

    @enemyMap.setter
    def enemyMap(self, value):
        self._enemyMap = value


    def choose_layout(self):
        players_choose = False
        m = map.Map()
        m.regenerate_ships()

        while not players_choose:
            print(f"Player {self.playerNumber}, please choose ships layout!")
            m.regenerate_ships()
            print(m)
            str_choose = str(input("Do you want to play with this layout? (y - yes, n - no): "))

            if str_choose == 'y':
                players_choose = True

        print(f"Player {self.playerNumber}, you play with this layout!")
        print(m)
        self.myMap = m

    def get_next_shoot(self):
        sh = shoot.Shoot()
        input_shoot = str(input("Enter shoot (Example: A10 or J2): "))

        while len(input_shoot) > 3 or len(input_shoot) < 2:
            input_shoot = str(input("Wrong input! Enter again: "))

        letters = { 'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7, 'i':8, 'j':9 }
        sh.row = letters[input_shoot[0]]
        sh.col = int(input_shoot[1:])

        return sh

    def show_my_map(self):
        print(self._myMap)

    def show_enemy_map(self):
        print(self.enemyMap)

    def handle_shoot(self, sht):
        self.myMap.handle_shoot(sht)

    def update_enemy_map(self, sht, other_player):
        if not sht in self.myShoots:
            self.myShoots.append(sht)

        if sht.is_missed():
            self.enemyMap.mark_as_missed(sht)

        if sht.is_wounded():
            self.enemyMap.mark_as_wounded(sht)

        if sht.is_dead() or sht.is_end_game():
            self.enemyMap.mark_as_wounded(sht)
            self.enemyMap.increment_dead_ships_count()

            found_ship = self.enemyMap.find_ship(sht, other_player.myMap.ships)
            print(found_ship)

            self.enemyMap.mark_cells(found_ship)


        if sht.is_end_game():
            print("The game is ended!")
