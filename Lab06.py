class Player:
    def __init__(self,firstname,lastname,team=None):
        self.first_name = firstname
        self.last_name = lastname
        self.scores = []
        self.team = team

def add_score(self,score):
    self.scores.append(score)

firstname=raw_input('enter firstname:')
lastname=raw_input('enter lastname:')
team=raw_input('enter team if any:')
