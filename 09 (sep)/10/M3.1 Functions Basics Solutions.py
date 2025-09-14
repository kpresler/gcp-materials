def cube_num(num):
    return num **3    # could also break this out into another variable, if you were so inclined



def is_even(num):
    return num % 2 == 0


# or, if you prefer branching:
def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False
    
    
def squadratic_roots(a, b, c):
    
    rad = (b**2 - 4 * a * c) ** .5
    
    pos_root = (-b + rad) / 2 * a
    neg_root = (-b - rad) / 2 * a
    
    return pos_root, neg_root