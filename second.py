#Python program to build flashcard using class in Python
class flashcard:
	def __init__(self, word, meaning):
		self.word = word
		self.meaning = meaning
	def __str__(self):
	
		#we will return a string 
		return self.word+' ( '+self.meaning+' )'
	
flash = []
print("welcome to flashcard application")

#the following loop will be repeated until
#user stops to add the flashcards
while(True):
	word = input("enter the name you want to add to flashcard : ")
	meaning = input("enter the meaning of the word : ")
	
	flash.append(flashcard(word, meaning))
	option = int(input("enter 0 , if you want to add another flashcard : "))
	
	if(option):
		break
		
# printing all the flashcards 
print("\nYour flashcards")
for i in flash:
	print(">", i)
	

#Approach :
# Create a class named flashcard.
# Initialize dictionary fruits using __init__() method.
# Now randomly choose a pair from fruits using choice() method and store the key in variable fruit and value in variable color.
# Now prompt the user to answer the color of the randomly chosen fruit.
# If correct print correct else print wrong.
import random

class flashcard:
	def __init__(self):
	
		self.fruits={'apple':'red',
					'orange':'orange',
					'watermelon':'green',
					'banana':'yellow'}
		
	def quiz(self):
		while (True):
		
			fruit, color = random.choice(list(self.fruits.items()))
			
			print("What is the color of {}".format(fruit))
			user_answer = input()
			
			if(user_answer.lower() == color):
				print("Correct answer")
			else:
				print("Wrong answer")
				
			option = int(input("enter 0 , if you want to play again : "))
			if (option):
				break

print("welcome to fruit quiz ")
fc=flashcard()
fc.quiz()


#Shuffle a deck of cards using a Python random module.
# Import required modules
from random import shuffle


# Define a class to create
# all type of cards
class Cards:
	global suites, values
	suites = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
	values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

	def __init__(self):
		pass


# Define a class to categorize each card
class Deck(Cards):
	def __init__(self):
		Cards.__init__(self)
		self.mycardset = []
		for n in suites:
			for c in values:
				self.mycardset.append((c)+" "+"of"+" "+n)

	# Method to remove a card from the deck
	def popCard(self):
		if len(self.mycardset) == 0:
			return "NO CARDS CAN BE POPPED FURTHER"
		else:
			cardpopped = self.mycardset.pop()
			print("Card removed is", cardpopped)


# Define a class gto shuffle the deck of cards
class ShuffleCards(Deck):

	# Constructor
	def __init__(self):
		Deck.__init__(self)

	# Method to shuffle cards
	def shuffle(self):
		if len(self.mycardset) < 52:
			print("cannot shuffle the cards")
		else:
			shuffle(self.mycardset)
			return self.mycardset

	# Method to remove a card from the deck
	def popCard(self):
		if len(self.mycardset) == 0:
			return "NO CARDS CAN BE POPPED FURTHER"
		else:
			cardpopped = self.mycardset.pop()
			return (cardpopped)


# Driver Code
# Creating objects
objCards = Cards()
objDeck = Deck()

# Player 1
player1Cards = objDeck.mycardset
print('\n Player 1 Cards: \n', player1Cards)

# Creating object
objShuffleCards = ShuffleCards()

# Player 2
player2Cards = objShuffleCards.shuffle()
print('\n Player 2 Cards: \n', player2Cards)

# Remove some cards
print('\n Removing a card from the deck:', objShuffleCards.popCard())
print('\n Removing another card from the deck:', objShuffleCards.popCard())



# Overloading constructors based on arguments
# The constructor overloading is done by checking conditions for the arguments passed and performing the required actions. For example, consider passing an argument to the class sample, 

