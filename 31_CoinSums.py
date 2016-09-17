"""
Project Euler Problem 31
Coin Sums

In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:

    1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).

It is possible to make £2 in the following way:

    1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p

How many different ways can £2 be made using any number of coins?

"""

import copy

def extend(dic, dic2):
	for key, value in dic2.items():
		if key in dic:
			dic[key] += value
		else:
			dic[key] = value
	return dic

# this function is copied, removes duplicates in a list
def removeDup(l):
	try:
		seen = set()
		new_l = []
		for d in l:
			t = tuple(d.items())
			if t not in seen:
				seen.add(t)
				new_l.append(d)

		return new_l
	except:
		return l

def main():
	denominations = [1, 2, 5, 10, 20, 50, 100, 200]
	dp = [[]] * 201 

	#print(dp)

	for i in denominations:
		dp[i] = copy.deepcopy(dp[i] + [{i:1}])
		#dp[i] = [y for y in itertools.chain(dp[i], [{i:1}])]
		#print(dp)

		for j in range(1, 201):
			#print("At denomination", i, "At value", j)
			#if j % i == 0 and j != i:
			#	tempobj = removeDup([extend(way, {i: 1}) for way in dp[j - i]])
			#	dp[j] = dp[j] + tempobj
		
			if len(dp[j]) != 0 and (j+i <= 200):
				kek = copy.deepcopy(dp[j])
				tempobj = copy.deepcopy(removeDup([extend(way, {i: 1}) for way in kek]))
				dp[j + i] = copy.deepcopy(dp[j + i] + tempobj)
				
	#print(len(dp[200]))
	print(len(removeDup(dp[200])))
main()