from maze import *


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
    column_1 = ["tennis", "at", "lambda", "lightning", "cat", "h", "back-c"]
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
        if symbol_1 in columns[i] and symbol_2 in columns[i] and symbol_3 in columns[i] and symbol_4 in columns[i]:
            correct_column = i
            break

    if correct_column == -1:
        print("Something went wrong, try again\n")
        keypad()

    for i in range(0, 7, 1):
        if columns[correct_column][i] in symbols:
            print(columns[correct_column][i])


def simon_says(vowel, strikes):
    while True:

        colors = input("\nEnter pattern\n")

        if colors == "done":
            return

        if colors == "strike":
            print("strike added")
            simon_says(vowel, strikes + 1)

        for i in range(0, len(colors), 1):
            if vowel:
                if strikes == 0:
                    color = colors[i]
                    if color == "r":
                        print("blue")
                    if color == "b":
                        print("red")
                    if color == "g":
                        print("yellow")
                    if color == "y":
                        print("green")
                if strikes == 1:
                    color = colors[i]
                    if color == "r":
                        print("yellow")
                    if color == "b":
                        print("green")
                    if color == "g":
                        print("blue")
                    if color == "y":
                        print("red")
                if strikes == 2:
                    color = colors[i]
                    if color == "r":
                        print("green")
                    if color == "b":
                        print("red")
                    if color == "g":
                        print("yellow")
                    if color == "y":
                        print("blue")

            else:
                if strikes == 0:
                    color = colors[i]
                    if color == "r":
                        print("blue")
                    if color == "b":
                        print("yellow")
                    if color == "g":
                        print("green")
                    if color == "y":
                        print("red")
                if strikes == 1:
                    color = colors[i]
                    if color == "r":
                        print("red")
                    if color == "b":
                        print("blue")
                    if color == "g":
                        print("yellow")
                    if color == "y":
                        print("green")
                if strikes == 2:
                    color = colors[i]
                    if color == "r":
                        print("yellow")
                    if color == "b":
                        print("green")
                    if color == "g":
                        print("blue")
                    if color == "y":
                        print("red")


