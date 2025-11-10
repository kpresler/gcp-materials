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
        for i in range(n):
            seq.append(seq[-2]+seq[-1])    
            return seq
    else:
        return []

if __name__ == "__main__":
    print("This program prints a Lucas sequence of length n")
    n = int(input("Enter n: "))
    print(lucas(n))
    
    
