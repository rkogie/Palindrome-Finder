import GameAssets as ga
from Program import Program


class Game:

        def __init__(self, program: Program):
            self.program = program

        def play_game(self):
            choice = ''
            print(ga.WELCOME_MESSAGE)
            choice = input()

            while choice != ga.QUIT:
                self.program.run()
                choice = input(ga.REPLAY_PROMPT)

            print(ga.GOODBYE_MESSAGE)

if __name__ == "__main__":
    program = Program()
    app = Game(program)
    app.play_game()
    
    
    
