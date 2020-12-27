from plotly.graph_objs import Bar, Layout
from plotly import offline

n = 14
#load roll data into list
filename = f'd{n}_rolls.txt'
with open(f"dice_tests/{filename}") as file_object:
	lines = file_object.readlines()
rolls = []
for line in lines:
	rolls.append(int(line.rstrip()))

# Analyze results
def analyze_results(results, x_title="Result", 
	y_title="Frequency", title=f"Results of rolling a D{n} {len(rolls)} times"):

	max_result = n
	frequencies = [results.count(value) for value in range(1, max_result+1)]
	x_vals = list(range(1, max_result+1))
	data = [Bar(x=x_vals, y=frequencies)]

	x_axis_config = {'title': x_title, 'dtick': 1}
	y_axis_config = {'title': y_title}
	my_layout = Layout(title=title,
		xaxis=x_axis_config, yaxis=y_axis_config
		)
	offline.plot({'data': data, 'layout': my_layout}, filename=f'graph_dump/d{n}.html')
	pass 


print(rolls)

#Make a dictionary that stores a list of every roll that comes after each possibility
what_comes_next = {}
for num in range(1, n + 1):							#for all the possible rolls
	next_roll = []
	roll_num = 0
	for roll in rolls:								#for all the times this result  
		if roll == num: 							#
			roll_num += 1							#is rolled 
			next_roll.append(rolls[roll_num])		#add the next roll to list
		
	#next_roll.sort()		
	what_comes_next[num] = next_roll

#print(what_comes_next)

# Dictionary that stores a list of every roll preceding each result.
what_comes_before = {}
for num in range(1, n + 1):							#for all the possible rolls
	next_roll = []
	roll_num = 0
	for roll in rolls:								#for all the times this result  
		if roll == num: 							#is rolled 
			next_roll.append(rolls[roll_num-1])		#add the previous roll to list
		roll_num += 1
	#next_roll.sort()		
	what_comes_before[num] = next_roll

#analyze_results(what_comes_next[11], "Next Roll", 
#	"Frequency", "Frequency of rolling any value after an 11")

def check_sequence(list_of_rolls, sequence):
	"""finds the number of occurances of a sequence 
		in a list of rolls"""
	s = len(sequence)
	occurances = 0
	roll_num = 0
	for roll in list_of_rolls:
		if roll == sequence[0]:
			roll_sequence = list_of_rolls[roll_num: roll_num + len(sequence)]
			#[list_of_rolls[roll_num], list_of_rolls[roll_num + 1]]
			if sequence == roll_sequence:
				occurances += 1
		roll_num += 1
	return occurances

doubles = {}
print("\nDoubles")
for i in range(1, n+1):
	doubles[i] = check_sequence(rolls, [i,  i])

print(doubles)
list_of_doubles = list(doubles.values())
print(list_of_doubles)

from matplotlib import pyplot as plt
#plot bars with left x-coordinates [0,1,2,3,4], heights [num_oscars]
plt.bar(range(n), list_of_doubles)

plt.title("Times Doubles Rolled")			#add title
plt.ylabel("Number of Doubles Rolled")	#add label to y
plt.xlabel("Value")							#add label to x

plt.yticks(range(2 + 1) , list(range(min(list_of_doubles), max(list_of_doubles) + 1)))
plt.xticks(range(n), list(range(1, n + 1))) 	#label x ticks

plt.show()

#print(what_comes_)
'''
analyze_results(what_comes_before[1], "Previous Roll", 
	y_title="Frequency", title=f"Frequency of rolling a 1 after a given value")


for start, results in what_comes_before.items():
	print("")
	print(start)
	print(results)

'''