def who_is_on_first():
    display = dict()
    solutions = dict()

    display["yes"] = "Middle-left"
    display["first"] = "Top-right"
    display["display"] = "Bottom-right"
    display["okay"] = "Top-right"
    display["says"] = "Bottom-right"
    display["nothing"] = "Middle-left"
    display[""] = "Bottom-left"
    display["blank"] = "Middle-right"
    display["no"] = "Bottom-right"
    display["led"] = "Middle-left"
    display["lead"] = "Bottom-right"
    display["read"] = "Middle-right"
    display["red"] = "Middle-right"
    display["reed"] = "Bottom-left"
    display["leed"] = "Bottom-left"
    display["hold on"] = "Bottom-right"
    display["you"] = "Middle-right"
    display["you are"] = "Bottom-right"
    display["your"] = "Middle-right"
    display["you're"] = "Middle-right"
    display["ur"] = "Top-left"
    display["there"] = "Bottom-right"
    display["they're"] = "Bottom-left"
    display["their"] = "Middle-right"
    display["they are"] = "Middle-left"
    display["see"] = "Bottom-right"
    display["c"] = "Top-right"
    display["cee"] = "Bottom-right"

    solutions["ready"] = "YES, OKAY, WHAT, MIDDLE, LEFT, PRESS, RIGHT, BLANK, READY"
    solutions["first"] = "LEFT, OKAY, YES, MIDDLE, NO, RIGHT, NOTHING, UHHH, WAIT, READY, BLANK, WHAT, PRESS, FIRST"
    solutions["no"] = "BLANK, UHHH, WAIT, FIRST, WHAT, READY, RIGHT, YES, NOTHING, LEFT, PRESS, OKAY, NO"
    solutions["blank"] = "WAIT, RIGHT, OKAY, MIDDLE, BLANK"
    solutions["nothing"] = "UHHH, RIGHT, OKAY, MIDDLE, YES, BLANK, NO, PRESS, LEFT, WHAT, WAIT, FIRST, NOTHING"
    solutions["yes"] = "OKAY, RIGHT, UHHH, MIDDLE, FIRST, WHAT, PRESS, READY, NOTHING, YES"
    solutions["what"] = "UHHH, WHAT"
    solutions["uhhh"] = "READY, NOTHING, LEFT, WHAT, OKAY, YES, RIGHT, NO, PRESS, BLANK, UHHH"
    solutions["left"] = "RIGHT, LEFT"
    solutions["right"] = "YES, NOTHING, READY, PRESS, NO, WAIT, WHAT, RIGHT"
    solutions["middle"] = "BLANK, READY, OKAY, WHAT, NOTHING, PRESS, NO, WAIT, LEFT, MIDDLE"
    solutions["okay"] = "MIDDLE, NO, FIRST, YES, UHHH, NOTHING, WAIT, OKAY"
    solutions["wait"] = "UHHH, NO, BLANK, OKAY, YES, LEFT, FIRST, PRESS, WHAT, WAIT"
    solutions["press"] = "RIGHT, MIDDLE, YES, READY, PRESS"
    solutions["you"] = "SURE, YOU ARE, YOUR, YOU'RE, NEXT, UH HUH, UR, HOLD, WHAT?, YOU"
    solutions["you are"] = "YOUR, NEXT, LIKE, UH HUH, WHAT?, DONE, UH UH, HOLD, YOU, U, YOU'RE, SURE, UR, YOU ARE"
    solutions["your"] = "UH UH, YOU ARE, UH HUH, YOUR"
    solutions["you're"] = "YOU, YOU'RE"
    solutions["ur"] = "DONE, U, UR"
    solutions["u"] = "UH HUH, SURE, NEXT, WHAT?, YOU'RE, UR, UH UH, DONE, U"
    solutions["uh huh"] = "UH HUH"
    solutions["uh uh"] = "UR, U, YOU ARE, YOU'RE, NEXT, UH UH"
    solutions["what?"] = "YOU, HOLD, YOU'RE, YOUR, U, DONE, UH UH, LIKE, YOU ARE, UH HUH, UR, NEXT, WHAT?"
    solutions["done"] = "SURE, UH HUH, NEXT, WHAT?, YOUR, UR, YOU'RE, HOLD, LIKE, YOU, U, YOU ARE, UH UH, DONE"
    solutions["next"] = "WHAT?, UH HUH, UH UH, YOUR, HOLD, SURE, NEXT"
    solutions["hold"] = "YOU ARE, U, DONE, UH UH, YOU, UR, SURE, WHAT?, YOU'RE, NEXT, HOLD"
    solutions["sure"] = "YOU ARE, DONE, LIKE, YOU'RE, YOU, HOLD, UH HUH, UR, SURE"
    solutions["like"] = "YOU'RE, NEXT, U, UR, HOLD, DONE, UH UH, WHAT?, UH HUH, YOU, LIKE"

    while True:
        current_word = input("Display says?\n")
        if current_word == "done":
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


def memory():
    stages = list()
    # Append dummy stage so index number will equal stage number later
    stages.append([0, 0])

    # Stage 1
    display = int(input("Display says?\n"))
    if display == 1:
        print("Position 2")
        label = input("What number was pressed?\n")
        stages.append([2, label])
    if display == 2:
        print("Position 2")
        label = input("What number was pressed?\n")
        stages.append([2, label])
    if display == 3:
        print("Position 3")
        label = input("What number was pressed?\n")
        stages.append([3, label])
    if display == 4:
        print("Fourth position")
        label = input("What number was pressed?\n")
        stages.append([4, label])

    # Stage 2
    display = int(input("Display says?\n"))
    if display == 1:
        print("Label 4")
        position = input("What position was it in?\n")
        stages.append([position, 4])
    if display == 2:
        print("Position", stages[1][0])
        label = input("What number was pressed?\n")
        stages.append([stages[1][0], label])
    if display == 3:
        print("Position 1")
        label = input("What number was pressed?\n")
        stages.append([1, label])
    if display == 4:
        print("Position", stages[1][0])
        label = input("What number was pressed?\n")
        stages.append([stages[1][0], label])

    # Stage 3
    display = int(input("Display says?\n"))
    if display == 1:
        print("Label", stages[2][1])
        position = input("What position was it in?\n")
        stages.append([position, stages[2][1]])
    if display == 2:
        print("Label", stages[1][1])
        position = input("What position was it in?\n")
        stages.append([position, stages[1][1]])
    if display == 3:
        print("Position 3")
        label = input("What number was pressed?\n")
        stages.append([3, label])
    if display == 4:
        print("Label 4")
        position = input("What position was it in?\n")
        stages.append([position, 4])

    # Stage 4
    display = int(input("Display says?\n"))
    if display == 1:
        print("Position", stages[1][0])
        label = input("What number was pressed?\n")
        stages.append([stages[1][0], label])
    if display == 2:
        print("Position 1")
        label = input("What number was pressed?\n")
        stages.append([1, label])
    if display == 3:
        print("Position", stages[2][0])
        label = input("What number was pressed?\n")
        stages.append([stages[2][0], label])
    if display == 4:
        print("Position", stages[2][0])
        label = input("What number was pressed?\n")
        stages.append([stages[2][0], label])

    # Stage 5
    display = int(input("Display says?\n"))
    if display == 1:
        print("Label", stages[1][1])
    if display == 2:
        print("Label", stages[2][1])
    if display == 3:
        print("Label", stages[4][1])
    if display == 4:
        print("Label", stages[3][1])


