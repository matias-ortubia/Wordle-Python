import random


class Wordle:
    '''
    Represents the game in progress.
    '''

    def __init__(self, words):
        self.words = words
        self.answer = random.choice(self.words).strip()

    def choose_word(self):
        '''
        Chooses a random word from the words array
        and updates the value of self.answer.
        '''
        self.answer = random.choice(self.words).strip()

    def compare_words(self, input_word):
        ''' Returns a list of flags
        G: the letter is in the right position
        Y: the letter is included in the word but in another position
        -: the letter is not in the word 
        '''
        length = len(self.answer)
        flags = [0] * (length)
        result = [0] * (length)

        for i in range(length):
            if input_word[i] == self.answer[i]:
                result[i] = "G"

        i_answer = 0
        i_input = 0
        while i_input < length:
            if result[i_input] == "G":
                i_input += 1
                continue

            i_answer = 0
            while i_answer < length:
                if flags[i_answer] == "Y" or result[i_input] == "Y" or result[
                        i_answer] == "G":
                    i_answer += 1
                    continue

                if self.answer[i_answer] == input_word[i_input]:
                    flags[i_answer] = "Y"
                    result[i_input] = "Y"
                    break
                i_answer += 1

            if result[i_input] != "Y":
                result[i_input] = "-"
            i_input += 1
        return result

    # Use colors here
    def show_result(self, result):
        print("{}\n".format("".join(result)))

    def check_victory(self, result):
        for flag in result:
            if flag != 'G':
                return False
        return True
