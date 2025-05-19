import random       #imports the module to make sure we can use it

class Two_Dice_Race:    #creates a class so we can run the whole program
    def __init__(self, size=30):    #defines the global variables that can be called anywhere within the class
        self.size = size
        self.board = {}
        self.rolls = []
        self.show_board = ['_'] * size
        self.back_board = [0] * size
        self.player_a = 0
        self.player_b = 0
        self.penalty_a = True
        self.penalty_b = True
        self.last_a = 0
        self.last_b = 0

    def background_board(self):     #function to generate the board comprised of '_' for safe squares and 'P' on penalty squares with a 0.3 chance
        for i in range(self.size):
            if random.random() < 0.3:
                self.board[i] = 'P'  # Penalty square
            else:
                self.board[i] = '_'  # Safe square

    def show_background_board(self):    #a function that prints the board in the background
        for i in range(self.size):
            print(self.board[i], end='')
        print()

    def make_move(self):    #a function that controls the game choices and movements
        if self.penalty_a is True:  #rolls a dice to indicate the steps the player gets and adds it to the current player's position
            dice_roll = random.randint(1, 6)
            self.player_a += dice_roll
            self.rolls.append(dice_roll)
            try:    #adds the value of the background board by 1 to indicate whether a landed on the board or not
                self.back_board[self.player_a - 1] += 1
            except IndexError:  #if the player's position is already outside of range of the board, it will isntantly convert the player into
                #the final position on the board
                self.back_board[self.size - 1] += 1
        else:   #if player a landed on a penalty square the turn before, we don't need to roll the dice or add the value of the player's position, but append dice roll by 0
            self.rolls.append(0)
        if self.penalty_b is True:      #same as the make move part of player a, but add 2 if it lands on a square instead of 1
            dice_roll = random.randint(1, 6)
            self.player_b += dice_roll
            self.rolls.append(dice_roll)
            try:
                self.back_board[self.player_b - 1] += 2
            except IndexError:
                self.back_board[self.size - 1] += 2
        else:
            self.rolls.append(0)
        self.penalty_a = True   #resets the penalty variable to True after each rotation to make sure the penalty status of each player resets after 1 penalty turn
        self.penalty_b = True

    def display_board(self):    #generates and prints out the board to display for  the user
        for i in range(self.size):  #checks each square in on the board.
            if self.back_board[i] == 3 and self.board[i] == '_': #if both land, its 'X' in safe space and 'x' on penalty spaces. same with a and b if only one lands on a space
                self.show_board[i] = 'X'
                self.back_board[i] = 0
            elif self.back_board[i] == 2 and self.board[i] == '_':
                self.show_board[i] = 'B'
                self.back_board[i] = 0
            elif self.back_board[i] == 1 and self.board[i] == '_':
                self.show_board[i] = 'A'
                self.back_board[i] = 0
            elif self.back_board[i] == 3 and self.board[i] == 'P':  #only difference for penalty spaces here is that changes penalty values of the player who landed in the
                self.show_board[i] = 'x'    #penalty space to False so the player loses a turn
                self.back_board[i] = 0
                self.penalty_b = False
                self.penalty_a = False
                self.rolls.append(0)
                self.rolls.append(0)
            elif self.back_board[i] == 2 and self.board[i] == 'P':
                self.show_board[i] = 'b'
                self.back_board[i] = 0
                self.penalty_b = False
            elif self.back_board[i] == 1 and self.board[i] == 'P':
                self.show_board[i] = 'a'
                self.back_board[i] = 0
                self.penalty_a = False
        if self.rolls[0] == 0:      #this makes sure that a, b, and x are printed on the board even after a penalty turn has occured, making sure they do not disappear
            self.show_board[self.player_a-1] = 'a'
        if self.rolls[1] == 0:
            self.show_board[self.player_b-1] = 'b'
        if self.rolls[0] == 0 and self.player_b == self.player_a:
            self.show_board[self.player_b-1] = 'x'
        for i in self.show_board:   #prints the display board
            print(end=i)
        print('(A = %d, B = %d)' % (self.rolls[0], self.rolls[1]))  #prints the rolls player A and B got
        self.rolls = [] #resets the list so it always contains only 2 elements

    def reset(self):    #resets the display board so it only displays player positions on the current turn
        self.show_board = ['_'] * self.size

    def play_game(self):    #makes sure the program runs for as long as the final position has not been filled
        while self.show_board[self.size - 1] == '_':
            self.reset()
            self.make_move()
            self.display_board()
        if self.show_board[self.size - 1] == 'a' or self.show_board[self.size - 1] == 'A':  #once the final position is filled, prints out who wins based on the letter on the end
            print('Player A wins!')
        elif self.show_board[self.size - 1] == 'b' or self.show_board[self.size - 1] == 'B':
            print('Player B wins!')
        elif self.show_board[self.size - 1] == 'x' or self.show_board[self.size - 1] == 'X':
            print('Both players win!')
        self.show_background_board()    #shows the background board with all the penalty squares


def start_game():   #a function that runs the program/game
    game = Two_Dice_Race()
    game.background_board()
    game.play_game()


start_game()    #runs the program/game
