
# setup -- build ourselves a deck of cards, shuffle it, and remove one

import random

cards = list()

# build the deck
for suit in ["diamonds", "clubs", "hearts", "spades"]:
    for rank in list(range(2,10)) + ["A", "J", "Q", "K"]:
        cards.append((rank, suit)) # generate a card, f.ex ("A", "Clubs") for "Ace of Clubs"
        
        
random.shuffle(cards)

removed = cards[0] # this is the card we are removing from the deck
print("We have removed " + str(removed))
 
rest = cards[1:] # this is what is left

# now, we'll "teach" the computer how to perform some actions we need


# tell the computer _how_ to split up the deck of the cards into "stacks" for each of the suits
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
        
    return d, c, h, s


# actually split up the deck into the piles
diamonds, clubs, hearts, spades = divide_into_suits(rest)


# teach the computer another skill.
# given several stacks of cards, figure out which stack is missing a card (it'll be the one w. the wrong length)
def find_missing_suit(suits):
    for suit in suits:
        if len(suit) != 12:
            return suit

# then, figure out which pile has the missing card
suit_with_missing = find_missing_suit([diamonds, clubs, hearts, spades])


# the last thing we want to teach the computer
# once we have just one stack to look through, figure out which card isn't there
def find_missing_card(stack_of_cards):
    ranks_should_have = list(range(2,10)) + ["A", "J", "Q", "K"]
    this_suit = stack_of_cards[0][1]
    ranks_do_have = [card[0] for card in stack_of_cards]
    
    for card_rank in ranks_should_have:
        if card_rank not in ranks_do_have:
            return (card_rank, this_suit)
        
    raise ValueError("Couldn't find the missing card....something bad"
                     " has happened along the way")



# and finally, figure out which card is missing from that file        
missing_card = find_missing_card(suit_with_missing)


# report our results
print("We found " + str(missing_card) + " as the missing card")


    
