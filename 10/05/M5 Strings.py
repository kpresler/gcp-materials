# if we've got a string, we can _extract_ characters out of it using []
#             0123456
this_class = "EN.500.113 Gateway Computing: Python"

print(this_class[0]) # 0th character (E)
print(this_class[1]) # 1st character (N)
print(this_class[2]) # 2nd character (.)
print(this_class[3]) # 3rd character (5)
# ....and so on and so forth

# notice how strings (and lists, and tuples, and other "things")
# are zero-indexed.  so, the "first" element is at index 0, not 1

# we can also index into a string from the right side

print(this_class[-1]) # last character (n)
print(this_class[-2]) # second-to-last character (o)
print(this_class[-3]) # third-to-last character (h)

# you might be wondering...in addition to using [] to access characters out of a string
# can we also _change_ the string like so?

# nope!
# TypeError: 'str' object does not support item assignment
this_class[3] = "6"

# Strings in Python, like in _most_ other languages are _immutable_
# that is, you can't change a string to be a different string
# you can generate _new_ strings (that's what the concatenation, repetition etc)
# does, but it's a _new_ string, not changing the original object
# when we learn about lists (next module!) we'll see how they
# are our first _mutable_ datatype


# in addition to extracting single characters out of strings
# we can also _slice_ strings to extract multiple characters


this_class[0]

class_prefix = this_class[0:2] # grabs characters 0 & 1 (EN)
class_dept = this_class[3:6] # grabs characters 3, 4, 5 (500)
class_num = this_class[7:10] # grabs characters 7, 8, 9 (113)
class_name = this_class[11:] # grabs characters from 11 to the end



# note something pretty important about what we've got above
# when you're slicing a string, the _start index_ is inclusive
# and the end index is _exclusive_

# so this_class[0:2] is from 0, inclusive, up to, but not including, 2
# this is nice because it means you can take consecutive 
# slices of a string and you get no overlap/repetition
# in our case, we are deliberately _not_ taking consecutive
# slices, since we want to drop the `.`s and ` `, but YMMV

# notice something else about slicing
# either (and in fact, both) indices are optional
# we had
class_name = this_class[11:]

# if you don't have an end index, it says to go all the way to
# the end of the string

# if you don't have a start index, it says "start at the beginning"

class_prefix = this_class[:2] # this is a fine way to extract characters 0 & 1


# let's learn about some string _methods_ that we can use to 
# generate transformations of strings 

original = "Hello World!"

# WANT TO SOUND REALLY EXCITED?
# HOW ABOUT YELLING ALL THE TIME?
print(original.upper()) # prints HELLO WORLD!

# maybe you're tired of being yelled at now
# can't blame you
print(original.lower()) # prints hello world!

new_str = "this is all lowercase"

# the capitalize method will capitalise
# the first letter of the string
print(new_str.capitalize()) # prints This is all lowercase

# the title method will capitalise the first 
# letter of each word in the string
print(new_str.title()) # prints This Is All Lowercase


# WARNING: COMMON BUG! #
# this capitalises the string and then
# immediately throws it in the trash
new_str.upper()


# You almost always want to do something like this instead
# this puts the capitalised version back into a varible 
# so we can use it later
new_str = new_str.upper()



# we saw previously that you can loop through all of the characters in a string

our_loc = "Baltimore Maryland"
for char in our_loc:
    print(char)

# what if we want words, but not chars?

our_loc_words = our_loc.split()

# this _splits_ the string into a list (soon!) of strings
# the default split character is a space, so we get the list
# ["Baltimore", "Maryland"]

# thus

for word in our_loc_words:
    print(word)

# suppose we've got a strangly formatted string
odd = "this.string.is.written.really.oddly.because.maybe.my.spacebar.is.broken"

words = odd.split(".")

# ahhh, much better :)
for word in words:
    print(word)
    
    
# we can also do the reverse -- convert a list of strings
# into a single string by _joining_ them together

# join all of the words from our list together, using a space (" ")
# as the separator character between each element
reassembled = " ".join(words)

# we can use whatever we want as the joining character, however

# let's image our assembly instructions came from IKEA, so we've 
# got bits of Swedish stuck throughout what we're making
oddly_assembled = "åö".join(words)

# oddly_assembled = thisåöstringåöisåöwrittenåöreallyåöoddlyåöbecauseåömaybeåömyåöspacebaråöisåöbroken
# lovely (?)
