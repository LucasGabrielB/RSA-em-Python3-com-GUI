# Author: Lucas Gabriel

from random import randint
from math import floor, sqrt

def is_prime(n):
	''' return "True" if "n" is a prime number else return "False" '''
	if n % 2 == 0:
		return False
	
	max_divisor = floor(sqrt(n))
	
	for d in range(3, max_divisor + 1, 2):
		if n % d == 0:
			return False
	
	return True


def generate_random_prime(limite: int):
	''' return a random prime number from 3 up to the "limite" '''

	is_a_prime_number = False

	while is_a_prime_number == False:

		number = randint(3, limite) # returns a random number between 3 and "limite"
		is_a_prime_number = is_prime(number) # verify if is a prime number

	return number


def modular_inverse(a, m):
	''' returns the modular inverse of "a" and "b" '''
	a = a % m 

	for x in range(1, m): 
		if ((a * x) % m == 1): 
			return x 

	return 1


def mdc(x, y):
	''' returns the greatest common divisor of two numbers, "x" and "y" '''
	while(y): 
		x, y = y, x % y 

	return x


def generate_new_keys():
	''' generate a RSA keypar and save then in they respective files '''

	# choose two distinct prime numbers p and q
	p = generate_random_prime(500)
	q = generate_random_prime(500)

	# compute n = pq
	n = p * q

	# compute M, where M is carmichael's totient function
	m = (p-1) * (q-1)

	# choose an integer e such that, [1 > E > M], that is, E and M are coprime
	e = 3
	while mdc(m, e) > 1:
		e += 2

	# determine D, D is the modular multiplicative inverse of E modulo M
	d = modular_inverse(e, m)

	# save private key in a file
	with open('chave_privada.pem', 'w') as arquivo:
		arquivo.write(f'{d} {n}')

	# save public key in a file
	with open('chave_publica.pem', 'w') as arquivo:
		arquivo.write(f'{e} {n}')
