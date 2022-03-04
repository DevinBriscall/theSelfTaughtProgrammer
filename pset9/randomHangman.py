import random
def hangman(word):
    wrong = 0
    stages = ["",
             "________        ",
             "|               ",
             "|        |      ",
             "|        0      ",
             "|       /|\     ",
             "|       / \     ",
             "|               "
              ]
    rletters = list(word)
    board = ["__"] * len(word)
    win = False
    print("Welcome to Hangman")
    print(" ".join(board))

    #while the player hasn't won or lost
    while (win == False and wrong < len(stages)):
        guess = input("player2 guess a letter: ")
        #check if the guess is in the list of letters
        if guess in rletters:
            ind = rletters.index(guess)
            board[ind] = guess
            rletters[ind] = '$'
            print(" ".join(board))
            # check if the letter repeats
            if guess in rletters:
                ind = rletters.index(guess)
                board[ind] = guess
                rletters[ind] = '$'
                print(" ".join(board))
            # if there are no more sblank spaces in the board then the player must have won
            if "__" not in board:
                win = True
        # if the letter wasn't in the word        
        else:
            wrong += 1
            for i in range(0, wrong):
                print(stages[i])
            print(" ".join(board))
    # after the while loop check to see if the player won or lost
    if win == False:
        print("the word was {}".format(word))
        print("Better luck next time.")
    else:
        print("YOU WIN!")

possibleWords = ['cat', 'dog', 'burrito', 'sandwich', 'pineapple']
index = random.randint(0, len(possibleWords) - 1)
hangman(possibleWords[index])
