import random
import os

grid = [[0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]]

def print_grid():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=" * 31)
    print("        WELCOME TO 2048!")
    print("   Use W(up) A(left) S(down) D(right)")
    print("=" * 31)
    print()
    
    for row in grid:
        for num in row:
            if num == 0:
                print("|    ", end=" ")
            else:
                print(f"|{num:4}", end=" ")
        print("|")
        print("-" * 31)
    print()

def add_new_number():
    empty_spots = []
    for i in range(4):
        for j in range(4):
            if grid[i][j] == 0:
                empty_spots.append((i, j))
    
    if empty_spots:
        row, col = random.choice(empty_spots)
        grid[row][col] = 2 if random.random() < 0.9 else 4
        return True
    return False

def move_left():
    moved = False
    for row in range(4):
        new_row = [num for num in grid[row] if num != 0]
        
        i = 0
        while i < len(new_row) - 1:
            if new_row[i] == new_row[i + 1]:
                new_row[i] = new_row[i] * 2
                new_row.pop(i + 1)
                moved = True
            i += 1
        
        while len(new_row) < 4:
            new_row.append(0)
        
        if grid[row] != new_row:
            moved = True
        grid[row] = new_row
    
    return moved

def move_right():
    for row in range(4):
        grid[row] = grid[row][::-1]
    
    moved = move_left()
    
    for row in range(4):
        grid[row] = grid[row][::-1]
    
    return moved

def move_up():
    rotate_clockwise()
    moved = move_left()
    rotate_counter_clockwise()
    return moved

def move_down():
    rotate_clockwise()
    moved = move_right()
    rotate_counter_clockwise()
    return moved

def rotate_clockwise():
    global grid
    grid = [list(row) for row in zip(*grid[::-1])]

def rotate_counter_clockwise():
    global grid
    grid = [list(row) for row in zip(*grid)][::-1]

def check_win():
    for row in grid:
        if 2048 in row:
            return True
    return False

def check_game_over():
    for row in grid:
        if 0 in row:
            return False
    
    for i in range(4):
        for j in range(4):
            if j < 3 and grid[i][j] == grid[i][j + 1]:
                return False
            if i < 3 and grid[i][j] == grid[i + 1][j]:
                return False
    
    return True

add_new_number()
add_new_number()

game_over = False
while not game_over:
    print_grid()
    
    move = input("Enter move (W/A/S/D) or Q to quit: ").upper()
    
    if move == 'Q':
        print("Thanks for playing!")
        break
    
    moved = False
    if move == 'A':
        moved = move_left()
    elif move == 'D':
        moved = move_right()
    elif move == 'W':
        moved = move_up()
    elif move == 'S':
        moved = move_down()
    else:
        print("Invalid move! Use W, A, S, or D")
        input("Press Enter to continue...")
        continue
    
    if moved:
        add_new_number()
        
        if check_win():
            print_grid()
            print("CONGRATULATIONS! YOU REACHED 2048!")
            break
        
        if check_game_over():
            print_grid()
            print("GAME OVER! No more moves left!")
            highest = 0
            for row in grid:
                for num in row:
                    if num > highest:
                        highest = num
            print(f"Your highest tile was: {highest}")
            break
    else:
        print("Can't move that way! Try again.")
        input("Press Enter to continue...")

print()
print("Thanks for playing 2048!")