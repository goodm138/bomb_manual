def panel_wires(even):
    wires = input("Input the wires\n")

    if len(wires) == 3:
        if wires.count("r") == 0:
            return "Cut second wire\n"
        if wires[2] == "w":
            return "Cut the last wire\n"
        if wires.count("u") > 1:
            return "Cut the last blue wire\n"
        return "Cut the last wire\n"

    if len(wires) == 4:
        if wires.count("r") > 1 and not even:
            return "Cut the last red wire\n"
        if wires[3] == "y" and wires.count("r") == 0:
            return "Cut the first wire\n"
        if wires.count("u") == 1:
            return "Cut the first wire\n"
        if wires.count("y") > 1:
            return "Cut the last wire\n"
        return "Cut the second wire\n"

    if len(wires) == 5:
        if wires[4] == "b" and not even:
            return "Cut the fourth wire"
        if wires.count("r") == 1 and wires.count("y") > 1:
            return "Cut the first wire"
        if wires.count("b") == 0:
            return "Cut the second wire"
        return "Cut the first wire"

    if len(wires) == 6:
        if wires.count("y") == 0 and not even:
            return "Cut the third wire"
        if wires.count("y") == 1 and wires.count("w") > 1:
            return "Cut the fourth wire"
        if wires.count("r") == 0:
            return "Cut the last wire"
        return "Cut the fourth wire"

    return "Something went wrong"


def hold_button(car, frk, batteries):
    button_color = input("What color is the button?\n")
    button_text = input("What does the button say?\n")

    if button_color == "blue" and button_text == "abort":
        return True
    if batteries > 1 and button_text == "detonate":
        return False
    if button_color == "white" and car:
        return True
    if batteries > 2 and frk:
        return False
    if button_color == "yellow":
        return True
    if button_color == "red" and button_text == "hold":
        return False

    return True


def keypad():
    column_1 = ["tennis", "a-t", "lambda", "lightning", "cat", "h", "back-c"]
    column_2 = ["back-e", "tennis", "back-c", "squiggle", "white-star", "h", "question"]
    column_3 = ["copyright", "nutsack", "squiggle", "xi", "federer", "lambda", "white-star"]
    column_4 = ["6", "paragraph", "b", "cat", "xi", "question", "smile"]
    column_5 = ["psi", "smile", "b", "c", "paragraph", "snake", "black-star"]
    column_6 = ["6", "back-e", "equal", "ae", "psi", "back-n", "omega"]

    columns = [column_1, column_2, column_3, column_4, column_5, column_6]

    print("Enter symbols, one per line\n")
    symbol_1 = input()
    symbol_2 = input()
    symbol_3 = input()
    symbol_4 = input()

    symbols = [symbol_1, symbol_2, symbol_3, symbol_4]

    correct_column = -1

    for i in range(0, 6, 1):
        if columns[i].count(symbol_1) == 1 and columns[i].count(symbol_2) == 1 and columns[i].count(symbol_3) == 1 and columns[i].count(symbol_4) == 1:
            correct_column = i
            break

    if correct_column == 0:
        print("Something went wrong, try again\n")
        keypad()

    for i in range(0, 7, 1):
        if columns[correct_column][i] in symbols:
            print(columns[correct_column][i])


def simon_says(vowel, strikes):
    color = ""

    if vowel:
        if strikes == 0:
            while color != "done":
                color = input()
                if color == "r":
                    print("blue")
                if color == "b":
                    print("red")
                if color == "g":
                    print("yellow")
                if color == "y":
                    print("green")
                if color == "strike":
                    simon_says(vowel, strikes + 1)
        if strikes == 1:
            while color != "done":
                color = input()
                if color == "r":
                    print("yellow")
                if color == "b":
                    print("green")
                if color == "g":
                    print("blue")
                if color == "y":
                    print("red")
                if color == "strike":
                    simon_says(vowel, strikes + 1)
        if strikes == 2:
            while color != "done":
                color = input()
                if color == "r":
                    print("green")
                if color == "b":
                    print("red")
                if color == "g":
                    print("yellow")
                if color == "y":
                    print("blue")
                if color == "strike":
                    simon_says(vowel, strikes + 1)

    else:
        if strikes == 0:
            while color != "done":
                color = input()
                if color == "r":
                    print("blue")
                if color == "b":
                    print("yellow")
                if color == "g":
                    print("green")
                if color == "y":
                    print("red")
                if color == "strike":
                    simon_says(vowel, strikes + 1)
        if strikes == 1:
            while color != "done":
                color = input()
                if color == "r":
                    print("red")
                if color == "b":
                    print("blue")
                if color == "g":
                    print("yellow")
                if color == "y":
                    print("green")
                if color == "strike":
                    simon_says(vowel, strikes + 1)
        if strikes == 2:
            while color != "done":
                color = input()
                if color == "r":
                    print("yellow")
                if color == "b":
                    print("green")
                if color == "g":
                    print("blue")
                if color == "y":
                    print("red")
                if color == "strike":
                    simon_says(vowel, strikes + 1)


def whos_on_first():
    display = dict()
    solutions = dict()

    display["yes"] = "Middle-left"

    solutions["ready"] = "yes, okay, what, middle, left, press, right, blank, ready"

    while True:
        current_word = input("Display says?\n")
        if current_word == "quit":
            return
        if current_word in display:
            print(display[current_word])
        else:
            print("Typo, try again")
            continue

        current_word = input()
        if current_word in solutions:
            print(solutions[current_word])
        else:
            print("Typo, try again")

    return
