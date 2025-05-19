import pygame
import time
import random
pygame.font.init()

class Grid:
    board = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    def __init__(self, rows, cols, width, height, win):
        self.rows = rows
        self.cols = cols
        self.squares = [[Square(self.board[i][j], i, j, width, height) for j in range(cols)] for i in range(rows)]
        self.width = width
        self.height = height
        self.model = None
        self.update_model()
        self.selected = None
        self.win = win
        self.board = self.generate_board()
        self.create_puzzle()

    def generate_board(self):
        board = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        self.solve_sudoku(board)
        return board

    def solve_sudoku(self, board):
        find = find_empty(board)
        if not find:
            return True
        else:
            row, col = find

        for num in range(1, 10):
            if valid(board, num, (row, col)):
                board[row][col] = num

                if self.solve_sudoku(board):
                    return True

                board[row][col] = 0

    def create_puzzle(self):
        # Hide numbers to create initial hints
        squares_to_hide = random.sample(range(81), random.randint(48, 64))  # Adjust the range for the number of squares to hide
        for i in squares_to_hide:
            row = i // 9
            col = i % 9
            self.board[row][col] = 0

        for i in range(self.rows):
            for j in range(self.cols):
                self.squares[i][j].value = self.board[i][j]

    def update_model(self):
        self.model = [[self.squares[i][j].value for j in range(self.cols)] for i in range(self.rows)]

    def enter(self, val):
        row, col = self.selected
        if self.squares[row][col].value == 0:
            self.squares[row][col].set(val)
            self.update_model()

            if valid(self.model, val, (row,col)):
                return True
            else:
                self.squares[row][col].set(0)
                self.squares[row][col].set_pencil(0)
                self.update_model()
                return False

    def delete(self):
        row, col = self.selected
        if self.squares[row][col].value > 0:
            self.squares[row][col].set(0)
        if self.selected:
            self.squares[row][col].set_pencil(0)
            self.update_model()

    def sketch(self, val):
        row, col = self.selected
        self.squares[row][col].set_pencil(val)

    def draw(self):
        gap = self.width / 9
        for i in range(self.rows+1):
            if i % 3 == 0 and i != 0:
                thick = 4
            else:
                thick = 1
            pygame.draw.line(self.win, (0,0,0), (50, i*gap+60), (self.width+50, i*gap+60), thick)
            pygame.draw.line(self.win, (0,0,0), (i * gap+50, 60), (i * gap+50, self.height+60), thick)
            pygame.draw.line(self.win, (0,0,0), (50, gap), (self.width+50, gap), 4)
            pygame.draw.line(self.win, (0,0,0), (gap-10, 60), (gap-10, self.height+60), 4)

        for i in range(self.rows):
            for j in range(self.cols):
                self.squares[i][j].draw(self.win)

    def select(self, row, col):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.board[i][j] == 0:
                    self.squares[i][j].selected = False

        if self.board[row][col] == 0:
            self.squares[row][col].selected = True
            self.selected = (row, col)

    def click(self, pos):
        if pos[0] < self.width + 50 and pos[1] < self.height + 60:
            gap = self.width / 9
            x = (pos[0] - 50) // gap
            y = (pos[1] - 60) // gap
            return int(y), int(x)
        else:
            return None

    def solved(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.squares[i][j].value == 0:
                    return False
        return True

    def solve(self):
        find = find_empty(self.model)
        if not find:
            return True
        else:
            row, col = find

        for i in range(1, 10):
            if valid(self.model, i, (row, col)):
                self.model[row][col] = i

                if self.solve():
                    return True

                self.model[row][col] = 0

        return False

    def auto_solve(self):
        find = find_empty(self.model)
        if not find:
            return True
        else:
            row, col = find

        for i in range(1, 10):
            if valid(self.model, i, (row, col)):
                self.model[row][col] = i
                self.squares[row][col].set(i)
                self.squares[row][col].draw_squares(self.win, True)
                self.update_model()
                pygame.display.update()

                if self.auto_solve():
                    return True

                self.model[row][col] = 0
                self.squares[row][col].set(0)
                self.update_model()
                self.squares[row][col].draw_squares(self.win, False)
                pygame.display.update()

        return False

def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)

    return None


def valid(bo, num, pos):
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False

    return True

