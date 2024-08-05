
class Player(object):
    
    def __init__(self, cards=[], name=''):
        self.cards = cards
        self.name  = name


class Game(object):

    """
    The "Snap!" matching condition can be:
        1. the face value of the card,
        2. the suit,
        3. or both.
    """

    def same_suit(c1, c2):
        return c1['suit'] == c2['suit']
    
    def same_value(c1, c2):
        return c1['value'] == c2['value']

    def same_or_condition(c1, c2):
        return c1['value'] == c2['value'] or c1['suit'] == c2['suit']

    criteria = {
        1: same_suit,
        2: same_value,
        3: same_or_condition
    }

    def __init__(self, N, C):
        self.number_packs = int(N)
        self.condition    = self.Criteria[int(C)]
        self.p1           = Player(name='Foo')
        self.p2           = Player(name='Bar')
        self.pile         = []




""""
The program should ask:
 
* How many packs to use (i.e. define N)
* Which of the three matching Criteria to use
"""
if __name__ == '__main__':

    pack_to_use = ['1','2','3','4']
    matching_Criteria = ['1','2','3']

    while True:
        N = input('Packs of cards to use? (choose from 1/2/3/4)\n')
        C = input('Which of the three matching Criteria to use?')
        
        if N not in pack_to_use or C not in matching_Criteria:
            print ("Invalid choice!")
        else:
            break
    
    game = Game(N, C)
    game.play()