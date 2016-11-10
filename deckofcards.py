'''
doctest

>>> from deckofcards import *
>>> deck1 = Deck()
>>> deck1
A deck of 52 cards.
>>> deck1.card_count
52

'''

import random


class Card():
    '''
    Models every attribute of a single card; suit, rank, and value.
    '''
    # initialize the attributes of the cards. (leave value False for now..)
    def __init__(self, value=False, *args, **kwargs):
        self.rank = self.rank()  # 2 -10, J Q K A
        self.suit = self.suit()  # hearts, diamonds, etc..
        self.value = value  # TODO: make_add_value():

    def __repr__(self):
        # represents each cards in nice english; i.e. 10 of hearts
        return "{rank} of {suit}".format(rank=self.rank, suit=self.suit)

class Deck():
    '''
    Class to model an entire deck of cards.
    '''
    def __init__(self, *args, **kwargs):
        #  We now create all the cards; using a list comprehension that
        #  creates every possible combination of rank and suit.
        self.ranks = self.make_ranks()
        self.suits = self.make_suits()
        self.cards = self.make_cards(self.ranks, self.suits)
        self.card_count = self.count_cards(self.cards)

    def __repr__(self, *args, **kwargs):
        deck = "A deck of {} cards."
        return deck.format(self.card_count)

    def make_ranks(self):
        '''
        Creates all the possible ranks for the cards.
        '''
        # create a list of integers from 2 - 10
        int_nums = list(range(2, 11))
        # converts the list of integers to a list of strings
        nums = [str(num) for num in int_nums]
        # create the list of royals; list('') splits the chars to create a list of strings
        royals = list('AJQK')
        # add the two lists together
        ranks = nums + royals
        # now, return the list of ranks.
        return ranks

    def make_suits(self):
        '''
        Manually creates a list of suits.
        '''
        suits = ['hearts', 'clubs', 'spades', 'diamonds']
        return suits

    def make_cards(self, ranks, suits):
        '''
        Makes all the card instances and populates them in the Card class.
        '''
        cards = [Card(rank, suit) for rank in self.ranks for suit in self.suits]
        return cards

    def count_cards(self, cards):
        '''
        Counts the cards list.
        '''
        card_count = len(cards)
        return card_count

    def pop_card(self, i=0):
        """
        Removes and returns a card from the deck.
        i default set to pop the first card.
        """
        return self.cards.pop(i)

    def shuffle(self):
        """
        Shuffles the cards with random module
        """
        random.shuffle(self.cards)

# TODO: create value to sort cards!
#    def sort(self):
#        """
#        Sorts the cards in ascending order.
#        """
#        self.cards.sort()

    def print_deck(self):
        print('Here is your deck of {} cards: '.format(self.card_count))
        for i in self.cards:
            print(i)
