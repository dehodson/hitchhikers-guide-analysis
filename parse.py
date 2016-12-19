import re

characters = ["Arthur", "Ford", "Trillian", "Zaphod", "Marvin", "Slartibartfast", "Jeltz", "Random", "God", "Hotblack", "Fenchurch"]
objects    = ["Guide", "Vogon", "Gargle Blaster", "infinite improbability", "Sirius", "42", "forty-two", "krikkit", "golgafrinchan"]

def analyze(book, data):

	mentions = [0] * len(data)

	with open(book) as f:
		for line in f:
			line = line.strip()

			i = 0
			for d in data:
				mentions[i] += len([m.start() for m in re.finditer(d, line, re.IGNORECASE)])
				i += 1

	print(zip(data, mentions))

for i in range(1,6):
	analyze("guide"+str(i)+".txt", objects)