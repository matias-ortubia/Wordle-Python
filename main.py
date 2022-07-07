from wordle import Wordle

MAX_TRIES = 6

if __name__ == "__main__":
    with open('words.txt') as f:
        word_list = f.readlines()

    print("WORDLE\n")

    game = Wordle(word_list)

    turn = 1
    victory = False

    while turn <= MAX_TRIES and victory == False:
        print("Turn {} - ".format(turn), end='')
        input_word = input("Input a 5 letters word.\n")

        if len(input_word) != len(game.answer):
            continue

        # Check if the input word is included in the list (to see if it's a valid word)

        # Check the if the word is guessed
        result = game.compare_words(input_word)
        game.show_result(result)
        if game.check_victory(result) == True:
            victory = True
        turn += 1

    if victory == True:
        print("You win!!!")
    else:
        print("You lost\nThe word was '{}'".format(game.answer))
        
                
    
