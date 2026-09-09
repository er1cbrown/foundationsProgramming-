# 155 - 15 time calculator per seonds

from math import floor # floor rounds to the min integer for examlpe 5.9 is rounded to 5

# we initialize our variable from the user
nbTotalSeconds=int(input("Number of Seconds? "))

# in every step we need to calculate secs, mins and hours
if nbTotalSeconds<0:
    print("Negative number not acceptable")
    nbSec=-1
    nbMin=-1
    nbHour=-1
    
elif nbTotalSeconds<60:
    nbSec=nbTotalSeconds
    nbMin=0
    nbHour=0
    
elif nbTotalSeconds>=60 and nbTotalSeconds<3600:
    nbMin=floor(nbTotalSeconds/60) # we need an int
    nbSec=nbTotalSeconds-(nbMin*60) # the remainder of minutes is calculated ins seconds
    nbHour=0 # since we have less than 3600 seconds we have zero hours
else:
    nbHour=floor(nbTotalSeconds/3600) # since we have less than 3600 seconds we have zero hours
    remainderHour=nbTotalSeconds-(nbHour*3600)
    nbMin=floor(remainderHour/60) # we need an int
    nbSec=nbTotalSeconds-((nbMin*60)+(nbHour*3600))
    
print('nb hours', nbHour)
print('nb mins', nbMin)
print('nb secs', nbSec)
