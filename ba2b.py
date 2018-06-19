DNA = ["AAATTGACGCAT", "GACGACCACGTT", "CGTCAGCGCCTG", "GCTGAGCACCGG", "AGTACGGGACAG"]
k = 3
def hammingDistance(p, q):
	ham = 0
	for x, y in zip(p, q):
		if x != y:
			ham += 1
	return ham

def distanceBetweenPatternAndString(pattern, DNA):
	k = len(pattern)
	distance = 0
	for x in DNA:
		hammer = k+1
		for i in range(len(x) - k + 1):
			z = hammingDistance(pattern, x[i:i+k])
			if hammer > z:
				hammer = z
		distance += hammer
	return distance

def numberToPattern(x,k):
    if k == 1:
        return numberToSymbol (x)
    x = x // 4
    y = x % 4
    prefixPattern = numberToPattern(x, k - 1)
    return prefixPattern + numberToSymbol(y)

def numberToSymbol(x):
	if x == 0:
		return "A"
	if x == 1:
		return "C"
	if x == 2:
		return "G"
	if x == 3:
		return "T"

def bestString(DNA, k):
	distance = (k+1) * len(DNA)
	best = ""
	for i in range(4**k):
		pattern = numberToPattern(i, k)
		z = distanceBetweenPatternAndString(pattern, DNA)
		if distance > z:
			distance = z
			best = pattern
	return best

print(bestString(DNA, k))