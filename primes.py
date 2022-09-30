"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    if number_of_primes <= 0:
        raise ValueError(f"{number_of_primes}should be greater than 0")
    list = []
    num = 2
    count = 0
    while count < number_of_primes:
        if is_prime(num):
            list.append(num)
            count += 1
            num +=1
        else:
            num +=1
    return list


def is_prime(n):
    for i in range(2,n):
        if (n%i) == 0:
            return False
    return True
