# Blackjack
# By Lucky
import random

def main()
	print("Welcome to BlackJack!!!")
	usermoney = 5000
	playing = True
	while (playing):
		try:
			checking_playing = True
			while (checking_playing):
				z = (input("Do you want to play? (y/n): ")).lower()
				if (z=="y"):
					checking_playing=False
				elif (z=="n"):
					print("Exiting game...")
					return
				else:
					print("THAT IS NOT A VALID INPUT!!!")
			checking_bet = True
			while (checking_bet):
				print("You have",usermoney,"credits")
				x = eval(input("How much would you like to bet? Credits: "))
				if (x<=5000 and x>=1):
					checking_bet = False
				elif (x<=0):
					print("You can't bet that...")
				else:
					print("You don't have that much money...")
			UserWon = BlackJack()
			if (UserWon):
				usermoney+=x
			else:
				usermoney=usermoney-x

			#If they have zero credits they lose
			if (usermoney==0):
				print("You are out of money, therefore you have lost. Thank you for playing!")
				return
		except:
			print("Something went wrong... Restarting")

def BlackJack():
	#Creating the entire deck
	deck = []
	for i in range(52):
		deck.append(1)
		#This will give a card a number
		#To calculate a card, (index//4)+1= card number
		#To calculate Suite do index%4= Suite Number

	#Give the user their first 2 cards
	#Give the house their first 2 cards
	User_Aces = 0
	Computer_Aces = 0
	deck, user1c = cardgiver(deck) #User 1st Card
	deck, comp1c = cardgiver(deck) #User 2nd Card
	deck, user2c = cardgiver(deck) #User 3rd Card
	deck, comp2c = cardgiver(deck) #User 4th Card

	#Calculates the Card Value
	user1 = ((user1c//4)+1)
	user2 = ((user2c//4)+1)
	comp1 = ((comp1c//4)+1)
	comp2 = ((comp2c//4)+1)

	#Card Names so you can tell the user
	user1N = str(user1)
	user2N = str(user2)
	comp1N = str(comp1)
	comp2N = str(comp2)

	#CHECKING FOR JACKS QUEENS KINGS AND ACES!!!
	if (user1c>=40): #THIS MEANS THE CARD IS A FACE CARD
		if (user1==11):
			user1N="Jack"
		elif (user1==12):
			user1N="Queen"
		elif (user1==13):
			user1N="King"
		user1 = 10
	if (user2c>=40):
		if (user2==11):
			user2N="Jack"
		elif (user2==12):
			user2N="Queen"
		elif (user2==13):
			user2N="King"
		user2 = 10
	if (comp1c>=40):
		if (comp1==11):
			comp1N="Jack"
		elif (user1==12):
			comp1N="Queen"
		elif (comp1==13):
			comp1N="King"
		comp1 = 10
	if (comp2c>=40):
		if (comp2==11):
			comp2N="Jack"
		elif (user2==12):
			comp2N="Queen"
		elif (comp2==13):
			comp2N="King"
		comp2 = 10

	#This accounts for specifically how many aces. You should do aces checks every once in a while 
	#to make sure if they busted their aces reduce down to 1
	if (user1==1):
		User_Aces+=1
		user1 = 11
	if (user2==1):
		User_Aces+=1
		user2 = 11
	if (comp1==1):
		Computer_Aces+=1
		comp1 = 11
	if (comp2==1):
		Computer_Aces+=1
		comp2 = 11

	usertotal = user1 + user2 #Generating User Total
	comptotal = comp1 + comp2 #Generating Computer Total
	print("Your first card was", user1N,"and your second card was",user2N,"Your total is:",usertotal)
	print("The computer's first card was", comp1N,"and the computers second card was",comp2N,"Their total is:",comptotal)

	newUname=""
	newCname=""
	playing = True
	while (playing):
		cardhitname = ''
		choice = (input("Would you like to hit or stay? ")).lower()
		if choice=="hit":
			deck, tempUcard = cardgiver(deck) #Gets the new card from the deck
			tempUnum = (tempUcard//4)+1 #Gets the value of the card
			if (tempUnum>10):
				if (tempUnum==11):
					newUname="Jack"
				elif (tempUnum==12):
					newUname="Queen"
				elif (tempUnum==13):
					newUname="King"
				tempUnum = 10
			elif (tempUnum==1):
				tempUnum=11
				User_Aces+=1
				newUname="Ace"
			else:
				newUname = str(tempUnum)
			usertotal += tempUnum #Adds that value of the card to the user
		elif choice=="stay":
			playing = False

		if (comptotal<16):
			deck, newCcard = cardgiver(deck)
			tempCnum = (newCcard//4)+1
			if (tempCnum>10):
				tempCnum=10
			comptotal += tempCnum

		if (usertotal==21):
			print("YOU WIN!!!")
			return True
		elif (usertotal>=22):
			if (User_Aces>=1):
				User_Aces=User_Aces-1
				usertotal=usertotal-10
				print("Your card was", newUname,"and your total is",usertotal)
			else:
				print("Your card was", newUname,"and your total is",usertotal)
				print("YOU BUSTED!!!")
				return False
		else:
			print("Your card was", newUname,"and your total is",usertotal)
		
	#IF THE COMPUTER HAS NOT ENOUGH CARDS
	while (comptotal<16):
		deck, newCcard = cardgiver(deck)
		tempCnum = (newCcard//4)+1
		if (tempCnum>10):
			tempCnum=10
		comptotal += tempCnum

	#NOW TO FIND THE WINNER
	winner = findwinner(usertotal,comptotal)
	return winner

def findwinner(x,y):
	if (x>=22):
		#USER BUSTED and COMP WINS
		print("YOU LOSE")
		print("You had:",x,"and the Computer had:",y)
		return False
	elif (y>=22):
		#COMP BUSTED and USER WINS
		print("YOU WIN")
		print("You had:",x,"and the Computer had:",y)
		return True
	elif (x>=y+1):
		#USER WINS
		print("YOU WIN")
		print("You had:",x,"and the Computer had:",y)
		return True
	else:
		#COMP WINS
		print("YOU LOSE")
		print("You had:",x,"and the Computer had:",y)
		return False

def cardgiver(deck):
	while (True):
		x = random.randint(0, 51)
		if (deck[x]!=0):
			deck[x] = 0
			return deck, x

main()