def morse_code():
    morse = dict()
    passwords = dict()
    morse_password = ""

    morse[".-"] = "a"
    morse["-..."] = "b"
    morse["-.-."] = "c"
    morse["."] = "e"
    morse["..-."] = "f"
    morse["--."] = "g"
    morse["...."] = "h"
    morse[".."] = "i"
    morse["-.-"] = "k"
    morse[".-.."] = "l"
    morse["--"] = "m"
    morse["-."] = "n"
    morse["---"] = "o"
    morse[".-."] = "r"
    morse["..."] = "s"
    morse["-"] = "t"
    morse["...-"] = "v"
    morse["-..-"] = "x"

    passwords["shell"] = "3.505"
    passwords["halls"] = "3.515"
    passwords["slick"] = "3.522"
    passwords["trick"] = "3.532"
    passwords["boxes"] = "3.535"
    passwords["leaks"] = "3.542"
    passwords["strobe"] = "3.545"
    passwords["bistro"] = "3.552"
    passwords["flick"] = "3.555"
    passwords["bombs"] = "3.565"
    passwords["break"] = "3.572"
    passwords["brick"] = "3.575"
    passwords["steak"] = "3.582"
    passwords["sting"] = "3.592"
    passwords["vector"] = "3.595"
    passwords["beats"] = "3.600"

    print("Enter morse, one letter per line")
    while True:
        current_letter = input()

        if current_letter == "done":
            break

        if current_letter in morse:
            morse_password += morse[current_letter]
        else:
            print("Invalid letter, restart")
            morse_code()

    if morse_password in passwords:
        print(morse_password, passwords[morse_password])
    else:
        print("No password found, try again")
        morse_code()


def complicated_wires(even, parallel, batteries):
    wire_count = int(input("How many wires?\n"))
    wires_to_cut = list()

    print("Enter wires, one per line")
    for i in range(0, wire_count, 1):
        current_wire = input()

        # C - always cut
        if current_wire == "w":
            wires_to_cut.append(i + 1)
        if current_wire == "rs":
            wires_to_cut.append(i + 1)
        if current_wire == "ws":
            wires_to_cut.append(i + 1)

        # S - cut if serial number is even
        if even:
            if current_wire == "r":
                wires_to_cut.append(i + 1)
            if current_wire == "b":
                wires_to_cut.append(i + 1)
            if current_wire == "rb":
                wires_to_cut.append(i + 1)
            if current_wire == "rbl":
                wires_to_cut.append(i + 1)

        # P - cut if we have parallel port
        if parallel:
            if current_wire == "rbs":
                wires_to_cut.append(i + 1)
            if current_wire == "bl":
                wires_to_cut.append(i + 1)
            if current_wire == "bls":
                wires_to_cut.append(i + 1)

        # B - cut if >= 2 batteries
        if batteries >= 2:
            if current_wire == "wls":
                wires_to_cut.append(i + 1)
            if current_wire == "rl":
                wires_to_cut.append(i + 1)
            if current_wire == "rls":
                wires_to_cut.append(i + 1)

    print("Cut wires:")

    for i in range(0, len(wires_to_cut), 1):
        print(wires_to_cut[i], " ")

    print("")


