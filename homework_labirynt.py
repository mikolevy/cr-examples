import random
import math


def generate_level(number_of_moves):
    possible_move = list(range(random.randint(2, number_of_moves)))
    move = possible_move[random.randint(0, len(possible_move) - 1)]
    return {
        "ruch": move,
        "mozliwosci": possible_move
    }


def generate_maze(level):
    maze = {}
    if level == 1:
        for i in range(5):
            maze[i] = generate_level(2)
    else:
        for i in range(8):
            maze[i] = generate_level(3)
    return maze


def count_pesimistic_possibilities(maze):
    amount = 0
    for move in maze.values():
        amount += len(move["mozliwosci"])
    return amount


def make_a_move(level, move=0):
    move += 1
    info = "wykonaj ruch: A - w lewo, D - w prawo"
    if len(level["mozliwosci"]) == 3:
        info += ", W - prosto"
    print(info)
    user_move = input('Gdzie chcesz iść?: ')
    if not ((user_move == "A" and level["ruch"] == 0)
            or (user_move == "D" and level["ruch"] == 1)
            or (user_move == "W" and level["ruch"] == 2)):
        print("zły ruch, próbuj dalej")
        return make_a_move(level, move)
    return move


def exit_the_maze(maze, MaksMove):
    player_move = 0
    for decision in maze:
        print("\ndecyzja:", decision + 1)
        player_move += make_a_move(maze[decision])
        if player_move > MaksMove:
            break
    print()
    if player_move > MaksMove:
        print("umarłeś z głodu :(")
    else:
        print("brawo, udało Ci się wydostać z labiryntu :)")
    return player_move


level = int(input("podaj poziom trudności, 1 - łatwy, 2 - trudny: "))
maze = generate_maze(level)
optimistic_move = 5 if level == 1 else 8
pesimistic_move = count_pesimistic_possibilities(maze)
death_move = optimistic_move + math.ceil((pesimistic_move - optimistic_move) * 0.6)
player_move = exit_the_maze(maze, death_move)

print("\n=== STATYSTYKI ===")
print("Wykonałeś ruchów:", player_move)
print("Minimalna ilość ruchów aby się wydostać:", optimistic_move)
print("Śmiertelna ilość ruchów:", death_move + 1)
print("=== LABIRYNT ===")
print(maze)
