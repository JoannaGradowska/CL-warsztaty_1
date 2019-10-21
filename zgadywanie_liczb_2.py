from time import sleep
min = 0
max = 1000
guesses = 0
print("\nPomyśl liczbę od 0 do 1000, a ja zgadnę ją w max. 10 próbach")
sleep(1)
while True:
    sleep(1)
    guess = int((max-min)/2)+min
    print("\nZgaduję: ", guess)
    guesses += 1
    i = input("\nZa dużo(D), za mało(M)? A może zgadłam?(Z)\n")
    if i == "Z":
        if guesses > 1:
            print(f"Wygrałam w {guesses} próbach!")
            break
        else:
            print(f"Wygrałam w pierwszej próbie!")
            break
    elif i == "D":
        max = guess
    elif i == "M":
        min = guess
    else:
        print("Nie oszukuj!")