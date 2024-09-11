#The Western Suburbs Croquet Club has two categories of membership, Senior and Open. 
# They would like your help with an application form that will tell prospective members which category they will be placed.
#To be a senior, a member must be at least 55 years old and have a handicap greater than 7. 
# In this croquet club, handicaps range from -2 to +26; the better the player the lower the handicap.

def open_or_senior(data):
    lst = []
    for i in range(len(data)):      
        if data[i][0] >= 55 and data[i][1] > 7:
            lst.append('Senior')
        else:
            lst.append('Open')
    return lst