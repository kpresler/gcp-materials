# -*- coding: utf-8 -*-
"""

Program that uses the Sieve of Eratosthenes to calculate prime numbers
up to a limit provided.

A description of the algorithm can be seen here: 
    https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes#Overview

Created on Sat Jul 19 11:13:12 2025

@author: Kai Presler-Marshall
"""



def sieve(upper_limit):
    
    # a list for keeping track of whether each number is prime
    # each index represents a number we are primality testing
    
    # this initialises 0 & 1 to be not prime, and states
    # that all other numbers are prime, so far.  the sieve will figure out
    # which ones _actually_ are
    results = [False, False] + [True] * (upper_limit - 1)
    
    p = 2
    
    # the outer loop runs through numbers that are definitely prime
    while results[p] and (p < upper_limit):
        
        # enumerate the multiples of `p`, and mark them as Not Prime (False)
        for num in range (2*p, upper_limit):
            results[num] = False
        
        # go looking for the next prime number to setup the next iteration
        # of the outer loop
        p += 1
        while p < len(results) and not results[p]: p += 1
        
    # return the list; the `True`s are the now confirmed primes, and 
    # Falses are composites
    return results






# as you're debugging, you'll probably have a better time if you don't run all
# the way up to 120, at least not at first -- find primes up to 10, or 20
# or something like that, so there's less digging to do

if __name__ == "__main__":
    print("This program uses the Sieve of Erathosthenes to find prime numbers up to n")
    n = int(input("Enter n: "))
    
    # If you want a non-trivial example, you can do primes up to 120 
    # as shown in the Wiki example
    first_primes = sieve(n)

    # loop through the list, and print out all numbers that are prime
    # (indices with a `True` in that slot)
    for idx, is_prime in enumerate(first_primes):
        if is_prime:
            print(idx)
    