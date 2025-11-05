# -*- coding: utf-8 -*-
"""
Created on Fri Jul 18 15:31:36 2025

@author: Kai
"""


def get_best_pokemon(filename):
    
    with open(filename) as poke_file:
        
        best_name = ""
        best_stats = -1
        
        
        for pokemon_line in poke_file.readlines()[1:]:
            
            pokemon_details = pokemon_line.split(",")
            
            this_name = pokemon_details[1]
            this_stats = int(pokemon_details[5])
            
            if this_stats > best_stats:
                best_name, best_stats = this_name, this_stats
                
        return best_name, best_stats
    
    
best_pokemon = get_best_pokemon("Pokemon.csv")
print(best_pokemon)


def get_pokemon_by_type(filename, type):
    with open(filename) as poke_file:
    
        count_this_type = 0
        
        for pokemon_line in poke_file.readlines()[1:]:
            
            pokemon_details = pokemon_line.split(",")
            
            if pokemon_details[3] == type or pokemon_details[4] == type:
                count_this_type += 1
            
            
        return count_this_type
    
num_dragons = get_pokemon_by_type("Pokemon.csv", "Dragon")
print(num_dragons)