primelist = []
for possibleCandidate in range(2,21):
	isPrime = true
	for nump in range(2,possibleCandidate):
		if (possibleCandidate%nump ==0):
			isPrime = false
		if isPrime:
			primelist.append(possibleCandidate)
for a in primelist:
	print(a)