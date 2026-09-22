
# functions _can_ use variables that are declared in their enclosing scope
# (for now, that means global variables)
# however, this is generally a Bad Idea, because it makes the functions less portable
# this is because rather than depending just on their parameters, 
# they depend on other stuff in a way that is less obvious


# for instance, you can do this -- technically (that is, there's 
# nothing that will _stop_ you from writing this code)
# but it's a pretty bad way to do it
x = 5
y = 8
z = 36

def convert_to_mins():
    hours_in_day = 24
    mins_in_hour = 60
    
    total_hours = x + (y * hours_in_day)
    total_mins = z + (total_hours * mins_in_hour)
    
    return total_mins


# when solving a complicated problem, it's often useful to figure out _how_
# to solve it before we write any of the actual code.  This way, we can make
# sure that the high-level approach seems basically workable, before we spend
# a while implementing one step, and then realise later on that we've hit an impass.


# One way to do this is to create _stubs_ of our functions
# before we actually add their implementation

# a function stub is just the `def` line, with a single expression as the 
# body so that we don't get syntax errors

# personally, I prefer to have function stubs error out rather than running,
# and doing something potentially nonsensical.  We'll learn more about
# errors & exceptions later on, but this `raise NotImplementedError` is a 
# brief look ahead.  If you prefer to have just a `return -1` instead, 
# that's also tolerable

def stddev(nums):
    raise NotImplementedError
    
def mean(nums):
    raise NotImplementedError
    
    
stddev([1,2,3])
    
    
# it's possible for a function return multiple values*, just like it's 
# possible for a function to have multiple parameters and thus
# take multiple arguments

# we saw this before, in our card game activity

def divide_into_suits(cards):
    
    d = list()
    c = list()
    h = list()
    s = list()
    
    for card in cards:
        suit = card[1]
        if suit == "diamonds":
            d.append(card)
        elif suit == "clubs":
            c.append(card)
        elif suit == "hearts":
            h.append(card)
        else:
            s.append(card)
        
    # we return all four different lists here
    # *technically, this is squishing all of the 
    # lists into a single _tuple_, and returning that
    # but it's the same result as returning multiple
    # values, so call it what you prefer
    return d, c, h, s





# one _really_ cool feature that Python supports (and I wish Java supported!)
# is _default arguments_ and _keyword arguments_

# let's consider our convert_to_mins function from before

def convert_to_mins(days, hours, mins):
    """
    Calculates the total number of minutes elapsed,
    given a number of minutes, hours, and days
    Parameters
    -------
    days : int
         Number of complete days elapsed
    hours : int
        Number of hours elapsed, past the last day
    mins : int
        Number of mins elapsed, past the last hour

    Returns
    -------
        int: Total number of minutes
    """
    hours_in_day = 24
    mins_in_hour = 60
    
    total_hours = hours + (days * hours_in_day)
    total_mins = mins + (total_hours * mins_in_hour)
    
    return total_mins

# If I want to calculate the total number of minutes in a week
# it seems like this function will do it, right?  or the total number
# of minutes in 7 hours and 36 minutes
# I can make such a call easily enough
convert_to_mins(7, 0, 0) # hours in week

# At the same time, passing in a bunch of 0s to a function to say "nahhh"
# is pretty annoying
# this is solved with _default arguments_

def convert_to_mins(days=0, hours=0, mins=0):
    """
    Calculates the total number of minutes elapsed,
    given a number of minutes, hours, and days
    Parameters
    -------
    days : int (0)
         Number of complete days elapsed
    hours : int (0)
        Number of hours elapsed, past the last day
    mins : int (0)
        Number of mins elapsed, past the last hour

    Returns
    -------
        int: Total number of minutes
    """
    hours_in_day = 24
    mins_in_hour = 60
    
    total_hours = hours + (days * hours_in_day)
    total_mins = mins + (total_hours * mins_in_hour)
    
    return total_mins

# here, we've said that the _default_ value for each of the parameters is zero
# so if no argument is passed, we use the _default argument value_

# now, we can get the "minutes in a week" done very easily
mins_week = convert_to_mins(7)

# you might wonder, "What if I want the number of mins 
# in 6 hours?  How do I do that?"
# clearly, this can't do it, because even though _we_ want the 6 to be hours
# not days, the computer can't discern this from our call above

mins_six_hours = convert_to_mins(6)

# better
# here, we specify _which_ argument we're trying to pass
# and the others use their default values
mins_six_hours = convert_to_mins(hours=6)

# we can use keyword args to pass arguments in whatever order we want, too
conv_res = convert_to_mins(mins=5, hours=22, days=4)


# Python also supports letting functions take in an _arbitrary number of arguments_
def make_table_reservation(name, *args):
    """ 
    Reserves a table at a restaurant.  At least one name is required, 
    but multiple names can be added.  The restaurant will put out 
    a custom placemat for each person on the reservation
    
    """
    print (f"Reservation for {name}", end = "") # this is another example of named arguments
    if len(args) == 0: print()
    else: 
        print(", ", end="")
        for addl in args:
            print(f"{addl}, ", end="")
        print()
        

make_table_reservation("Bobby")

make_table_reservation("Nancy", "Jimmy", "Sally", "Katherine", "Henry", "Johann")

