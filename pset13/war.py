from operator import truediv
from random import shuffle


class Card:
    suits = ['spades', 'hearts', 'diamonds', 'clubs']
    values = [None, None, '2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']

    def __init__(self, s, v):
        self.suit = s
        self.value = v
    
    def __lt__(self, c2):
        if self.value < c2.value:
            return True
        elif self.value > c2.value:
            return False
        elif self.value == c2.value:
            if self.suit < c2.suit:
                return True
            elif self.suit > c2.suit:
                return False
    
    def __gt__(self, c2):
        if self.value > c2.value:
            return True
        elif self.value < c2.value:
            return False
        elif self.value == c2.value:
            if self.suit > c2.suit:
                return True
            elif self.suit < c2.suit:
                return False

    def __repr__(self):
        v = self.values[self.value] + " of " + self.suits[self.suit]
        return v

class Deck:
    def __init__(self):
        self.cards = []
        for i in range(2, 15):
            for j in range(4):
                self.cards.append(Card(j, i))
        shuffle(self.cards)
    
    def rm_card(self):
        if len(self.cards) == 0:
            return
        return self.cards.pop()

class Player:
    def __init__(self, name):
        self.name = name
        self.wins = 0
        self.card = None

class Game:
    def __init__(self):
        self.deck = Deck()
        name1 = input("Player 1 Name: ")
        name2 = input("Player 2 Name: ")
        self.player1 = Player(name1)
        self.player2 = Player(name2)

    def wins(self, winner):
        print("{} wins this round!".format(winner))
    
    def draw(self, p1n, p1c, p2n, p2c):
        print("{} drew {}, {} drew {}".format(p1n, p1c, p2n, p2c))

    def play_game(self):
        cards = self.deck.cards
        print("beginning war!")
        while len(cards) >= 2:
            ans = input("Type 'q' to quit. Any key to continue: ")
            if ans == 'q':
                break
            p1c = self.deck.rm_card()
            p2c = self.deck.rm_card()
            p1n = self.player1.name
            p2n = self.player2.name
            self.draw(p1n, p1c, p2n, p2c)
            if p1c > p2c:
                self.wins(p1n)
                self.player1.wins += 1
            else:
                self.wins(p2n)
                self.player2.wins += 1

        win = self.winner(self.player1, self.player2)
        print(win)
        
    def winner(self, player1, player2):
        if player1.wins > player2.wins:
            return player1.name + " wins"
        if player2.wins > player1.wins:
            return player2.name + " wins"
        return "it was a tie"
                

game = Game()
game.play_game()
        


 