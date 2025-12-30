import enum
import random

class State(enum.Enum):
    Green = 1
    Yellow = 2
    Grey = 3

colors = {
	State.Green: "\033[0;30m\033[42m",
	State.Yellow: "\033[0;30m\033[43m",
    State.Grey: "\033[0;30m\033[47m",
    "None": "\033[0m",
}

class Game:
    def __init__(self):
        self.wordle_words = []
        self.nguesses = 0
        self.won = False
        with open("answers.txt", "r") as f:
            for line in f:
                self.wordle_words.append(line.strip())

        self.generate_answer()


    def generate_answer(self):
        self.answer = self.wordle_words[random.randint(0, len(self.wordle_words) - 1)]

    def get_input(self):
        while True:
            guess = input("")
            if len(guess) != 5:
                print("must be length five.")
                continue

            for c in guess:
                if c.isalpha() is False:
                    print("only alphabetic characters.")
                    continue

            return guess

    def get_state(self, guess):
        out = []
        for (a, c) in zip(list(self.answer), list(guess)):
            state = State.Grey
            if c is a:
                state = State.Green
            elif c in self.answer:
                state = State.Yellow
            
            out.append((c, state))

        return out

    def print_state(self, state):
        for (char, color) in state:
            print(colors[color] + char + colors["None"], end="")

        print("")

    def run(self):
        while True:
            guess = self.get_input()
            print("\033[1A\033[K", end="")
            self.nguesses += 1
            self.print_state(self.get_state(guess))

            if guess == self.answer:
                break;
            elif self.nguesses >= 6:
                break;

# game = Game();
# game.run()
