
# Deck of Cards.

doctest will automatically test to see if the deck of cards has 52 cards and
is printing correctly.

to use:

**To make a deck**

*in terminal:*
   
    $~ python3
    >>> from deckofcards import *
    >>> deck = Deck()
    >>> deck
    A deck of 52 cards.
    >>> deck.print_deck()
    ...

(.print_deck() returns the entire list of cards.)


**Shuffle your deck**

    >>> deck.shuffle()

**Pop a card off the deck (without removing it)**
    
    >>> deck.pop_card()

# DeckofCards
