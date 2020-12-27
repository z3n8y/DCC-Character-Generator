from pandas import read_csv as rc 
from dcc_dice import Dice

class Character():
	"""Model of a DCC character"""
	def __init__(self, name, level):
		"""Initialize the attrivutes"""
		self.name = name
		self.level = level
		self.occupation = 'none'
		self.race = 'none'
		self.character_class = 'none'
		self.stats = {}
		self.inventory = []
		'''
		self.strength = stats['str']
		self.agility = stats['agl']
		self.stamina = stats['sta']
		self.personality = stats['per']
		self.intelligence = stats['int']
		self.luck = stats['lck']'''
		self.stats_rolled = False


	def describe_character(self):
		"""Ptints out a basic character sheet including:
				-name
				-level
				-occupation
				-race
				-stats
				-inventory """
		print(f"\nName: {(self.name).title()}")
		print(f"level: {self.level}    occupation: {self.occupation}    "
			f"race: {self.race}")
		for stat, score in self.stats.items():
			print(f"\t{stat}: {score}")
		print(f"\tInventory: {self.inventory}")

	def roll_stats(self):
		"""Rolls fresh stats for a level zero character"""
		if self.stats_rolled:
			print("Character already has stats.")
		else:
			self.stats_rolled = True
			d100 = Dice(100)
			d6 = Dice(6)
			stats = ['str', 'agl', 'sta', 'per', 'int', 'lck']
			self.stats = {}
			for stat in stats:
				roll = d6.roll_dice(1, 3)
				#print(f"{stat} : {roll}")
				self.stats[stat] = roll
			
	def get_occupation(self):
		"""Obtains an occupation and starting gear from the DCC occupation table"""
		d100 = Dice(100)
		df = rc('occupations.csv')
		roll = d100.roll_dice(1)
		roll = roll - 1
		
		occupation = df.iloc[roll].values.tolist()
		self.occupation = occupation[1].strip()
		(self.inventory).append(occupation[2].strip())
		if occupation[3].strip() == 'animal':
			animals = ['chicken', 'donkey', 'goat', 'sheep', 'chicken']
			animal_dice = Dice(5)
			roll = animal_dice.roll_dice(1)
			animal = animals[roll - 1]
			self.inventory.append(animal)

		elif occupation[3].strip() == 'pushcart of...':
			produce = ['stripped dead bodies', 'cabbages', 'nothing', 'tomatoes', 'dirt', 'straw']
			produce_dice = Dice(6)
			roll = produce_dice.roll_dice(1)
			product = produce[roll - 1]
			product = "pushcart full of " + product
			self.inventory.append()
		else: 
			(self.inventory).append(occupation[3].strip())
		self.race = occupation[4].strip()

	def give_item(self, item):
		"""Gives an item to the character"""
		print(f"{self.name.title()} has obtained {item}")
		(self.inventory).append(item)
	
	def take_item(self, item):
		"""takes an item from the character"""
		print(f"{self.name.title()} has lost {item}")
		(self.inventory).remove(item)



