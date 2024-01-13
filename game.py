MAX_MISTAKES = 7 
game_over = False
mistakes = 0
attempts = 0
wordlist = []

def read_file(fileName):
    tfl = open(fileName)
    words = tfl.readlines()
    tfl.close
    for k in range (len(words)-1):
        words[k] = words[k][:-1]
    return words

def print_guessed_word_so_far(listGuessedSoFar):
    word = ""
    for k in listGuessedSoFar:
        word = word + k + " "
    word = word[:-1]
    print(word)