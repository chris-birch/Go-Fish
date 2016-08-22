# A Python version of the childrens card game Go Fish

# Clear the screen so it looks neat & tidy
import subprocess as sp

# Function to clear the screen
def clearScreen():	
	sp.call('clear', shell=True)

# How to play function
def howToPlay():
	sp.call('clear', shell=True)
	print"""
Objective of the game -

The goal is to win the most "books" of cards. A book is any four of a kind, such as four kings, four aces, and so on.

	"""

	wait = raw_input("Press RETURN to continue")
	clearScreen()


# Print main menu
clearScreen()
print("\nWelcome to the Go Fish Game! Please choose one of the following options:")

# Set an inistial empty value for choice
viewMenu = True
choice = ''

# Start the menu loop
while viewMenu == True:

	# Print menu option
	print("\n --- Main Menu ---")
	print("\n1. Start a new game of Go Fish")
	print("2. How to play")
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
			print("now starting a new gmae")
		
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