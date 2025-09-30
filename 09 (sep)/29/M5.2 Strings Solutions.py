# -*- coding: utf-8 -*-
"""
Created on Mon Sep 29 11:31:35 2025

@author: Kai
"""

def find_emails(text):
    
    words = text.split()
    
    for word in words:
        
        if "@" in word and "." in word:
            print(word)
           
sample_string = "Contact us at info@example.com or support@company.com for assistance."
find_emails(sample_string)



# Task 2

#(a)
first = "Cave"
last = "Johnson"

print(f"{first:<10}{last:>20}")


#(b)

print(f"{'~~!!~~':^10}")


#(c)
frac = 17/6

print(f"{frac:.3f}")

#(d)
num = 37
print(f"{num:b}")



# Task 3

def find_and_replace_advanced(text, old_word, new_word, case_insensitive=True, word_boundary=True):
       
    text_split = text.split()
    
    
    for i in range(len(text_split)):
    
        
    
        if case_insensitive and not word_boundary and (old_word.lower() in text_split[i].lower()):
            
            
            text_split[i] = (text_split[i].lower()).replace(old_word,new_word)
            
        
        elif case_insensitive and word_boundary and (removePunctuations(text_split[i].lower()) == old_word.lower()):
             
            
            text_split[i] = (text_split[i].lower()).replace(old_word,new_word)
            
            
        elif not case_insensitive and not word_boundary and (old_word in text_split[i]):
            
            text_split[i] = new_word
                
        elif not case_insensitive and word_boundary and (removePunctuations(text_split[i]) == old_word):
                
            text_split[i] = text_split[i].replace(old_word,new_word)
                    
                    
        
        
    result = ' '.join(text_split)
                    
    return result

            
                             
def removePunctuations(text): 

    
    clean_text = ''
    punctutations = '?!.,;:"\''
    
    for character in text:
        
        if character not in punctutations:
            
            clean_text += character
            
    return clean_text