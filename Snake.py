import msvcrt   #imports necessary modules
import random
import os
import shutil


def clear_screen(): #clears the screen after every repition
    os.system("cls" if os.name == "nt" else "clear")


def get_key():
    if msvcrt.kbhit():
        key = msvcrt.getch()
        return ord(key)
    return None


def draw_screen(snake, food, obstacles, score):
    screen = [[" " for _ in range(screen_width)] for _ in range(screen_height - 1)]

    for obstacle in obstacles:  #obstacles
        for x, y in obstacle:
            screen[y][x] = "#"

    for segment in snake:   #snake
        x, y = segment
        screen[y][x] = "O"

    x, y = food
    if is_special_food: #food. special as X normal as phi
        screen[y][x] = "X"
    else:
        screen[y][x] = "π"

    clear_screen()
    for row in screen:
        print("".join(row))



def move_snake(snake, direction):   #how snake move
    head = snake[0]
    x, y = head

    if direction == "up":
        y -= 1
    elif direction == "down":
        y += 1
    elif direction == "left":
        x -= 1
    elif direction == "right":
        x += 1

    head = [x, y]
    snake.insert(0, head)

    return snake


def generate_food(snake, obstacles):    #generates food
    while True:
        x = random.randint(0, screen_width - 1)
        y = random.randint(0, screen_height - 2)
        if [x, y] not in snake and [x, y] not in obstacles:
            # Determine if the generated food is special or normal
            if random.random() < 0.7:
                return [x, y], True  # Special food
            else:
                return [x, y], False  # Normal food


def generate_obstacles():   #generates obstacles with 5% of cells
    obstacles = []
    total_cells = screen_width * (screen_height - 1)
    num_obstacles = int(total_cells * 0.003)  # 5% of the total cells

    for _ in range(num_obstacles):
        obstacle_length = random.randint(5, 10)
        is_horizontal = random.choice([True, False])

        if is_horizontal:
            x = random.randint(0, screen_width - obstacle_length)
            y = random.randint(0, screen_height - 2)
            obstacle = [[x + i, y] for i in range(obstacle_length)]
        else:
            x = random.randint(0, screen_width - 1)
            y = random.randint(0, screen_height - obstacle_length - 2)
            obstacle = [[x, y + i] for i in range(obstacle_length)]

        obstacles.append(obstacle)

    return obstacles


# Initialize the game variables #creates variables to be called at the end of game
screen_width, screen_height = shutil.get_terminal_size()
snake = [[3, 2], [2, 2], [1, 2]]
food, is_special_food = generate_food(snake, [])
obstacles = generate_obstacles()
score = 0
direction = "right"
normal_food_count = 0
special_food_count = 0

# Makes sure game loops until game over
while True:
    draw_screen(snake, food, obstacles, score)
    key = get_key()

    if key == 224:
        key = get_key()
        if key == 72 and direction != "down" and direction != "up":  # up arrow
            direction = "up"
        elif key == 80 and direction != "up" and direction != "down":  # down arrow
            direction = "down"
        elif key == 75 and direction != "right" and direction != "left":  # left arrow
            direction = "left"
        elif key == 77 and direction != "left" and direction != "right":  # right arrow
            direction = "right"
    elif key == 32:  # spacebar to pause
        input("Paused. Press Enter to continue...")
        continue

    snake = move_snake(snake, direction)
    head = snake[0]
    x, y = head

    if [x, y] == food:
        score += 1
        if is_special_food and len(snake) > 1:
            snake.pop()
            snake.pop()  # Shrink the snake by removing the tail
            special_food_count += 1
        else:
            normal_food_count += 1
        food, is_special_food = generate_food(snake, obstacles)
    else:
        snake.pop()

    if x < 0:
        x = screen_width - 1
    elif x >= screen_width:
        x = 0
    elif y < 0:
        y = screen_height - 2
    elif y >= screen_height - 1:
        y = 0

    head = [x, y]
    snake[0] = head

    if (
        head in snake[1:]
        or any(head in obstacle for obstacle in obstacles)
    ):
        break

# Prints board and message if game is over
draw_screen(snake, food, obstacles, score)
if head in snake[1:]:
    print("Game over because of Hit self.")
elif any(head in obstacle for obstacle in obstacles):
    print("Game over because of Hit obstacle.")
else:
    print("Game over because of unknown reason.")

print('You ate %d normal food and %d special food'%(normal_food_count,special_food_count))
