"""
Project Euler Problem 3
Largest Prime Factor

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

"""
def isprime(n):
    # Returns True if n is prime.
    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False

    i = 5
    w = 2

    while i * i <= n:
        if n % i == 0:
            return False

        i += w
        w = 6 - w

    return True
"""

import sympy.ntheory.factor_ as snf

def main():
	x = 600851475143
	print(max(snf.factorint(x)))

main()