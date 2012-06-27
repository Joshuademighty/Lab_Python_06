class Player:
    def __init__(self,firstname,lastname,team=None):
        self.first_name = firstname
        self.last_name = lastname
        self.scores = []
        self.team = team

    def add_score(self,score):
            self.scores.append(score)
            print  self.scores
            

    def __str__(self):
        describ=self.first_name+' '+self.last_name+' '+'is a player of'+' '+self.team
        return describ
    def __repr__(self):
        playee=self.first_name+' '+self.last_name
        return playee
    
    def total_score(self):
        total=sum(self.scores)
        print total

    def average_score(self):
        avg=(sum(self.scores))/2
        print avg



#firstname=raw_input('enter firstname:')
#lastname=raw_input('enter lastname:')
#team=raw_input('enter team if any:')

#torres=Player(firstname,lastname,team)
#print torres

#num=input('enter number of scores:')
#print'***************************************************************'
#n=0
#while n<num:
 #   score=input('enter the score:')
  #  if score>=0:
   #     print torres.add_score(score)
    #n+=1

#print'*************************************************************'
#print'the total is :',torres.total_score()
#print'**************************************************************'
#print'the average is :',torres.average_score()

#print'*************************************************************************'




class Team:
    portugal='portugal'
    spain='spain'
    def __init__(self,name,league,manager_name,points,players=None):
        self.name=name
        self.league=league
        self.manager_name=manager_name
        self.points=[]
        self.players=[]
        
    def add_player(self,player):
        self.players.append(player)
        return self.players

    def __str__(self):
        des=self.name+' '+'plays in the'+' '+self.league+' '+'league'+' '+'and is managed by'+\
        ' '+self.manager_name
        return des
 


name=raw_input('Enter team name:')
league=raw_input('Enter league name:')
manager_name=raw_input('Enter manager\'s name:')
points=input('Enter team\'s points:')
players=raw_input('enter player name:')

boyteam=Team(name,league,manager_name,points)
print boyteam
firstname=raw_input('enter:')
lastname=raw_input('enter:')
player=Player(firstname,lastname)
#print boyteam.add_player(player)
manteam=boyteam.spain
print manteam
torres=boyteam.add_player(player)
print torres



class Match:
    def __init__(home_team,away,date,home_scores,away_scores)
    self.home=home_team
    self.away=away_team
    self.date=date
    self.hscores={}
    self.ascores={}



home=raw_input('enter home team:')
away=raw_input('enter away team:')
yr=int(raw_input("Enter Year: "))
mon=int(raw_input("Enter Month: "))
day=int(raw_input("Enter Day: "))
date=datetime.date(yr,mon,day)   




















