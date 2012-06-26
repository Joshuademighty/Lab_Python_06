"""
Lab_Python_06
Part 1
"""

"""
Whatever the datastructure you choose,
it should represent the following data:

player		| date		| score
_______________________________________
rooney		| 6/23/2012	| 2
rooney		| 6/25/2012	| 2
ronaldo		| 6/19/2012	| 0
ronaldo		| 6/20/2012	| 3
torres		| 6/21/2012	| 0
torres		| 6/21/2012	| 1
"""

## create the player_stats data structure

import datetime
num_scorers=int(raw_input("Enter the number of Goal Scorers for today: "))

player_stats={}
newtuple=()
#score_details[]

for scorers in range(0,num_scorers):
    Name=raw_input("Enter Player name: ")
    yr=int(raw_input("Enter Year: "))
    mon=int(raw_input("Enter Month: "))
    day=int(raw_input("Enter Day: "))
    #Date=(raw_input("Enter Date: "))
    NumGoals=int(raw_input("Enter number of goals scored: "))
    dateformat=datetime.date(yr, mon, day)
    if Name in player_stats:
        newlist=list(newtuple)
        newlist.append(dateformat)
        newlist.append(NumGoals)
        newlist=tuple(newlist)
        player_stats[Name].append(newlist)
        #player_stats[Name].append(NumGoals)
    else:
        #myDict[newKey] = [value]
        newlist=list(newtuple)
        newlist.append(dateformat)
        newlist.append(NumGoals)
        newlist=tuple(newlist)
        player_stats[Name]=[newlist]
    
print player_stats.items()



#used dictionaries with list;where the list of players
#can be changed by adding other players.


print player_stats[""][0][1]



## implement highest_score



## implement highest_score_for_player



## implement highest_scorer
