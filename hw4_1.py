import random   #imports the random module
import time     #imports the time module
class Minesweeper:  #makes a class called Minesweeper
    def __init__(self, size=9, num_mines=10):   #calls the variables inside the class so it can be globally called
        self.size = size    #the size of the sides of the board
        self.loc = [[0 for y in range(size)] for x in range(size)]  #a 2d list/array of 0s with the size of the board. This will be used in the background
        self.board = [['|   ' for j in range(size)] for i in range(size)]   #a 2d list array of the board format equal to the size of the board. This will the actual board
        self.flags = [] #empty list to indicate the locations of the flags. starts as an empty list so it can be modified later
        self.checked = []   #empty list that indicate the cells already checked in the check sides function
        self.num_mines = num_mines  #indicates the number of mines available
    def display(self):  #a function that will display the board
        print("    a   b   c   d   e   f   g   h   i")  #format of top of the board
        a = 0
        for row in range(self.size):
            print("  " + "+---" * self.size + "+")
            a += 1
            strings = ''
            for i in range(len(self.board[row])):   #checks if there is a flag on the board, if yes makes it able to be printed. otherwise just print an empty spcae
                if self.board[row][i] == '| F ':
                    strings += '| F '
                else:
                    strings += self.board[row][i]
            print(str(a) + " " + strings + '|')
        print("  " + "+---" * self.size + "+")
    def mines(self):    #makes a function that will find 10 random cells to be changed into mines
        mines_left = 0
        while mines_left < self.num_mines:  #while the number of mines left is less than 10, finds a random int between 0 and 8 to indicate the rows and columns of cell
            row = random.randint(0, self.size - 1)
            col = random.randint(0, self.size - 1)
            if self.loc[row][col] != -1:    #if the cell gotten is not already a mine, changes the value of the 0s board and add the mines count by 1 to make sure the loop ends
                self.loc[row][col] = -1
                mines_left += 1
        self.check_mines()  #runs the check mines function to check the neigbouring cell values and modify them accordingly
    def show_cells(self):   # a function that shows all the cells after the game ends
        mines = 0
        while mines < 10:   #prints the cell as an X if it has a mine
            for row in range(self.size):
                for col in range(self.size):
                    if self.loc[row][col] == -1:
                        self.board[row][col] = '| X '
                        mines += 1
        for row in range(self.size):    #prints a number indicated in the 0s board otherwise
            for col in range(self.size):
                if self.loc[row][col] != -1:
                    self.board[row][col] = '| %d '%self.loc[row][col]
    def check_mines(self):  #a function that checks and modifies the value of the cells in the 0s board depending on the cells or mines around them
        for row in range(self.size):
            for col in range(self.size):
                if self.loc[row][col] == -1:
                    continue
                if row > 0 and self.loc[row - 1][col] == -1:    #checks up, below, right, left, and diagonals
                    self.loc[row][col] = self.loc[row][col] + 1
                if row < self.size - 1 and self.loc[row + 1][col] == -1:
                    self.loc[row][col] = self.loc[row][col] + 1
                if col > 0 and self.loc[row][col - 1] == -1:
                    self.loc[row][col] = self.loc[row][col] + 1
                if col < self.size - 1 and self.loc[row][col + 1] == -1:
                    self.loc[row][col] = self.loc[row][col] + 1
                if row > 0 and col > 0 and self.loc[row - 1][col - 1] == -1:
                    self.loc[row][col] = self.loc[row][col] + 1
                if row > 0 and col < self.size - 1 and self.loc[row - 1][col + 1] == -1:
                    self.loc[row][col] = self.loc[row][col] + 1
                if row < self.size - 1 and col > 0 and self.loc[row + 1][col - 1] == -1:
                    self.loc[row][col] = self.loc[row][col] + 1
                if row < self.size - 1 and col < self.size - 1 and self.loc[row + 1][col + 1] == -1:
                    self.loc[row][col] = self.loc[row][col] + 1
    def check_sides(self, row, col):    #a function that will check the cells on the sides and modify the actual board according to it
        if [row, col] not in self.checked:
            self.checked.append([row, col]) #makes sure that the function does not recheck the same cell, otherwise an infinite recursion happens
            if self.loc[row][col] == 0:     #if the cell is an empty cell with no mines around, it will reveal all sides until it meets a non-zero
                self.board[row][col] = '| %d '%self.loc[row][col]
                if row > 0:
                    self.check_sides(row - 1, col)
                if row < self.size - 1:
                    self.check_sides(row + 1, col)
                if col > 0:
                    self.check_sides(row, col - 1)
                if col < self.size - 1:
                    self.check_sides(row, col + 1)
                if row > 0 and col > 0:
                    self.check_sides(row - 1, col - 1)
                if row > 0 and col < self.size - 1:
                    self.check_sides(row - 1, col + 1)
                if row < self.size - 1 and col > 0:
                   self.check_sides(row + 1, col - 1)
                if row < self.size - 1 and col < self.size - 1:
                    self.check_sides(row + 1, col + 1)
        if self.loc[row][col] != 0:    #if it is a non-zero cell, only reveal that cell
            self.board[row][col] = '| %d '%self.loc[row][col]
        self.display()  #displays the board
    def check_win(self):    #checks if the user wins by filling all the cells without hitting a mine
        cells = 0
        for row in range(self.size):    #counts the ammount of cells no longer empty. if it isn't empty, adds the cells by 1
            for col in range(self.size):
                if self.board[row][col] != '|   ':
                    cells += 1
        if cells <= 71: #if the ammount of cells not empty is less than 71 (the number of non-mine cells), continues the game. Otherwise, ends the game
            return True
        else:
            end_time = time.time()  #counts the time that has passed since starting the program
            duration = end_time - start_time    #reduce it by the time it took to start the game, then indicate it as the duration in seconds that have passed
            if duration < 60:   #if it is less than 60 seconds, prints that the user wins on how many seconds
                print('\nYou win! It took you %d seconds'%(duration))
            elif duration >= 60:    #if it is more than 60 seconds, convert them into minutes and seconds with the modulus and floor division operators
                minutes = duration // 60
                seconds = duration % 60
                print('\nYou win! It took you %d minutes and %d seconds.', (minutes, seconds))
            return False    #retuns False to end the game
    def make_move(self):    #a function that indicates the moves the user will make
        while True: #runs the program for as long as the value is True
            try:    #uses try and except to continuously run the program until it reaches an index error
                print("Enter the column followed by the row (ex: a5). To add or remove a flag, add \'f\' to the cell (ex: a5f). Type \'help\' to show this message again.\n")
                move = list(input("Enter the cell (10 mines left):"))   #seperates the move input into a list
                if move[0] == 'h' and move [1] == 'e' and move[2] == 'l' and move[3] == 'p':
                    self.display()  #if it is help, reprints the board and initial message and redo the loop
                    continue
                elif len(move) == 2:    #if it is a 2 character input meaning, it wants to reveal a cell
                    let = move[0]
                    col = ord(let) - 97 #changes the first value as the column by using the ord function and reduces it by 97 to find the numbered representation of it
                    row = int(move[1])-1    #the row will be the numbered input. -1 so it will not be index out of range
                    if 0 <= row <= 8 and 0 <= col <= 8: #makes sure the row and columns inputted as the cell is in the board
                        if self.board[row][col] != '| F ' and self.board[row][col] != '|   ':   #if it has already been revealed and is not a flag, it shows that the cell is
                            print("The cell is already shown")  #already planned
                            self.display()
                            continue
                        else:   #otherwise, modify the cell
                            if self.loc[row][col] == -1:    #if it hits a mine, the game ends, all the cells are shown, and a game over message is shown
                                print("\nGame Over")
                                self.show_cells()
                                self.display()
                                return False    #returns false to end the game
                            elif self.loc[row][col] == 0:   #if it is 0, runs the check_sides function and do the action according to the results they give
                                self.board[row][col] = '| 0 '
                                self.check_sides(row, col)
                            elif self.board[row][col] == '| F ':    #if it is a flag, say that there is a flag there.
                                print("There is a flag there")
                                self.display()
                                continue
                            else:
                                self.board[row][col] = '| %d '%self.loc[row][col]   #otherwise, shows the board as the numbered value of the cell
                                self.display()
                                continue    #always end each part with self.display() and continue to display the board and continue the loop
                    else:   #otherwise, shows that it is an invalid cell, reprint the initial message, and redo the loop
                        self.display()
                        print("Invalid cell.", end=' ')
                        continue
                elif len(move) == 3 and move[2] == 'f': #if it is flag input
                    let = move[0]
                    col = ord(let) - 97
                    row = int(move[1])-1    #does the same as above
                    if 0 <= row <= 8 and 0 <= col <= 8:
                        if self.board[row][col] == '| F ':  #if there is a flag already there, remove the flag in that cell from the board and the flags list
                            self.flags.remove(str(row) + str(col))
                            self.board[row][col] = '|   '
                            self.display()
                            continue
                        elif self.board[row][col] != '|   ' and self.board[row][col] != '| F ': #if the cell is already shown, show that you cannot put a flag there
                            print("Cannot put a flag there")
                            self.display()
                            continue
                        else:
                            self.flags.append(str(row) + str(col))  #otherwise, add a flag to the cell and flags list
                      =      self.board[row][col] = '| F '
                            self.display()
                            continue
                    else:
                        self.display()  #otherwise, if your input is in a cell that does not exist, or is it is not a valid input, prints invalid cell and the initial message
                        print("Invalid cell.", end=' ')
                        continue
                else:
                    self.display()
                    print("Invalid cell.", end=' ')
                    continue
            except IndexError:
                break
def start_game():   #a function to start the game
    start_time = time.time()    #starts the timer
    game = Minesweeper()    #defines the class and runs all the functions in it
    game.display()
    game.mines()
    game.make_move()
    again = input("Play again? (y/n):") #makes the user able to choose whether to end the game or re run it
    if again == 'y':    #if yes, starts the game
        start_game()
    elif again == 'n':  #if not, quits the program
        quit()
start_game()    #starts the program


