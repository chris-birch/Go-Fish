# This is the main game and other things are imported in from other files

import subprocess as sp
import random

# function to clear the screen
def clearScreen():
    sp.call('clear', shell=True)

# Main variables
numberOfPlayers = 0
playerTypes = []
deck = []
playerHands = {}
important_veriable = "I can be removed if needed"

sp.call('clear', shell=True)

## TESTING ONLY ##
numberOfPlayers = 4
playerTypes = ['computer', 'human', 'computer', 'human']
########################################################

def numberOfPlayersInGame():
    AllOptionsChosen = False

    global numberOfPlayers
    numberOfPlayers = 0

    print("\n\nPlease enter a number between 2 and 5\n")

    while numberOfPlayers <= 1 or numberOfPlayers > 5:

        numberOfPlayers = raw_input("How many people are playing? ")

        try:
            # check if the input is a number, cast as int
            numberOfPlayers = int(numberOfPlayers)
        except ValueError:
            numberOfPlayers = 0

def setPlayerTypes():
    global numberOfPlayers

    if numberOfPlayers != 0:

        global playerTypes

        # Add extra player so the user never see's 'player 0'
        numberOfPlayersPlusOne = numberOfPlayers + 1

        # as above, add extra 1
        i = 1
        option = ''

        while i < numberOfPlayersPlusOne:

            option = raw_input("Player " + str(i)  + " will be [H]uman / [C]omputer? ")

            if option == 'h' or option == 'H':
                playerTypes.append("human")
                i = i + 1

            elif option == 'c' or option == 'C':
                playerTypes.append("computer")
                i = i + 1

            else:
                print("\n # Please choose either [H]uman / [C]omputer #\n")

    else:
        print("\n # Please choose how many players are playing first. #")

def createCards():
    # Clear current deck and generate new ones
    global deck
    deck = []
    suits = ['h', 'd', 'c', 's']
    ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

    for suitId, suitVal in enumerate(suits):
        for rankId, rankVal in enumerate(ranks):
            deck.append(rankVal+suitVal)

def dealCards():

    # create a new list of cards
    createCards()
    global deck
    global playerHands
    global playerTypes

    for id, player in enumerate(playerTypes):

        i = 0
        randomFiveCards = []
        while i < 5:

            # pick a random card from the deck and append it to the current loop (players) -
            # random cards then remove it from the deck
            currentCard = random.choice(deck)
            randomFiveCards.append(currentCard)
            deck.remove(currentCard)

            i = i + 1

        playerHands['player' + str(id)] = randomFiveCards

def goFish():
    clearScreen()
    # create and assign all players 5 random cards each

    dealCards()
    playingGame = True

    while playingGame == True:

        # each player gets a go
        for id, player in enumerate(playerTypes):

            currentTurn = True

            while currentTurn == True:
                #Print the players hand

                myHand = "You currently have"
                for cards in playerHands['player'+str(id)]:
                    myHand = myHand + cards

                    print myHand

                    currentTurn = False

            playingGame = False



# Choose game options
viewMenu = True
choice = ''

# Start the menu loop
while viewMenu == True:

    # Print menu option
    print("\n --- Game Setup ---")
    print("\n1. Number of players"), "[" + str(numberOfPlayers) + "]" if numberOfPlayers != 0 else ""
    print("2. Player types"), playerTypes
    print("3. Start game!")
    print("\n")
    print("Type 'q' to go back to main menu")
    print("\n")

    # Get a choice
    while choice != 'q':


        # Ask for the choice
        choice = raw_input("Option: ")

        # Respond to the users choice
        if choice == "1":
            numberOfPlayersInGame()
            break

        elif choice == "2":
            setPlayerTypes()
            break

        elif choice == "3":
            goFish()

        ### secret option to view teh current players hands ###
        elif choice == "4":
            print(playerHands)
        #######################################################

        elif choice == "q":
            # Exit out of loop
            viewMenu = False
            break

        else:
            clearScreen()
            print("\n # Please choose from one of the options in the menu # \n")
            break

# If exit
print("\n\nThank you for playing!\n")
