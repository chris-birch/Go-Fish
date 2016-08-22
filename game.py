# The main game...

import subprocess as sp


numberOfPlayers = 0
playerTypes = {}

# Function to clear the screen
def clearScreen():	
	sp.call('clear', shell=True)

def numberOfPlayersInGame():	
	AllOptionsChosen = False

	while AllOptionsChosen == False:
		global numberOfPlayers

		while numberOfPlayers <=0 and numberOfPlayers <=5:
			numberOfPlayers = int(raw_input("How many people are playing? "))
			
			#AllOptionsChosen = True
		break

	print numberOfPlayers





# Choose game options
viewMenu = True
choice = ''

# Start the menu loop
while viewMenu == True:

	# Print menu option
	print("\n --- Game Setup ---")
	print("\n1. Number of players")
	print("2. Game Mode")
	print("3. More information")
	print("\n")
	print("Type 'q' to quit")
	print("\n")

	# Get a choice
	while choice != 'q':
		

		# Ask for the choice
		choice = raw_input("Option: ")

		# Respond to the users choice
		if choice == "1":
			numberOfPlayersInGame()
		
		elif choice == "2":
			howToPlay()
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
