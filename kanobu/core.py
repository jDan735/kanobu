import locale
import re

if __file__ == "__main__":
    from __init__ import __version__, __logo__
else:
    from kanobu import __version__, __logo__


class Kanobu:
    def __init__(self):
        self.lang = locale.getdefaultlocale()[0] or "en_US"
        self.version = __version__.replace("a", " \033[41m Alpha ") \
                                  .replace("b", " \033[43m\033[30m Beta ")
        self.version = f"v{self.version} "
        self.name = "Rock paper scissors"
        self.objects = ["Rock", "Scissors", "Paper"]
        self.massive = [
            [2, 0, 1],
            [1, 2, 0],
            [0, 1, 2]
        ]
        self.results = [
            self.black(self.green("Win")) + " ",
            self.redbg("Loss"),
            self.black(self.yellow("Draw"))
        ]

    def game(self, players):
        self.players = players

    def logo(self):
        print(self.blue(__logo__).replace("\n", "\n "))

    def battle(self, user1, user2):
        for key in self.massive[user1.choice]:
            if user2.choice == self.massive[user1.choice].index(key):
                return self.results[key]

    def blue(self, text):
        #  \033[1;30m
        return f"\033[34m {text}\033[0m"

    def red(self, text):
        return f"\033[31m{text}\033[0m"

    def redbg(self, text):
        return f"\033[41m {text} \033[0m"

    def green(self, text):
        return f"\033[42m {text} \033[0m"

    def yellow(self, text):
        return f"\033[43m {text} \033[0m"

    def black(self, text):
        return f"\033[30m{text}\033[0m"

    def gray(self, text):
        return f"\033[1;30m{text}\033[0m"

    def test(self):
        self.game_results = [
            [
                self.battle(self.players[0], self.players[-1]),
                [self.players[0], self.players[-1]]
            ],
            [
                self.battle(*self.players[0:2]),
                self.players[0:2]
            ],
            [
                self.battle(*self.players[1:3]),
                self.players[1:3]
            ],
            [
                self.battle(*self.players[2:4]),
                self.players[2:4]
            ]
        ]

        vs = self.red('vs')

        for result in self.game_results:
            index = self.gray(self.game_results.index(result))
            users = result[1:2][0]
            print(f"{index} {result[0]}  {users[0].name} {vs} {users[1].name}")

    def rzaka(self):
        for player in self.players:
            print(f"{player.name} - {self.objects[player.choice]}")
