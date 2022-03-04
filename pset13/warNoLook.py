from random import shuffle

class Card:
    suits = ["hearts", "diamonds", "spades", "clubs"]
    values = [None, None, '2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']

    def __init__(self, v, s):
        self.value = v
        self.suit = s
    
    def __lt__(self, c2):
        if self.value < c2.value:
            return True
        elif self.value > c2.value:
            return False
        elif self.value == c2.value:
            if self.suit < c2.suit:
                return True
            else:
                return False
    
    def __gt__(self, c2):
        if self.value > c2.value:
            return True
        elif self.value < c2.value:
            return False
        elif self.value == c2.value:
            if self.suit > c2.suit:
                return True
            else:
                return False

    def __repr__(self):
        return "{} of {}".format(self.values[self.value], self.suits[self.suit])

class Deck:
    def __init__(self):
        self.cards = []
        for i in range(2,15):
            for j in range(4):
                self.cards.append(Card(i, j))
        shuffle(self.cards)

    def rm_card(self):
        if len(self.cards) > 0:
            return self.cards.pop()

class Player:
    def __init__(self, name):
        self.name = name
        self.wins = 0
        self.card = None

class Game:
    def __init__(self):
        name1 = input("Player1 Name: ")
        name2 = input("Player2 Name: ")
        self.player1 = Player(name1)
        self.player2 = Player(name2)
        self.deck = Deck()

    def draw(self, p1n, p1c, p2n, p2c):
        return "{} drew {}, {} drew {}".format(p1n, p1c, p2n, p2c)

    def play_game(self):
        cards = self.deck.cards
        while len(cards) >= 2:
            ans = input("Type 'q' to quit. Press any key to continue")
            if ans != 'q':
                p1n = self.player1.name
                p2n = self.player2.name
                p1c = self.deck.rm_card()
                p2c = self.deck.rm_card()
                print(self.draw(p1n, p1c, p2n, p2c))
                if p1c > p2c:
                    self.player1.wins += 1
                    print("player 1 wins this round")
                else:
                    self.player2.wins += 1
                    print("player 2 wins this round")
        
        print(self.winner(self.player1, self.player2))
        
    def winner(self, player1, player2):
        if player1.wins > player2.wins:
            return player1.name + ' wins'
        if player1.wins < player2.wins:
            return player2.name + ' wins'
        else:
            return "It's a draw!"

game = Game()
game.play_game()



    