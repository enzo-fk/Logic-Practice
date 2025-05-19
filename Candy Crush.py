import random   #makes it so u can use random functions

class CandyCrush:   #the game denoted by class 
    def __init__(self, width, height, num_types):   #makes it so we can call global variables
        self.width = width
        self.height = height
        self.num_types = num_types
        self.board = self.generate_board()
        self.moves = 0
        self.score = 0

    def generate_board(self):   #function that generates a board by first making an array of 0s according to the height and width user inputted
        board = [[0 for _ in range(self.width)] for _ in range(self.height)]

        for i in range(self.height):    #changes this 0s to random candys types identified by numebrs starting from 1 up to the user inputted candy types
            for j in range(self.width):
                while True:
                    candy_type = random.randint(1, self.num_types)
                    if (j >= 2 and board[i][j - 1] == candy_type and board[i][j - 2] == candy_type) or \
                       (i >= 2 and board[i - 1][j] == candy_type and board[i - 2][j] == candy_type):
                        continue
                    board[i][j] = candy_type
                    break

        return board

    def eliminate_candies(self):    #function to eliminate candies by turning them into 0s, applying gravity effect on them, then turn those 0s into  new random candy types
        crushed = []

        # Check for candies to eliminate horizontally
        for i in range(self.height):
            for j in range(self.width - 2):
                if self.board[i][j] == self.board[i][j + 1] == self.board[i][j + 2] != 0:
                    candy_type = self.board[i][j]
                    count = 0
                    while j < self.width and self.board[i][j] == candy_type:
                        self.board[i][j] = 0
                        count += 1
                        self.score += 1 #adds the score according to the ammount of candies eliminated in one move,horizontally and vertically
                        j += 1
                    crushed.append((i, j - count, count, "horizontal"))

        # Check for candies to eliminate vertically
        for j in range(self.width):
            for i in range(self.height - 2):
                if self.board[i][j] == self.board[i + 1][j] == self.board[i + 2][j] != 0:
                    candy_type = self.board[i][j]
                    count = 0
                    while i < self.height and self.board[i][j] == candy_type:
                        self.board[i][j] = 0
                        count += 1
                        self.score += 1
                        i += 1
                    crushed.append((i - count, j, count, "vertical"))

        # Apply gravity system
        for j in range(self.width):
            zeros = 0
            for i in range(self.height - 1, -1, -1):
                if self.board[i][j] == 0:
                    zeros += 1
                elif zeros > 0:
                    self.board[i + zeros][j] = self.board[i][j]
                    self.board[i][j] = 0

        # Replace zeros with new candies
        for j in range(self.width):
            for i in range(self.height):
                if self.board[i][j] == 0:
                    self.board[i][j] = random.randint(1, self.num_types)

        return crushed


    def print_board(self):  #function to print the board
        for i in range(self.height):
            row = ""
            for j in range(self.width):
                if self.board[i][j] != 0:
                    row += str(self.board[i][j]) + " "
            print(row)

    def play_game(self):    #function that runs the game
        self.print_board()  #first part is to print the original board generated. Set how many turns user has, and sets a loop to run the game as long as player has moves

        end_moves = random.randint(5, 30)
        moves_left = end_moves - self.moves

        while self.moves < end_moves:
            print(f"Score: {self.score}")
            print(f"Move {self.moves + 1} | Moves Left: {moves_left}")

            while True: #lets user choose candies based on rows and columns, then make them reinput the input if they inputted incorrect or irrelevant inputs
                try:
                    row1 = int(input("Enter the row of the first candy to switch: ")) - 1
                    col1 = int(input("Enter the column of the first candy to switch: ")) - 1
                    row2 = int(input("Enter the row of the second candy to switch: ")) - 1
                    col2 = int(input("Enter the column of the second candy to switch: ")) - 1

                    if (
                            not (0 <= row1 < self.height)
                            or not (0 <= col1 < self.width)
                            or not (0 <= row2 < self.height)
                            or not (0 <= col2 < self.width)
                    ):
                        print("Invalid input. Please enter valid row and column values.")
                        continue

                    if abs(row1 - row2) > 1 or abs(col1 - col2) > 1 or (row1 == row2 and col1 == col2):
                        print("Invalid move. The selected candies must be adjacent.")
                        continue

                    self.board[row1][col1], self.board[row2][col2] = self.board[row2][col2], self.board[row1][col1] #selects the candies
                    crushed = self.eliminate_candies()
                    self.print_board()  #prints new board after elimination

                    if not crushed:
                        print("Nothing happened. Choose different candies.")
                        self.board[row1][col1], self.board[row2][col2] = self.board[row2][col2], self.board[row1][col1]
                        continue    #prints old board if no eliminations happen

                    self.moves += 1
                    moves_left = end_moves - self.moves
                    break   #decreases ur moves by one every turn

                except (ValueError, IndexError):    #if user inputs incorrect values
                    print("Invalid input. Please enter valid row and column values to choose your candies.")

        print(f"Final Score: {self.score}") #final score
        print("You are out of moves. Thank you for playing!")   #ending message


game = CandyCrush( int(input("Enter the width of the board: ")), int(input("Enter the height of the board: ")), int(input("Enter the number of candy types: ")))
game.play_game()    #runs the game and lets user input the width, height, and candy types
