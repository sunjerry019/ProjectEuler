"""
Project Euler Problem 4
Largest palindrome product

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

"""

def checkpalin(num):
	s = str(num)
	ls = len(s)

	first = s[:ls//2]

	if ls%2 == 0:
		second = s[ls//2:][::-1]
	else:
		# ls -= 1
		second = s[ls//2 + 1:][::-1]

	palin = True
	for i in range(ls//2):
		if first[i] != second[i]:
			palin = False
			break
	return palin

def main():
	arrOfPalins = []
	for i in range(100, 1000):
		for j in range(i,1000):
			prod = i*j
			if checkpalin(prod):
				arrOfPalins.append(prod)
				print("{} * {} = {}".format(i, j, prod))
	print("Max is {}". format(max(arrOfPalins)))
main()
