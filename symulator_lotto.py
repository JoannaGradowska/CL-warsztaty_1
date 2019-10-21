from random import sample
from time import sleep
losowanie = sample(range(1,49), 6)
wybrane = []
y = 0
while len(wybrane) < 6:
    wybrana = int(input("Podaj liczbę: "))
    if wybrana in wybrane:
        print("Już wybrałeś tę liczbę")
    elif int(wybrana) not in range(1,50):
        print("Wybierz liczbę od 1 do 49")
    else:
        wybrane.append(wybrana)
    print(wybrane)
print("\nWybrane liczby:", sorted(wybrane), "\n")
sleep(1)
print("Bęben maszyny losującej jest pusty, następuje zwolnienie blokady...\n")

sleep(2)
for numer in losowanie:
    sleep(2)
    print(numer)

print("\nWylosowane liczby:", losowanie, "\n")
for x in wybrane:

    if x in losowanie:
        y += 1
    else:
        pass
results = input("Jeśli chcesz sprawdzić czy wygrałeś wpisz TAK\n")
tak_lista = ["TAK", "tak", "TaK", "tAK", "tAk"]
if results in tak_lista:
    if y >= 3:
        print(f"Wygrałeś {y}")
    else:
        print("Niestety, nie udało Ci się nic wygrać")
else:
    "Do widzenia!"