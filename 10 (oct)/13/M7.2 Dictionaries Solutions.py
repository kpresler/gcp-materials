# -*- coding: utf-8 -*-
"""
Created on Mon Oct 13 11:31:54 2025

@author: Kai
"""

def word_counts(word_list):
    
    counts = dict()
    
    for word in word_list:
        
        if word in counts:
            counts[word] += 1
        
        else:
            counts[word] = 1
        
        #counts[word] = word_list.count(word)
        
    return counts

words = ["Apple", "Banana", "Plum", "Apple", "Banana", "Apple"]

print(word_counts(words))


items = {
    "bananas": (.17, 25),
    "eggs": (.12, 100),
    "frozen pizzas": (4.5, 4)
}


def greatest_expense(items):
    
    total_amount = 0
    
    greatest_cost = 0
    greatest_item = None
    
    
    for item, costs in items.items():
        
        # item is the thing (string)
        # costs is the num, cost of each (tuple<float, int>)
        
        cost_of_this, num_of_this = costs
        
        total_cost_of_this = cost_of_this * num_of_this
        
        if total_cost_of_this > greatest_cost:
            greatest_cost = total_cost_of_this
            greatest_item = item
        
        total_amount += total_cost_of_this
            
    perc = 100 * greatest_cost / total_amount
    
    print(f"The greatest expense came from {greatest_item}, which accounted for {perc} of the total amount spent.")
        
greatest_expense(items)


def invert_dict(orig_dict):
    
    out = dict()
    
    for key, value in orig_dict.items():
        
        # mapping isn't there -- add it
        if value not in out:
            out[value] = key
            
        # mapping is there, and is a list already.  add to the list
        elif type(out[value]) == list:
            out[value].append(key)
    
        # mapping is there, but still as a scalar.  have to make a list
        else:
            out[value] = [out[value], key]
            
    return out

res = invert_dict({"a":10, "b": 10, "c": 25})

print(res)
