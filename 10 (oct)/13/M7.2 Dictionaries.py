# -*- coding: utf-8 -*-
"""
Created on Tue Oct  7 09:35:27 2025

@author: Kai
"""

# Now, onward to Dictionaries

# suppose we want to keep track of all states, and for each state,
# its capital.  So far, we don't _really_ know a great way to do this.
# The best approach I can think of using our knowledge so far is to store 
# each (State, Capital) as a tuple (like that) and then have a list of 'em

state_capitals = [
  ("MD", "Annapolis"),
  ("VA", "Richmond"),
  ("PA", "Harrisburg"),
  ("WV", "Charleston")    
]

# this works, but it's annoying -- answering a question like "What is the capital of PA?"
# requires me to loop through everything

# dictionaries associate _unique, immutable, keys_ with _arbitrary_ values
# so, the keys in a dictionary are like the elements in a set
# the values in a dictionary can be anything we want

state_capitals_dict = {
  "MD": "Annapolis",
  "VA": "Richmond",
  "PA": "Harrisburg",
  "WV": "Charleston"
}

# given this dictionary, what can I do with it?

# (1) Given a key, lookup the value:
md_cap = state_capitals_dict["MD"]
print(md_cap) # "Annapolis"

# (2) Given a key, change the associated value:
state_capitals_dict["MD"] = "Baltimore" # hmm

state_capitals_dict["WV"] = None

# (3) Add a new key-value pair:
state_capitals_dict["NC"] = "Raleigh"

# (4) Remove a key-value pair
# this returns the value associated
# but be careful -- if the key doesn't exist, it'll explode
state_capitals_dict.pop("WV") 


# (5) Check if a dictionary has a mapping for a key
print ("MD" in state_capitals_dict) # True
print ("TX" not in state_capitals_dict) # True

# (6) Loop through keys, values, or entries.  Let's expand on this idea

# (6a) This lets us loop through all of the _keys_ in the dictionary
# From this, we can readily see, "For what entries do we have mappings?"
for state in state_capitals_dict:
    print(state)
    # We can also use the key to lookup the associated value
    cap = state_capitals_dict[state]
    print(cap)
    print("***")    

# (6b) This lets us loop through keys and values at the same time
# note, .items() returns basically a list of tuples; so we loop through each tuple, and unpack it
for state, capital in state_capitals_dict.items():
    print(f"The capital of {state} is {capital}")
    
# (6c) This lets us loop through the values in the dictionary.  From this,
# it is not possible to go "backwards" and find the key that this value 
# was mapped to.  This is because values are not guaranteed to be unique,
# so multiple keys could have the same value.  Also, doing the lookup
# in reverse is quite inefficient, even if we wanted to get _any_
# key mapped to the value

for capital in state_capitals_dict.values():
    print(f"{capital} is the capital of an unknown state")
    
# a few final examples

# while it's not possible to have a list as the _key_ in a dictionary, it absolutely
# can be the _value_ in it

cities_by_state = {
    "MD": ["Baltimore", "Towson", "Ellicott City", "Cumberland", "Frederick"],
    "ME": ["Portland", "Brunswick", "Belgrade", "Waterville", "Mexico"],
    "CA": ["Sacramento", "San Jose", "Los Angeles", "San Francisco"],
    "PA": ["York", "Pittsburgh", "Philadelphia", "Harrisburg"]   
}

# When we've got a doubly-nested data structure like this, a doubly-nested loop
# is often involved

for state, cities in cities_by_state.items():
    print(f"{state} has cities:")
    for city in cities:
        print(f"  {city}")
        
# Sometimes, you have two dictionaries with the same keys, but different values

state_codes = {
    "MD": "Maryland",
    "NY": "New York",
    "ME": "Maine",
    "CA": "California",
    "PA": "Pennsylvania"
}

# you can then use the key in one dictionary to look up a value in another

for state, cities in cities_by_state.items():
    state_name = state_codes[state]
    print(f"{state_name} ({state}) has cities:")
    for city in cities:
        print(f"  {city}")