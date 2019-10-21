import random


def lotto():
    nums = [i for i in range(1, 50)]
    result = []
    ind = 0
    while ind < 6:
        try:
            number = int(input(f"Podaj 6 licz z zakresu <1; 49>, pozostalo {6 - ind}: "))
        except ValueError:
            print("Wpisana wartość musi być liczbą")
            continue
        if number in nums:
            result.append(number)
            nums.remove(number)
            ind += 1
        else:
            print("Liczby nie mogą się powtarzać ani wybiega poza zakres <1; 49>")
    print(f"Twoje liczby to: {sorted(result)}")
    lotto_numbers = random.sample(range(1, 50), 6)
    print(f"Wylosowane liczby: {sorted(lotto_numbers)}")
    winner = [number for number in result if number in lotto_numbers]
    print(f"Liczby, które trafił gracz: {winner}")
    if len(winner) >= 3:
        print(f"Trafiłeś: {len(winner)}")


lotto()
