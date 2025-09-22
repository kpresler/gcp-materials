# -*- coding: utf-8 -*-
"""
Created on Mon Sep 22 11:26:22 2025

@author: Kai
"""



def is_prime(num):
    """
    Checks the primality of a single number, returning true or false accordingly.

    Parameters
    ----------
    num : int
        The number to check the primality of.

    Returns
    -------
    bool
        True if `num` was prime, `False` otherwise.

    """
    
    for potential_factor in range(2, num):
        
        # if the number divies evenly by anything less than it, not prime
        if num % potential_factor == 0:
            return False
        
    # if it divided evenly by nothing, then it is prime
    return True


def primes_up_to(num):
    """
    Finds all prime numbers up to and including the argument provided.  Each number is printed out to the console.
    
    NOTE: This uses trial division and is extremely inefficient.  `num` should not be too large.

    Parameters
    ----------
    num : int
        The upper bound for chekcing prime numbers.

    Returns
    -------
    None.

    """
    
    # 0 & 1 aren't prime, so we start range at 2
    # also, the +1 to make the end num inclusive
    
    for i in range (2, num + 1):
        if (is_prime(i)):
            print(i)
    
    

def first_n_primes(n):
    """
    

    Parameters
    ----------
    n : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """

    num = 2
    count = 0
    
    while count < n:
        
        if is_prime(num):
            print(num)
            count += 1
            
        num += 1
        
if __name__ == "__main__":
    
    choice = input("Please choose from one of the following options:\n"
                   "Test primarilty of a (s)ingle number, find (a)ll primes up to a target, or find (f)irst n primes")
    
    if choice == "s":
        num = int (input("What number? "))
        print(is_prime(num))
        
    elif choice == "a":
        num = int (input("What target? "))
        primes_up_to(num)

    elif choice == "f":
        num = int (input("How many? "))
        first_n_primes(num)