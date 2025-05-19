import random           #imports the random module
class Blackjack:        #makes a class for the game Blackjack
    def __init__(self): #calls the variable inside the Blackjack class, making it able to be globally used
        self.ranks = ["ACE", "2", "3", "4", "5", "6", "7", "8", "9", "10", "JACK", "QUEEN", "KING"] #defines the values of the cards
        self.suits = ["SPADE", "HEART", "DIAMOND", "CLUB"]  #defines the 4 types of symbols cards have
        self.deck = []  #makes an empty list that will represent the card deck
        self.value = 0  #makes an initial variable for the values of cards the player have that can be modified later
        self.values = 0 #same as above but for dealer's cards
        self.cards = [] #an empty list that will represent the cards drawn
        self.player = []    #an empty list that will represent the cards the player currently has
        self.computer = []  #same as above but for dealer's cards
        self.cur = []       #an empty list that will represent the current card the player has
        self.curr = ''      #an empty string that shows all the cards the player has as a string format
        self.com = []       #same as above but for dealer's current card
        self.comp = ''      #same as above but for all of dealer's cards
    #step 1
    def deck_of_cards(self):    #a function that will make the deck of cards consisting of 52 unique cards
        a = []  #empty list to contain the cards
        for x in range(len(self.suits)):    #for loop that will combine the ranks and suits into 52 unique cards
            for y in range(len(self.ranks)):
                a.append(self.ranks[y] + " " + self.suits[x])
        random.shuffle(a)   #shuffles the deck
        for x in range(len(a)):
            b = a[x].split()
            self.deck.append(b) #appends the deck as a nested list
    #step 2
    def draw(self):    #a function that draws cards
        card = random.randint(0, len(self.deck)-1)  #find a random index number that will select a card from the deck
        self.cards.append(self.deck[card])  #appends the cards drawn into a list
        self.deck.pop(card) #remove the card after it has been drawn
    def initial_hand(self): #a function that only runs to find the initial cards on both the dealer and player's hand
        for x in range(4):  #draws 4 cards
            self.draw()
        self.player.append(self.cards[0])   #appends the first 2 cards for the player
        self.player.append(self.cards[1])
        self.computer.append(self.cards[2]) #appends the last 2 cards to the dealer
        self.computer.append(self.cards[3])
        self.cards.clear()
    #step 3
    def count_player(self): #a function that will count the values the cards will total on the player's hand
        for x in range(len(self.player)):   #loop that checks individual cards on the player's hand
            if self.player[x][0].isdigit(): #checks if the card has a numbered rank, if it does, turns it into an integer
                self.player[x][0] = int(self.player[x][0])
                self.value += self.player[x][0] #adds the value by the rank of the card
            elif self.player[x][0] == 'JACK' or self.player[x][0] == 'QUEEN' or self.player[x][0] == 'KING':    #if the card is a non-number rank aside from Ace
                self.value += 10    #adds the value by 10
            elif self.player[x][0] == 'ACE':    #if the card checked has an Ace rank, adds the value by 11 if the total value the player has is less than 10, add it by 1
                if self.value <= 10:            #if the value of cards the player has is more than 10
                    self.value += 11
                elif self.value > 10:
                    self.value += 1
    def count_computer(self):   #same function as above, but this calculates the dealer's cards
        self.values = 0
        for x in range(len(self.computer)):
            if self.computer[x][0].isdigit():
                self.computer[x][0] = int(self.computer[x][0])
                self.values += self.computer[x][0]
            elif self.computer[x][0] == 'JACK' or self.computer[x][0] == 'QUEEN' or self.computer[x][0] == 'KING':
                self.values += 10
            elif self.computer[x][0] == 'ACE':
                if self.values <= 10:
                    self.values += 11
                elif self.values > 10:
                    self.values += 1
    #step 4
    def player_move(self):  #a function that will dictate the player's choices
        while True: #makes sure the program continuously runs
            for x in range(len(self.player)):   #combines your current card as a string, not a list
                self.player[x][0] = str(self.player[x][0])
                self.cur.append('-'.join(self.player[x]))
                self.curr += self.cur[x] + ', '
            #step 5
            if self.value < 21: #checks if the value of your cards is less than 21, if it is, shows you the cards you have and the value
                print('\nYour current value is %d' % (self.value))
                print('with the hand:', self.curr)
            elif self.value == 21:  #if it is equal to 21, tells you that your value right now is a Blackjack set totalling 21 value
                print('Your current value is Blackjack! (21)')
                print('with the hand:', self.curr)
            elif self.value > 21:   #if it is bigger 21, tell you that your cards right now is a bust. The dealer wins and the round ends
                print('Your current value is Bust (>21)')
                print('with the hand:', self.curr)
                print('\n*** Dealer Wins ***!')
                return False    #return False will end the round since the program only runs when the value is True
            self.cur.clear()
            self.curr = ''      #resets the current cards list so it does not duplicate
            choice = int(input('\nHit or stay? (Hit = 1, Stay = 0):'))  #gives the player a choice either to draw another card or stay
            if choice == 0:     #if it is stay, it will start running the dealer's side of the game
                self.count_computer()
                self.computer_move()
                return
            elif choice == 1:   #if the player chooses to draw another card, it draws the card, adds the card to the variables, and rerun the player_move function
                self.draw()
                print('You draw', '-'.join(self.cards[0]))
                self.player.append(self.cards[0])
                print('')
                self.cards.clear()
                self.count_player()
                self.cur.clear()
                self.curr = ''
        self.player_move()
    def computer_move(self):    #function that dictates the dealer's moves
        for x in range(len(self.computer)): #same loop as player's side that adds the dealer's cards into a string
            self.computer[x][0] = str(self.computer[x][0])
            self.com.append('-'.join(self.computer[x]))
            self.comp += self.com[x] + ', '
        #step 5
        if 17 <= self.values <= 21: #if the card is beteween 17 and 21, the dealer stops drawing and tells you the value it has
            print('\nDealer\'s current value is %d ' % (self.values))
            print('with the hand:', self.comp)
            if self.values < self.value:    #this part checks which cards between you and the dealer has a higher value. Prints out the message according to the winner
                print('\n*** You beat the dealer! ***') #and retuns False to end the round
                return False    #if you win
            elif self.values == self.value: #if it is a tie
                print('\n*** You tied the dealer, nobody wins. ***')
                return False
            elif self.values > self.value:  #if dealer wins
                print('\n*** Dealer wins! ***')
        elif self.values > 21:  #if the dealer busts (their values total above 21), you win
            print('Dealer\'s current value is Bust (>21)')
            print('with the hand:', self.comp)
            print('\n*** You beat the dealer! ***')
            return False
        elif self.values == 21 and self.values > self.value: #if the dealer's cards values total 21, it's a blackjack and prints out he wins if your value is less than that
            print('Dealer\'s current value is Blackjack (21)')
            print('with the hand:', self.comp)
            print('\n*** Dealer wins! ***')
        self.com.clear()    #resets the list and variable so it does not duplicate
        self.comp = ''
        if self.values < 17:    #forces the dealer to draw a card continuously until its card values total more than or equal to 17
            self.draw()
            print('Dealer draws', '-'.join(self.cards[0]))
            self.computer.append(self.cards[0])
            self.cards.clear()
            self.count_computer()
            self.com.clear()
            self.comp = ''
            self.computer_move()
def start():    #a function to run the game
    game = Blackjack()  #runs all the functions of the game
    game.deck_of_cards()
    game.draw()
    game.initial_hand()
    game.count_player()
    game.player_move()
    #step 6
    again = input('Want to play again? (y/n):') #offers the user a choice to play another round or end the game
    if again == 'y':
        print('\n' + '-' * 40)
        start()
    else:
        quit()
start() #starts the game