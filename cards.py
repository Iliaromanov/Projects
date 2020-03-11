from typing import Dict, List
import arcade

clubs = {'suite': 'clubs',
         'colour': 'black',
         'ace': 1, 
         'two': 2, 
         'three': 3,
         'four': 4,
         'five': 5,
         'six': 6,
         'seven': 7,
         'eight': 8,
         'nine': 9,
         'ten': 10,
         'jack': 11,
         'queen': 12,
         'king': 14
         }

spades = {'suite': 'spades',
          'colour': 'black',
          'ace': 1, 
          'two': 2, 
          'three': 3,
          'four': 4,
          'five': 5,
          'six': 6,
          'seven': 7,
          'eight': 8,
          'nine': 9,
          'ten': 10,
          'jack': 11,
          'queen': 12,
          'king': 14
         }

diamonds = {'suite': 'diamonds',
            'colour': 'red',
            'ace': 1, 
            'two': 2, 
            'three': 3,
            'four': 4,
            'five': 5,
            'six': 6,
            'seven': 7,
            'eight': 8,
            'nine': 9,
            'ten': 10,
            'jack': 11,
            'queen': 12,
            'king': 14
            }

hearts = {'suite': 'hearts',
          'colour': 'red',
          'ace': 1, 
          'two': 2, 
          'three': 3,
          'four': 4,
          'five': 5,
          'six': 6,
          'seven': 7,
          'eight': 8,
          'nine': 9,
          'ten': 10,
          'jack': 11,
          'queen': 12,
          'king': 14
         }

cards = [clubs, spades, diamonds, hearts]


class card_properties():
  def __init__(self, cards):
    self.cards = cards


  def card(self, cards: List[Dict], suite: str, name: str) -> Dict:
    card = {}

    card['suite'] = suite

    for _ in cards: 
      if _ == suite:     
        card['colour'] = suite['colour']
        card['value'] = suite[name]
    
    return card



class solataire_actions():
  def __init__(self, cards):
    self.cards = cards


  def check_if_stack(self, card: Dict) -> bool:
    '''Checks if cards can stack
    
    '''

def card(cards: List[Dict], suite: str, name: str) -> Dict:
    card = {}

    card['suite'] = suite['suite']

    for _ in cards:      
        card['colour'] = suite['colour']
        card['value'] = suite[name]
    
    return card
    

print(card(cards, clubs, 'jack'))
