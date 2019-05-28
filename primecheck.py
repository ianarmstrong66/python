primelist = []
for possibleCandidate in range(2,21):
	isPrime = True
	for nump in range(2,possibleCandidate):
		if (possibleCandidate%nump ==0):
			isPrime = False
	if isPrime:
			primelist.append(possibleCandidate)
for a in primelist:
	print(a)