class Square:
    rows = 9
    cols = 9

    def __init__(self, value, row, col, width, height):
        self.value = value
        self.pencil = 0
        self.row = row
        self.col = col
        self.width = width
        self.height = height
        self.selected = False

    def draw(self, win):
        fnt = pygame.font.SysFont("calibri", 40)

        gap = self.width / 9
        x = self.col * gap + 50
        y = self.row * gap + 60

        if self.pencil != 0 and self.value == 0:
            text = fnt.render(str(self.pencil), 1, (128, 128, 128))
            win.blit(text, (x + 15, y + 5))
        elif not (self.value == 0):
            text = fnt.render(str(self.value), 1, (0, 0, 0))
            win.blit(text, (x + (gap / 2 - text.get_width() / 2), y + (gap / 2 - text.get_height() / 2)))

        if self.selected:
            pygame.draw.rect(win, (255, 0, 0), (x, y, gap, gap), 3)

    def draw_squares(self, win, g=True):
        fnt = pygame.font.SysFont("calibri", 40)

        gap = self.width / 9
        x = self.col * gap
        y = self.row * gap

        pygame.draw.rect(win, (255, 255, 255), (x, y, gap, gap), 0)

        text = fnt.render(str(self.value), 1, (0, 0, 0))
        win.blit(text, (x + (gap / 2 - text.get_width() / 2), y + (gap / 2 - text.get_height() / 2)))
        if g:
            pygame.draw.rect(win, (0, 255, 0), (x, y, gap, gap), 3)
        else:
            pygame.draw.rect(win, (255, 0, 0), (x, y, gap, gap), 3)

    def set(self, val):
        self.value = val

    def set_pencil(self, val):
        self.pencil = val

def redraw_window(win, board, time, wrong, game_over):
    win.fill((255,255,255))

    title_font = pygame.font.SysFont("comicsans", 50)
    title_text = title_font.render("Sudoku", True, (0, 0, 0))
    win_width = win.get_width()
    text_width = title_text.get_width()
    x_pos = (win_width - text_width) // 2
    win.blit(title_text, (x_pos, -10))

    fnt = pygame.font.SysFont("calibri", 40)
    text = fnt.render("Time: " + format_time(time), 1, (0,0,0))
    win.blit(text, (360, 680))

    text = fnt.render(f"X: {wrong}", 1, (255, 0, 0))
    win.blit(text, (20, 620))
    if game_over:
        fnt = pygame.font.SysFont("comicsans", 40)
        text = fnt.render("Puzzle Solved!!!", 1, (255,255,255), 0)
        win.blit(text, (180, 620))

    board.draw()


def format_time(secs):
    minute, sec = divmod(secs, 60)
    return f" {minute:02}:{sec:02}"


def main():
    win = pygame.display.set_mode((640,720))
    pygame.display.set_caption("Sudoku")
    board = Grid(9, 9, 540, 540, win)
    key = None
    run = True
    start = time.time()
    wrong = 0
    game_over = False
    while run:

        play_time = round(time.time() - start)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    key = 1
                if event.key == pygame.K_2:
                    key = 2
                if event.key == pygame.K_3:
                    key = 3
                if event.key == pygame.K_4:
                    key = 4
                if event.key == pygame.K_5:
                    key = 5
                if event.key == pygame.K_6:
                    key = 6
                if event.key == pygame.K_7:
                    key = 7
                if event.key == pygame.K_8:
                    key = 8
                if event.key == pygame.K_9:
                    key = 9
                if event.key == pygame.K_KP1:
                    key = 1
                if event.key == pygame.K_KP2:
                    key = 2
                if event.key == pygame.K_KP3:
                    key = 3
                if event.key == pygame.K_KP4:
                    key = 4
                if event.key == pygame.K_KP5:
                    key = 5
                if event.key == pygame.K_KP6:
                    key = 6
                if event.key == pygame.K_KP7:
                    key = 7
                if event.key == pygame.K_KP8:
                    key = 8
                if event.key == pygame.K_KP9:
                    key = 9

                if event.key == pygame.K_BACKSPACE:
                    if board.selected:
                        row, col = board.selected
                        board.delete()
                        key = None

                if event.key == pygame.K_TAB:
                    board.auto_solve()

                if event.key == pygame.K_RETURN:
                    i, j = board.selected
                    if board.squares[i][j].pencil != 0:
                        if board.enter(board.squares[i][j].pencil):
                            pass
                        else:
                            wrong += 1
                        key = None

                        if board.solved():
                            game_over = True
                            game_over_time = play_time

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                clicked = board.click(pos)
                if clicked:
                    board.select(clicked[0], clicked[1])
                    key = None

        if board.selected and key != None:
            board.sketch(key)

        redraw_window(win, board,  play_time if not game_over else game_over_time, wrong, game_over)
        pygame.display.update()


main()
pygame.quit()