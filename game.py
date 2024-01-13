from random import randint


MAX_MISTAKES = 7 
game_over = False
mistakes = 0
attempts = 0
wordlist = []
listGuessedSoFar = []

def read_file(fileName):
    tfl = open(fileName)
    words = tfl.readlines()
    tfl.close
    for k in range (len(words)-1):
        words[k] = words[k][:-1]
    return words

def guessed_word_so_far(listGuessedSoFar):
    word = ""
    for k in listGuessedSoFar:
        word = word + k
    print(word)

def get_word(wordlist):
    num = randint(0,len(wordlist)-1)
    print(wordlist[num])