# If the parameter is an int, the square of the number should be the answer.
# If the parameter is a String, the answer should be “Hello!!”+string.
# If the parameter is of length greater than 1, the sum of arguments should be stored as the answer.
class sample: 

	# constructor overloading 
	# based on args 
	def __init__(self, *args): 

		# if args are more than 1 
		# sum of args 
		if len(args) > 1: 
			self.ans = 0
			for i in args: 
				self.ans += i 

		# if arg is an integer 
		# square the arg 
		elif isinstance(args[0], int): 
			self.ans = args[0]*args[0] 

		# if arg is string 
		# Print with hello 
		elif isinstance(args[0], str): 
			self.ans = "Hello! "+args[0]+"."


s1 = sample(1, 2, 3, 4, 5) 
print("Sum of list :", s1.ans) 

s2 = sample(5) 
print("Square of int :", s2.ans) 

s3 = sample("GeeksforGeeks") 
print("String :", s3.ans) 


#Calling methods from __init__
# A class can have one constructor __init__ which can perform any action when the instance of the class is created. 

# This constructor can be made to different functions that carry out different actions based on the arguments passed. Now consider an example : 

# If the number of arguments passed is 2, then evaluate the expression x = a2-b2
# If the number of arguments passed is 3, then evaluate the expression y = a2+b2-c.
# If more than 3 arguments have been passed, then sum up the squares, and divide it by the highest value in the arguments passed.
class eval_equations: 

# single constructor to call other methods 
	def __init__(self, *inp): 

		# when 2 arguments are passed 
		if len(inp) == 2: 
			self.ans = self.eq2(inp) 

		# when 3 arguments are passed 
		elif len(inp) == 3: 
			self.ans = self.eq1(inp) 

		# when more than 3 arguments are passed 
		else: 
			self.ans = self.eq3(inp) 

	def eq1(self, args): 
		x = (args[0]*args[0])+(args[1]*args[1])-args[2] 
		return x 

	def eq2(self, args): 
		y = (args[0]*args[0])-(args[1]*args[1]) 
		return y 

	def eq3(self, args): 
		temp = 0
		for i in range(0, len(args)): 
			temp += args[i]*args[i] 
		
		temp = temp/max(args) 
		z = temp 
		return z 


inp1 = eval_equations(1, 2) 
inp2 = eval_equations(1, 2, 3) 
inp3 = eval_equations(1, 2, 3, 4, 5) 

print("equation 2 :", inp1.ans) 
print("equation 1 :", inp2.ans) 
print("equation 3 :", inp3.ans) 



# Using @classmethod decorator
# @classmethod decorator allows a function to be accessible without instantiating the class. The functions can be accessed both by the instance of the class and the class itself. 

# The first parameter of the method that is declared as classmethod is cls, which is like the self of the instance methods. Here cls refer to the class itself. This proves to be very helpful in using multiple constructors in Python and is a more Pythonic approach compared to the above ones. 

# Consider the same example used above. Evaluate different expressions based on the number of inputs.
class eval_equations: 

	# basic constructor 
	def __init__(self, a): 
		self.ans = a 

	# expression 1 
	@classmethod
	def eq1(cls, args): 
		
	# create an object for the class to return 
		x = cls((args[0]*args[0])+(args[1]*args[1])-args[2]) 
		return x 

	# expression 2 
	@classmethod
	def eq2(cls, args): 
		y = cls((args[0]*args[0])-(args[1]*args[1])) 
		return y 

	# expression 3 
	@classmethod
	def eq3(cls, args): 
		temp = 0

		# square of each element 
		for i in range(0, len(args)): 
			temp += args[i]*args[i] 

		temp = temp/max(args) 
		z = cls(temp) 
		return z 


li = [[1, 2], [1, 2, 3], [1, 2, 3, 4, 5]] 
i = 0

# loop to get input three times 
while i < 3: 

	inp = li[i] 

	# no.of.arguments = 2 
	if len(inp) == 2: 
		p = eval_equations.eq2(inp) 
		print("equation 2 :", p.ans) 

	# no.of.arguments = 3 
	elif len(inp) == 3: 
		p = eval_equations.eq1(inp) 
		print("equation 1 :", p.ans) 

	# More than three arguments 
	else: 
		p = eval_equations.eq3(inp) 
		print("equation 3 :", p.ans) 

	#increment loop		 
	i += 1


