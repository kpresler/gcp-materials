# -*- coding: utf-8 -*-
"""
Created on Mon Jul 14 09:28:30 2025

@author: Kai
"""


# early on in the semester we learned how to use `input()`
# input displays a _prompt_ to the user, telling them _what to input_
# it then _returns_ everything they enter, before hitting the 'Enter' key
# as a string.  we can then take this string, pull it apart, coerce it into
# an int, etc

# this works fine for writing a program that needs to deal with a small amount
# of input, or one where we want to respond to precisely what a user is telling
# us, as they run the program.  This is not, however, a reasonable solution
# if we want to write a program that's going to process a _lot_ of data
# if we make the user type in everything every time the program is run, they
# will be, (a) annoyed, and (b) have ample opportunities to make mistakes


# a much better solution is to read data from _files_
# a file can be anything we want -- a bunch of text of a book
# a CSV file (https://en.wikipedia.org/wiki/Comma-separated_values) or other
# formats.  so long as we know the _name_ of that file, we can open it up, 
# slurp up its contents, and then our program can do with it what we want


# to open up a file, we use the open() function
# this returns a file object
# we can then iterate over this object, call methods on it, etc
shopping_list = open("shopping.txt")


# files are iterable, just like lists, so a `for thing in file` loop
# is the easiest solution for accessing every line in it
print("~~~~ My Shopping List ~~~~")
for line in shopping_list:
    # we add the end="" because each line in the file 
    print(line, end="") # is already terminated with a newline
    
   
    
# this resets us to the beginning of the file so I can show you
# some other stuff with it
shopping_list.seek(0)


# if I want all of the lines of the file in a collection, I can 
# do that pretty easily too.  this returns a list of all lines
file_lines = shopping_list.readlines()



# back to the beginning
shopping_list.seek(0)


# If I want all of my text in _a_ string, I can do that too
# this does keep track of the linebreaks in the file (each one is 
# preserved as a \n within the string) so you don't lose that information
# but lets you do analysis across the _entire_ text, if that's what you want
full_list = shopping_list.read()


# If you've got a CSV file, which is what I created above, a common approach
# is to _split_ it up on the commas so you can access parts of each line
# for instance, let's imagine that from my shopping list above, I want
# to figure out the _total amount_ that I spent on groceries.  since each
# line contains an item, a quantity of that item, and a price per unit,
# this is a pretty easy calculation to perform, _if_ I can get at the data


total_cost = 0
for item in file_lines:
    
    # we have chunks separated with commas, so split on that
    line_components =  item.split(",")
    
    
    item, amt, unit_price = line_components[0],\
        int(line_components[1]),\
        float(line_components[2])
    
    cost_of_this_item = int(amt) * float(unit_price)
    
    total_cost += cost_of_this_item
    
    # we can print data while we're at it
    
    print(f"{amt} {item} (${unit_price} each)")
    
# and our total amount
print(f"Total amount spent: ${total_cost}")

# this relinquishes the file so that another program can use it
shopping_list.close()

# let's see another thing we can do here

# I have a file that contains a couple paragraphs of Sherlock Holmes.  Let's 
# see how many times each word shows up


sherlock = open("mr_holmes.txt")

full_text = sherlock.read()

# a dictionary is a splendid choice for associating arbitrary keys (words)
# w. their counts (ints)
words_counts = {}
for word in full_text.split():
    if word in words_counts:
        words_counts[word] += 1
    else:
        words_counts[word] = 1


for word, count in words_counts.items():
    print(f"`{word}` appeared {count} times")
    
 
    
# we could improve upon the above a bit by stripping out extra punctuation
# at the ends of words, for handling words case-agnostic (if that's what we want)    
# or other such approaches, but this shows to a first approximation what we can do




# other things we can do -- just like we can _read_ from files, we can also
# _write_ to files

# when you're writing a file, it is _really important_ to make sure you 
# _close_ the file (in general, closing is important, but it's particularly
# important here, because contents _might_ be buffered until a file is closed
# and nothing else can access a file while it's open for writing)

# to do so, we use a `with` block:

def write_primes_file(filename, limit):
    
    # ***NOTE***: When you open up a file in _write_ mode,
    # all of the contents are _destroyed_
    
    # You can open it up in _append_ mode to preserve existing contents
    # & let you add new ones
    
    with open (filename, "w") as my_file:
        primes_list = primes_up_to(limit)
        
        for idx, prime in enumerate(primes_list):
            my_file.write(str(prime) + " ")
            
            if (idx and idx % 10 == 0): my_file.write("\n")
    
    # the file gets closed automagically at this point -- very nice!
        
        
# helper functions        
def is_prime(num):
    
    if num == 1:
        return False
    if num == 2:
        return True
    
    for possible_factor in range(2, num):
        if (num % possible_factor) == 0:
            return False
    
    return True


def primes_up_to(n):
    res = list()
    for num in range(1, n + 1):
        if (is_prime(num)):
            res.append(num)
    
    return res
            

write_primes_file("primes.txt", 10000)
