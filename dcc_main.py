from dcc_character_module import Character
from dcc_dice import Dice
import sys
'''
jenkins = Character('jenkins barripple', 0)
jenkins.give_item('beer')
jenkins.roll_stats()
jenkins.get_occupation()
jenkins.describe_character()
jenkins.take_item('beer')

sys.stdout = open(f'{jenkins.name}.txt', 'w')
print(jenkins.describe_character())
input('pause')
'''

def roll_character(level=0):
	name = input("Character Name:")
	char = Character(name, level)
	char.roll_stats()
	char.get_occupation()
	char.describe_character()
	sys.stdout = open(f'characters/{char.name}.txt', 'w')
	print(char.describe_character())
	sys.stdout = sys.__stdout__
	


roll_character()



input("enter to close")