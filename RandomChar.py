## random char generator
import random
## gdp classifications are
## civilization classifications are given in a planetary context
## type 1 is extreme local (is given to hunter/gathering levels
## type 2 is local (emerging transitioning from hunter/gathering)
## to larger subsitence type communities.  That is given
## by networks of villages in a tightly clustered regional localities
## type 3 is regional, clearly distinguished from type2 where
## a regional distribution is no longer clustered to locally
## less inter regional communication
## type 4 is hemispherical wide regional communication,
## that is, stronger than type 3 in that regional communication
## is loosely inter continental.
## type 5 is global.

## income classification are perecentile ranking by gdp
##  civilization types determine income distribution indexing
## this is shown civtoincome, the value relation to civilization type
## is a stratification index, that is, indicating the diversity of
## economic income relative to gdp for percentile rank.
## thus a 2 factor stratification index would have 2 percentile ranks
## usually give by say tribesman versus chief in the case of 2 factor
## gdp.

Civilization = 3
civtoincome = {1:[95,5],2:[90,5,4,1],3:[85,5,3,3,2,2],4:20,5:100}
lowerorder = ()
strat = []
for i in range(20):
    strat.append(5.0)
civtoincome[4] = strat

strat = []
for i in range(100):
    strat.append(1.0)
civtoincome[5] = strat
##chief and warrior/hunter/mixed role occupation civ type 1
##civ type 2 peasant/clergy/nobility
## civ type 3 property based classes.  For example, Roman classification gives
## 3 other unspecified classes, proletarii, equites, senatores.  


def buildCharacter(sex = None, clas = None, profession = None,
                   age = None, parent = None,
                   income = None, civilization = Civilization):
    char = {}
    if sex == None:
        ## ternary designation for now
        ## 0,1,2 male, female, neither/both
        sd = random.random()
        if sd <= .485:
            sex = 0
        elif sd > .485 and sd <= .97:
            sex = 1
        else:
            sex = 2
    if parent == None:
        pr = random.random()
    
        
