import random


def the_game():
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
