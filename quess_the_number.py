import random
from flask import Flask, request, render_template


def first_game():
    rand_num = random.randint(1, 101)
    while True:
        try:
            num = int(input("Zgadnij liczbę: "))
        except ValueError:
            print("To nie jest liczba.")
            continue

        if num > rand_num:
            print("Za dużo!")
        elif num < rand_num:
            print("Za mało!")
        else:
            print("Zgadłeś!")
            break


def second_game():
    print("Pomyśl liczbę z zakresu 0 - 1000, a ja ją zagadnę w max 10 próbach")
    minimum, maximum = 0, 1000
    allowed_answers = ('wiecej', 'mniej', 'zgadles')
    while 1:
        guess = int((maximum - minimum) / 2) + minimum
        print(f"Zgaduję: {guess}")
        answer = input("Odpowiedz: [wiecej, mniej, zgadles]: ")
        if answer in allowed_answers:
            if answer == 'zgadles':
                print(f'Twoja liczba to {guess}')
                return 'Wygrałem'
            if answer == 'wiecej':
                minimum = guess
            else:
                maximum = guess


app = Flask(__name__)


def my_guess(answer):
    global minimum
    global maximum
    result = ''
    guess = int((maximum - minimum) / 2 + minimum)
    if answer == 'zgadles':
        return "Zgadłem"
    elif answer == 'wiecej':
        minimum = guess
    elif answer == 'mniej':
        maximum = guess


@app.route('/', methods=['GET', 'POST'])
def game():
    answers = ('za duzo', 'za malo', 'wygrales')
    minimum = request.form.get('min', 0)
    maximum = request.form.get('max', 1000)
    guess = int((maximum - minimum) / 2 + minimum)
    if request.method == 'GET':
        return render_template('guessing_game.html', answer=answers, guess=guess)
    else:
        print(minimum)
        print(maximum)
        return render_template('guessing_game.html', answer=answers, guess=guess,
                               my_guess=my_guess(request.form.get('selected')))


if __name__ == '__main__':
    app.run()


# second_game()
