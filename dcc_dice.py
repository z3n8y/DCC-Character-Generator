from random import randint as r

class Dice():
	"""Simulated Die"""
	def __init__(self, sides):
		"""defining attributes of the dice."""
		self.sides = sides

	def roll_dice(self, number_of_rolls, number_of_dice=1):
		"""Rolls the die a number of times."""
		if number_of_dice == 1:
			for roll in range(0, number_of_rolls):
				face = r(1, self.sides)
				#print(f"Dice roll #{roll}: {face}")
				return face
		else:
			
			for roll in range(0, number_of_rolls):
				rolls = []
				for die in range(0, number_of_dice):
					face = r(1, self.sides)
					rolls.append(face)
				#print(f"{rolls} = {sum(rolls)}")

				return sum(rolls)
