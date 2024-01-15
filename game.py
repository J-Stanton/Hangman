from random import randint


MAX_MISTAKES = 7 

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
    word = wordlist[num]
    word_letterList = []
    for k in word:
        word_letterList.append("_")
    return word,word_letterList

def insert_letter_in_guess(theLetter,theGameWord,theCorrectList):
    for k in range(len(theGameWord)):
        if theLetter == theGameWord[k]:
            theCorrectList[k] = theLetter
    return theCorrectList

def game():
    game_over = False
    mistakes = 0
    wrongLetters = []
    wordlist = read_file("words.txt")
    game_word,listCorrectSoFar = get_word(wordlist)

    while not game_over:
        print("-------------------------------------------------")
        print(listCorrectSoFar)
        print("Incorrect letters: " + ",".join(wrongLetters))
        print("Attempts:" + str(mistakes) + "/" + str(MAX_MISTAKES))

        print("Guess a letter or guess the word!")
        letter = input().lower()
        if letter==game_word:
            game_over = True
            print("well done you guessed the word!")
        elif letter in game_word:
            listCorrectSoFar = insert_letter_in_guess(letter,game_word,listCorrectSoFar)
        else:
            mistakes += 1
            if letter not in wrongLetters:
                wrongLetters.append(letter)

        if ("".join(listCorrectSoFar) == game_word):
            game_over = True
            print("congratulations")
        elif mistakes == MAX_MISTAKES:
            game_over = True
            print("unlucky the word was " + game_word)



game()