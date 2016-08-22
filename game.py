# The main game...

import subprocess as sp

# Main variables
numberOfPlayers = 0
playerTypes = []
cards = []

# Function to clear the screen
def clearScreen():	
	sp.call('clear', shell=True)

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

	if numberOfPlayers != 0:

		global playerTypes

		# Add extra player so the user never see's 'player 0'
		numberOfPlayers = numberOfPlayers + 1

		# as above, add extra 1
		i = 1
		option = ''

		while i < numberOfPlayers:

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


def goFish():
	# create a new list of cards
	createCards()



# Choose game options
viewMenu = True
choice = ''

# Start the menu loop
while viewMenu == True:

	# Print menu option
	print("\n --- Game Setup ---")
	print("\n1. Number of players"), "[" + str(numberOfPlayers) + "]" if numberOfPlayers != 0 else ""
	print("2. Player types")
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
			print("This is some more information on how the game works")

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
