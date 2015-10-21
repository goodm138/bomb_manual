from modules import *

batteries = 0
parallel = False
even = False
vowel = False
frk = False
car = False
strikes = 0
module = ""

print("Bomb Defusal V1.0\n\n")

batteries = int(input("How many batteries?\n"))

if input("Parallel port?\n") == "y":
    parallel = True

if input("Even serial?\n") == "y":
    even = True
if input("Vowel in serial?\n"):
    vowel = True

if input("Lit FRK indicator?\n") == "y":
    frk = True
if input("Lit CAR indicator?\n") == "y":
    car = True


while module != "defused":

    module = input("Which module?\n")

    if module == "strike":
        strikes += 1
        print("You now have", strikes, "strike(s)")

    if module == "wires":
        print(panel_wires(even), "\n")

    if module == "button":
        if hold_button(car, frk, batteries):
            print("HOLD")
            print("Blue = 4")
            print("White = 1")
            print("Yellow = 5")
            print("Other = 1\n")
        else:
            print("Press and release\n")

    if module == "symbols":
        keypad()
        print("")

    if module == "simon":
        simon_says(vowel, strikes)

    if module == "who":
        whos_on_first()
