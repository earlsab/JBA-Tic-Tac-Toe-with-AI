import random

def board():
    print(f"""---------
    | {cells[0]} {cells[1]} {cells[2]} |
    | {cells[3]} {cells[4]} {cells[5]} |
    | {cells[6]} {cells[7]} {cells[8]} |
    ---------""")


def move(xy):
    global cells, num_list, move_current
    num_list = [[1, 3], [2, 3], [3, 3], [1, 2], [2, 2], [3, 2], [1, 1], [2, 1], [3, 1]]
    try:
        xy_str = xy.split()
    except AttributeError:
        xy_str = xy
    xy_int = []
    x_total = cells.count("X")
    o_total = cells.count("O")
    current_move = "X" if abs(x_total - o_total == 0) else "O"
    move_current = False
    try:
        xy_int = [int(xy) for xy in xy_str]
        xy_int = [xy for xy in xy_int if 0 < xy < 4]
        if len(xy_int) != 2:
            print("Coordinates should be from 1 to 3!")
    except ValueError:
        print("You should enter numbers!")
    if len(xy_int) == 2:
        for index in range(9):
            if xy_int == num_list[index] and cells[index] == " ":  # checks if move is legal
                cells[index] = current_move
                move_current = True
        if not move_current:
            print("This cell is occupied! Choose another one!")


def game_state():
    global repeat
    horizontal = [cells[x:x + 3] for x in range(0, len(cells), 3)]
    vertical = [cells[x:x + 7:3] for x in range(3)]
    diagonal = [cells[x:9 - x: 4 - x] for x in range(0, 3, 2)]  # this doesnt really have to be complicated :facepalm:
    game_board = [horizontal, vertical, diagonal]
    winner = []
    empty_cell_count = cells.count(" ")
    for direction in game_board:
        for line in direction:
            lead = line[0] if line[0] in ["X", "O"] else None
            winner.append(lead) if lead == line[1] and lead == line[2] else None
    if len(winner) == 1:
        print(f"{winner[0]} wins")
        repeat = False
    elif not len(winner) and empty_cell_count != 0:
        # print("Game not finished")
        pass
    elif not len(winner) and empty_cell_count == 0:
        print("Draw")
        repeat = False


def comp(level):
    empty_cells = [num_list[index] for index in range(9) if cells[index] == " "]
    if level == "easy":
        print('Making move level "easy"')
        move(random.choice(empty_cells))


def setGame(): 
    global cells, status
    if status == "ignore_menu":
        pass
    elif status == "player_menu":
        cells = "         "  # game state, start at empty
        cells = [x for x in cells]
# repeat = True
# gamerepeat = True

# while repeat:
#     setGame(input)
#     while gamerepeat:
#         move(input("Enter the coordinates: "))
#         board()
#         game_state()
#         if repeat and move_current:
#             comp("easy")
#             board


repeat = True
status = "player_menu"  # possible options "player_menu", "charactersel_menu", "ignore_menu"
while repeat:
    setGame()
    game()

#test
#test2
