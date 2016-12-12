import re

def analyze(book):

	characters = [["Arthur", "Ford", "Trillian", "Zaphod", "Marvin"], [0,0,0,0,0]]

	with open(book) as f:
		for line in f:
			line = line.strip()

			i = 0
			for char in characters[0]:
				characters[1][i] += len([m.start() for m in re.finditer(char, line)])
				i += 1

	print(characters)

for i in range(1,6):
	analyze("guide"+str(i)+".txt")