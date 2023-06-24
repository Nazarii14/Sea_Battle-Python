import player
import shoot

class Game:
    def __init__(self):
        self.player1 = player.Player(1)
        self.player2 = player.Player(2)

    def move(self, first_pl, second_pl):
        print(f"{first_pl.playerNumber} shoots at {second_pl.playerNumber}")
        shot = shoot.Shoot()

        while True:
            print(f"Player {first_pl.playerNumber}, please shoot!")
            print("Your enemy map: ")
            print(first_pl.show_enemy_map())

            new_shot = first_pl.get_next_shoot()

            shot.row = new_shot.row
            shot.col = new_shot.col
            print(f"Shoot: {shot.row} {shot.col} res: {shot.res}")

            # while not shot.isValidShoot():
            #     print("You have already shot into that cell!\n")
            #     print(first_pl.show_enemy_map())
            #     shot = first_pl.get_next_shoot()

            second_pl.handle_shoot(shot)
            print(f"Shoot: {shot.row} {shot.col} res: {shot.res}")
            first_pl.update_enemy_map(shot, second_pl)

            if shot.is_missed() or shot.is_end_game():
                break

        return shot

    def start(self):
        self.player1.choose_layout()
        self.player2.choose_layout()

        while True:
            shot = self.move(self.player1, self.player2)

            if shot.is_end_game():
                print("First Player won the game!")
                self.player2.show_enemy_map()
                break


            shot = self.move(self.player2, self.player1)

            if shot.is_end_game():
                print("Second Player won the game!")
                self.player1.show_enemy_map()
                break
