from flask import Flask, request, render_template


class Guess:
    def __init__(self):
        self.my_max = 1000
        self.my_min = 0
        self.my_guess = int((self.my_max - self.my_min) / 2 + self.my_min)
        self.click_counter = 0

    def get_answer(self, answer):
        if answer == 'trafiłeś':
            self.my_max = 1000
            self.my_min = 0
            return 'Brawo'
        if answer == 'więcej':
            self.click_counter += 1
            self.my_min = self.my_guess
        elif answer == 'mniej':
            self.my_max = self.my_guess

        self.my_guess = (self.my_max - self.my_min) / 2 + self.my_min
        return int(self.my_guess)


app = Flask(__name__)
g = Guess()


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('guessing_game.html', guess=g.my_guess)
    else:
        return render_template('guessing_game.html', guess=g.get_answer(request.form.get('ans')))


if __name__ == '__main__':
    app.run()