def wire_sequence():
    red = ["c", "b", "a", "ac", "b", "ac", "abc", "ab", "b"]
    blue = ["b", "ac", "b", "a", "b", "bc", "c", "ac", "a"]
    black = ["abc", "ac", "b", "ac", "b", "bc", "ab", "c", "c"]

    current_red = 0
    current_blue = 0
    current_black = 0

    print("Enter wires, one per line (BLUE = u)")
    while True:
        current_wire = input()

        if current_wire == "done":
            return

        if current_wire[0] == "r":
            if current_wire[1] in red[current_red]:
                print("Cut")
            else:
                print("Leave")
            current_red += 1

        if current_wire[0] == "u":
            if current_wire[1] in blue[current_blue]:
                print("Cut")
            else:
                print("Leave")
            current_blue += 1

        if current_wire[0] == "b":
            if current_wire[1] in black[current_black]:
                print("Cut")
            else:
                print("Leave")
            current_black += 1


def maze():
    marker_1 = input("Marker 1 at:\n")
    marker_2 = input("Marker 2 at:\n")

    start = input("Current position:\n")
    end = input("Goal position:\n")

    maze_layout = get_maze(marker_1, marker_2)

    path = maze_search(maze_layout, start, end)

    print_path(path)


def password():
    passwords = [
        "about", "after", "again", "below", "could",
        "every", "first", "found", "great", "house",
        "large", "learn", "never", "other", "place",
        "plant", "point", "right", "small", "sound",
        "spell", "still", "study", "their", "there",
        "these", "thing", "think", "three", "water",
        "where", "which", "world", "would", "write"
    ]

    columns = list()

    print("Enter the letters, one column per line")

    columns.append(input("column 1: "))
    columns.append(input("column 2: "))

    possibilities = list()

    for i in range(0, 6, 1):
        for j in range(0, 6, 1):
            word = columns[0][i] + columns[1][j]
            for k in range(0, len(passwords), 1):
                if passwords[k].startswith(word):
                    possibilities.append(passwords[k])

    if len(possibilities) == 1:
        print(possibilities[0])
        return
    else:
        del possibilities[:]

    columns.append(input("column 3: "))

    for i in range(0, 6, 1):
        for j in range(0, 6, 1):
            for k in range(0, 6, 1):
                word = columns[0][i] + columns[1][j] + columns[2][k]
                for l in range(0, len(passwords), 1):
                    if passwords[l].startswith(word):
                        possibilities.append(passwords[l])

    if len(possibilities) == 1:
        print(possibilities[0])
        return
    else:
        del possibilities[:]

    columns.append(input("column 4: "))

    for i in range(0, 6, 1):
        for j in range(0, 6, 1):
            for k in range(0, 6, 1):
                for l in range(0, 6, 1):
                    word = columns[0][i] + columns[1][j] + columns[2][k] + columns[3][l]
                    for m in range(0, len(passwords), 1):
                        if passwords[m].startswith(word):
                            possibilities.append(passwords[m])

    if len(possibilities) == 1:
        print(possibilities[0])
        return
    else:
        for poss in possibilities:
            print(poss)

    columns.append(input("column 5: "))

    for i in range(0, 6, 1):
        for j in range(0, 6, 1):
            for k in range(0, 6, 1):
                for l in range(0, 6, 1):
                    for m in range(0, 6, 1):
                        word = columns[0][i] + columns[1][j] + columns[2][k] + columns[3][l] + columns[4][m]
                        if word in passwords:
                            print(word)


def knobs():
    top_row = input("Top row?\n")
    if top_row == "135":
        bottom_row = input("Bottom row?\n")
        if bottom_row == "2356":
            return "Up"
        else:
            return "Down"
    if top_row == "356":
        return "Up"
    if top_row == "236":
        return "Down"
    if top_row == "5":
        return "Left"
    if top_row == "13456" or top_row == "134":
        return "Right"
