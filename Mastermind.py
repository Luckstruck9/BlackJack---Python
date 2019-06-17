# Mastermind
# By Lucky
import random
def main():
	playing = True
	while (playing):
		mastermind()
		checking_play_again = True
		while (checking_play_again):
			play_again=(input("Would you like to play again? (y/n): ")).lower()
			if (play_again=="y"):
				checking_play_again = False 
			elif (play_again=="n"):
				checking_play_again = False
				playing = False
			else:
				print("That is not a valid option...")
	print("Thanks for playing!!!")

def mastermind():
	print("Welcome to Mastermind!!!")
	checking_rules = True
	while (checking_rules):
		rules = (input("Do you want to hear the rules? (y/n): ")).lower()
		if (rules=="y"):
			print("You must guess a 4 digit number with each digit being a number between 1 and 6 (inclusive).")
			checking_rules = False
		elif (rules=="n"):
			checking_rules = False
		else:
			print("That is not a valid input... Try again")
	#Generating Random Numbers
	s1 = str(random.randint(1,6)) 
	s2 = str(random.randint(1,6))
	s3 = str(random.randint(1,6))
	s4 = str(random.randint(1,6))
	guesses = 20
	Trying = True
	while (Trying):
		try:
			while (guesses>0):
				print("You have",guesses,"guesses left")
				guesses=guesses-1
				#code = [s1, s2, s3, s4]
				RNRP = 0 #Right Number Right Place Counter
				RNWP = 0 #Right Number Wrong Place
				user_guess=input("Your Guess: ")
				slot1 = (user_guess[0])
				slot2 = (user_guess[1])
				slot3 = (user_guess[2])
				slot4 = (user_guess[3])

				#Check for right num right place
				if (code[0]==slot1):
					RNRP+=1
					code[0]=7
					slot1=8
				if (code[1]==slot2):
					RNRP+=1
					code[1]=7 
					slot2=8
				if (code[2]==slot3):
					RNRP+=1
					code[2]=7
					slot3=8
				if (code[3]==slot4):
					RNRP+=1
					code[3]=7
					slot4=8

				total_guess = [slot1, slot2, slot3, slot4]
				#Check for right num wrong place
				for i in range (0,4):
					for j in range(0,4):
						if code[i]==total_guess[j]:
							RNWP+=1
							code[i]=7
							total_guess[j]=8
				if (RNRP==4):
					print("CONGRATULATIONS, YOU GUESSED THE CODE!!!")
					return
				print("You got",RNRP,"as the right number and right place")
				print("You got",RNWP,"as the right number in the wrong place")

		except:
			print("AN ERROR OCCURRED..")

main()