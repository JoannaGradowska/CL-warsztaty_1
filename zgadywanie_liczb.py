from random import randint
x = randint(1, 100)
while True:
    try:
        y = int((input("Zgadnij liczbę: ")))
        if x > y:
            print("Za mało!")
        elif x < y:
            print("Za dużo!")
        else:
            print("Zgadłeś")
            break
    except ValueError:
        print("To nie jest liczba naturalna")