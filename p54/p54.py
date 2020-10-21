"""
In the card game poker, a hand consists of five cards and are ranked, from lowest to highest, in the following way:

High Card:          Highest value card.
One Pair:           Two cards of the same value.
Two Pairs:          Two different pairs.
Three of a Kind:    Three cards of the same value.
Straight:           All cards are consecutive values.
Flush:              All cards of the same suit.
Full House:         Three of a kind and a pair.
Four of a Kind:     Four cards of the same value.
Straight Flush:     All cards are consecutive values of same suit.
Royal Flush:        Ten, Jack, Queen, King, Ace, in same suit.

The cards are valued in the order:
2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

H: Heart        Herz
D: Diamonds     Ecke
S: Spades       Schaufel
C: Clubs        Kreuz

If two players have the same ranked hands then the rank made up of the highest value wins; for example, a pair of eights beats a pair of fives (see example 1 below).
But if two ranks tie, for example, both players have a pair of queens, then highest cards in each hand are compared (see example 4 below);
if the highest cards tie then the next highest cards are compared, and so on.

The file, poker.txt, contains one-thousand random hands dealt to two players. Each line of the file contains ten cards (separated by a single space):
the first five are Player 1's cards and the last five are Player 2's cards.
You can assume that all hands are valid (no invalid characters or repeated cards), each player's hand is in no specific order, and in each hand there is a clear winner.
How many hands does Player 1 win?

Lösung:
376
"""
import math

class player():
    def __init__(self, Card_string):
        # String read from txt file eg. 8C TS KC 9H 4S
        self.card_numbers = []
        # variables to calculate Cardvalues
        self.highestCard = False
        self.havePair = False
        self.have2Pair = False
        self.have3ofAKind = False
        self.have4ofAKind = False
        self.isFlush = False
        self.isStraight = False
        self.isFullHouse = False
        self.score = 0

        # save card number in an array and check if they are all of the same sign
        card_type = -1
        for letter in Card_string:
            if letter == " ":
                continue
            # if its either H,D,S or C -> 1 of the 4 Card Types
            if "HDSC".find(letter) != -1:
                if self.isFlush == True:
                    if card_type == -1:
                        card_type = "HDSC".find(letter)
                    if card_type == "HDSC".find(letter):
                        self.isFlush = True
                    else:
                        self.isFlush = False
            
            if "23456789TJQKA".find(letter) != -1:
                self.card_numbers.append("23456789TJQKA".find(letter)+2)

    def calculate_card_score(self):
        self.card_numbers.sort()    # sort values from low to high
        self.highestCard = self.card_numbers[-1]    # save highest number
        
        for straightIndex in range(1,5):
            if (self.card_numbers[straightIndex-1] + 1) == self.card_numbers[straightIndex]:
                self.isStraight = True
                continue
            else:
                self.isStraight = False
                break

        
        # make an array with every number only once in it
        # [4,4,8,8,12] -> [4,8,12]
        unique_numbers = [] 
        for i in self.card_numbers:
            if i not in unique_numbers:
                unique_numbers.append(i)

        isFirstPair = True
        for i in unique_numbers:
            if self.card_numbers.count(i) == 2: # pair
                if isFirstPair == True: # one pair
                    self.havePair = i
                    isFirstPair = False # if there is another pair -> have2Pair
                else:                   # two pairs
                    self.have2Pair = i
            if self.card_numbers.count(i) == 3: # three of a kind
                self.have3ofAKind = i
            if self.card_numbers.count(i) == 4: # four of a kind
                self.have4ofAKind = i

        if self.have3ofAKind != False:  # full House
            if self.havePair != False:
                self.isFullHouse = True

        self.score = self.highestCard

        if self.havePair != False:
            self.score += 10 * self.havePair
        if self.have2Pair != False:
            self.score += 100 * self.have2Pair
        if self.have3ofAKind != False:
            self.score += 1000 * self.have3ofAKind
        if self.isStraight != False:
            if  self.isFlush == False:   # normal straight
                self.score += 10000 * self.highestCard
            else:   # straight or royal flush
                self.score += 100000000 * self.highestCard
        if self.isFlush != False:
            self.score += 100000 * self.highestCard
        if self.isFullHouse != False:
            self.score += 1000000 * self.have3ofAKind
        if self.have4ofAKind != False:
            self.score += 10000000 * self.have4ofAKind
        """
        High Card:          1 / 2-14
        One Pair:           10 / 20 - 240 
        Two Pairs:          100 / 200 - 1400
        Three of a Kind:    1000
        Straight:           10000
        Flush:              100000
        Full House:         1000000
        Four of a Kind:     10000000
        Straight Flush:     100000000
        Royal Flush:        1000000000
        """

        return self.score

p1_win_counter = 0

txt_file = open("poker.txt","r")
f_content = txt_file.read()
win_arr = []

for i in range(1000):
    p1 = player(str(f_content[i*30:i*30+14]))
    p2 = player(str(f_content[i*30+15:i*30+29]))

    if p1.calculate_card_score() > p2.calculate_card_score():
        p1_win_counter += 1
        win_arr.append(i)

print("Player 1 wins " + str(p1_win_counter) + " times")
