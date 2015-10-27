from modules import *
import winsound


def load(initial=True):
    if initial:
        action = input("Wanna defuse a bomb?\n")
    else:
        action = input("Wanna go again?\n")
    if action == "y" or action == "yes":
        begin_defusal()


def begin_defusal():
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
    if input("Vowel in serial?\n") == "y":
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
            who_is_on_first()

        if module == "memory":
            memory()

        if module == "morse":
            morse_code()

        if module == "complex":
            complicated_wires(even, parallel, batteries)

        if module == "sequence":
            wire_sequence()

        if module == "maze":
            maze()

        if module == "password":
            password()

        if module == "knobs":
            print(knobs())
            print("")

    print("CONGLATURATION")
    winsound.PlaySound("defused.wav", winsound.SND_FILENAME)

    load(False)

load()
