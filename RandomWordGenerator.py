import random
import string

alphabet = string.ascii_lowercase # List of all characters in the alphabet for checking phonetic rules...
vowels = ['a', 'e', 'i', 'o', 'u'] # List of vowels... we do NOT add y and w to this list, we want to evalulate that manually later!
proceedingConsonantVowels = ['b', 'd', 'j', 'w', 'z', 'q']  # List of proceeding consonant vowels...
nextConsonants = ['a', 'e', 'i', 'o', 'u', 't', 'r'] # List of next consonants...
consonants = [x for x in alphabet if x not in vowels] # Grab a list of consonants... (grab every letter in the alphabet that isn't a vowel obviously)

class Random_Word_Generator:

	def init(self): 

		hasLetterOrSymbolWarning = "Input contained letter or symbol! Numbers only please!" # Warning message for if the user doesn't put in a digit like we expect...

		maxWordInput = input("Words to generate: ")
		if self.gotLetterOrSymbol(maxWordInput): print(hasLetterOrSymbolWarning); return
		maxWordAmount = int(maxWordInput)

		characterLengthInput = input("Characters per-word: ")
		if self.gotLetterOrSymbol(characterLengthInput): print(hasLetterOrSymbolWarning); return
		maxCharacterLength = int(characterLengthInput)

		# Set rules, construct a random word, and print it!
		for x in range(maxWordAmount):
			self.setRules(maxWordAmount, maxCharacterLength)
			print(self.construct_word())

	def setRules(self, maxWordAmount, maxCharacterLength):
			# Set up the phonetic rules then construct a random word and print it...
			self.maxWordAmount = maxWordAmount
			self.maxCharacterLength = maxCharacterLength
			self.startLetter = [x for x in alphabet if x != 'x' and x != 'u' and x != "z"] # Store list of starting letters that aren't x, u, or z, just because those are kinda "alien" sounding...
			self.newWord = '' + self.startLetter[random.randrange(len(self.startLetter))] # Concatenate (append) a random starting letter for our new word between 0 and the length of the starting letters list...

			# aeiou and sometimes Y rules...
			self.a = [x for x in alphabet if x != 'a' and x != 'h' and x != 'u']
			self.e = [x for x in alphabet if x != 'h']
			self.i = [x for x in alphabet if x != 'i' and x != 'h' and x != 'u' and x != 'y']
			self.o = [x for x in alphabet if x != 'a' and x != 'e' and x != 'i' and x != 'y']
			self.u = [x for x in consonants if x != 'y' and x != 'u']
			self.y = ['o', 'a', 'e', 'u']

	def construct_word(self): # Constructs and returns a random word!
		while len(self.newWord) < self.maxCharacterLength:
			# Construct our new word using a bunch of vowel/consonant rules, aforementioned mind numbing english language crap! 
			# This is kinda a mess of if statements and could be done better but whatever...
			if len(self.newWord) >= 2:
				if self.newWord[-2] and self.newWord[-1] in vowels:
					self.newWord += consonants[random.randrange(len(consonants))]
				if self.newWord[-2] and self.newWord[-1] in consonants:
					self.newWord += vowels[random.randrange(len(vowels))]
			if self.newWord[-1] in vowels:
				if self.newWord[-1] == 'a':
					self.newWord += self.a[random.randrange(len(self.a))]
				if self.newWord[-1] == 'e':
					self.newWord += self.e[random.randrange(len(self.e))]
				if self.newWord[-1] == 'i':
					self.newWord += self.i[random.randrange(len(self.i))]
				if self.newWord[-1] == 'o':
					self.newWord += self.o[random.randrange(len(self.o))]
				if self.newWord[-1] == 'u':
					self.newWord += self.u[random.randrange(len(self.u))]
			if self.newWord[-1] in consonants:
				if self.newWord[-1] in proceedingConsonantVowels:
					self.newWord += vowels[random.randrange(len(vowels))]
				if self.newWord[-1] == 'y':
					self.newWord += self.y[random.randrange(len(self.y))]
				else:
					self.newWord += nextConsonants[random.randrange(len(nextConsonants))]
		self.newWord = self.newWord[0:self.maxCharacterLength] # Force max character length/truncate new word string!
		return self.newWord
	
	def gotLetterOrSymbol(self, value): 
		for character in value:
			return not character.isdigit()

while True:

	randWordGen = Random_Word_Generator()
	randWordGen.init()