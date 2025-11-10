# -*- coding: utf-8 -*-
"""
Created on Mon Jul 21 14:00:10 2025

@author: Kai
"""

# Exceptions Tasks Solutions

# Task 1

def squareInteger():
    
    good_input = False
    
    while not good_input:
        
        inp = input("Please enter a positive integer: ")
            
        try:
            num = int(inp)
        except ValueError:
            print("Not an int, try again")
            continue
        
        if num < 0:
            print("Not a positive int, try again")
            
        else:
            print(f"Your squared number is {num**2}")
            good_input = True
            
    
        
squareInteger()

# Task 2

def combine_lists(list1, list2):
    
    
    res = dict()
    

    try :  
        for idx in range( max (len(list1), len(list2))):
                           
            key = list1[idx]
            value = list2[idx]
            
            if key in res:
                raise KeyError("Duplicate key in list")
            
            res[key] = value
    
    except IndexError:
        print("Invalid index, lists not the same length?")
    except KeyError as e:
        print(e)
            
    return res

lst1 = ['a', 'b', 'a']
lst2 = [1, 2, 3]

print(combine_lists(lst1, lst2))


# Debugging Tasks Solutions

# Task 1


def lucas(n):
    """
    Returns Lucas sequence of length n.
    A Lucas sequence starts with the values 2 and 1.
    Subsequent values are found by summing the two previous values
    
    https://en.wikipedia.org/wiki/Lucas_number
    
    Parameters
    ----------
    n : int
        Length of sequence to return.

    Returns
    -------
    list
        Lucas sequence.
    """
    if n == 1:
        return [2]
    elif n > 1:
        seq = [2,1]    
        for i in range(n-2): # dropped the range, since we build part of the seq on the previous line
            seq.append(seq[-2]+seq[-1])    
        return seq # de-indented this; don't return until we have the entire seq
    else:
        return []

if __name__ == "__main__":
    print("This program prints a Lucas sequence of length n")
    n = int(input("Enter n: "))
    print(lucas(n))
    
    
# Task 2


def sieve(upper_limit):
    
    # a list for keeping track of whether each number is prime
    # each index represents a number we are primality testing
    
    # this initialises 0 & 1 to be not prime, and states
    # that all other numbers are prime, so far.  the sieve will figure out
    # which ones _actually_ are
    results = [False, False] + [True] * (upper_limit - 1)
    
    p = 2
    
    # the outer loop runs through numbers that are definitely prime
    while (p < upper_limit) and results[p]: # switched order of checks so we don't wander out-of-bounds
        
        # enumerate the multiples of `p`, and mark them as Not Prime (False)
        for num in range (2*p, upper_limit + 1, p): # need to add third parameter, and make upper_limit inclusive
            results[num] = False
        
        # go looking for the next prime number to setup the nex iteration
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

