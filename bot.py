import wordle

def new_counter():
    return {
        "a": 0,
        "b": 0,
        "c": 0,
        "d": 0,
        "e": 0,
        "f": 0,
        "g": 0,
        "h": 0,
        "i": 0,
        "j": 0,
        "k": 0,
        "l": 0,
        "m": 0,
        "n": 0,
        "o": 0,
        "p": 0,
        "q": 0,
        "r": 0,
        "s": 0,
        "t": 0,
        "u": 0,
        "v": 0,
        "w": 0,
        "x": 0,
        "y": 0,
        "z": 0,
    }

class Bot:
    def __init__(self):
        self.game = wordle.Game()
        self.all_guesses = self.game.wordle_words
        self.states = []
        self.frequencies = []

        for i in range(5):
            counter = new_counter() 
            for word in self.all_guesses:
                counter[word[i]] += 1

            self.frequencies.append(counter)

    def calc_score(self, word):
        sum = 0
        for (c, f) in zip(list(word), self.frequencies):
            sum += f[c]

        return sum

    def valid_word(self, word, greens, yellows, greys):
        for c, i in greens:
            if c != word[i]:
                return False

        for c, i in yellows:
            if c not in word or c == word[i]:
                return False

        for c in greys:
            if c in word:
                return False

        return True

    def remove_invalid(self):
        greens = set([])
        yellows = set([])
        greys = set([])

        for guess in self.states:
            for i, state in enumerate(guess):
                if state[1] == wordle.State.Green:
                    greens.add((state[0], i))
                elif state[1] == wordle.State.Yellow:
                    yellows.add((state[0], i))
                else:
                    greys.add(state[0])

        greens = list(greens)
        yellows = list(yellows)
        greys = list(greys)

        for word in list(self.all_guesses):
            if not self.valid_word(word, greens, yellows, greys):
                self.all_guesses.remove(word)
                continue

    def get_best(self):
        best = ""
        high = 0
        for word in self.all_guesses:
            score = self.calc_score(word)
            if score > high:
                best = word
                high = score

        return best

    def solve(self):
        guess = ""

        while guess is not self.game.answer and len(self.states) <= 5:
            guess = self.get_best()
            state = self.game.get_state(guess)
            self.game.print_state(state)
            self.states.append(state)
            self.remove_invalid()
            
        if guess == self.game.answer:
            return (True, len(self.states))
        else:
            return False, 0

# games = {
#     1: 0,
#     2: 0,
#     3: 0,
#     4: 0,
#     5: 0,
#     6: 0,
#     "loss": 0,
# }

# for i in range(1000):
#     if i % 100 == 0:
#         print(i)
        
#     (win, moves) = Bot().solve()
#     if win:
#         games[moves] += 1
#     else:
#         games["loss"] += 1
        
# print(games)

Bot().solve()
