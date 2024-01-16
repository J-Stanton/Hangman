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

def game(theFile):
    game_over = False
    mistakes = 0
    wrongLetters = []
    wordlist = read_file(theFile)
    game_word,listCorrectSoFar = get_word(wordlist)

    while not game_over:
        print("-------------------------------------------------")
        print(" ".join(listCorrectSoFar))
        print("Incorrect letters: " + ",".join(wrongLetters))
        print("Attempts:" + str(mistakes) + "/" + str(MAX_MISTAKES))

        print("Guess a letter or guess the word!")
        letter = input().lower()

        if letter==game_word:
            game_over = True
            print("well done you guessed the word!")
        elif letter in listCorrectSoFar or letter in wrongLetters:
            print("You have guessed that letter already!")
        elif letter in game_word:
            listCorrectSoFar = insert_letter_in_guess(letter,game_word,listCorrectSoFar)
        else:
            mistakes += 1
            wrongLetters.append(letter)

        if ("".join(listCorrectSoFar) == game_word):
            game_over = True
            print("congratulations")
        elif mistakes == MAX_MISTAKES:
            game_over = True
            print("unlucky the word was " + game_word)
    return

def run_game():
    print("Welcome to hangman!")
    print("Options:")
    print("[A] Start New Game, [X] Exit")
    option = input().upper()
    while option != "X":
        if option =="A":
            print("Which topic would you like?")
            print("[A] Countires of the world, [B] Animals")
            topic = input().upper()
            if topic=="A":
                game("countries.txt")
            elif topic=="B":
                game("animals.txt")

        print("Options:")
        print("[A] Start New Game, [X] Exit")
        option = input().upper()
    print("Goodbye!")

run_game()