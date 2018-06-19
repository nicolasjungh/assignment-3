input1 = input("Geben Sie hier bitte die DNA-Sequenz ein:" )
input2 = input("Geben Sie bitte hier das Pattern ein:")

dna= input1
pattern = input2

def hammingDistance(a, b):
	hammer = 0
	for x, y in zip(a, b):
		if x != y:
			ham += 1
	return hammer

def distanceBetweenPatternAndString(pattern, dna):
	c = len(pattern)
	Abstand = 0
	for x in dna:
		Abstand = c+1
		for i in range(len(x) - c + 1):
			z = hammingDistance(pattern, x[i:i+c])
			if Abstand > z:
				Abstand = z
		distance = Abstand + 1
	return distance

print(distanceBetweenPatternAndString(pattern, dna))
