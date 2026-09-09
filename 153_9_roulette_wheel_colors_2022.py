# Roulette Wheel 117 - 9
# MZK
# 9/23/2016

pocketNb = int(input("Please provide the pocket number: "))

# Here we filter everything that is not in the range: 0-36
if pocketNb<0 or pocketNb>36:
    print("This number is wrong.")
    print("Please input a number between 0 and 36")
else:
    if pocketNb==0:
        pocketColor="Green"

    elif pocketNb >0 and pocketNb <= 10:
        if  pocketNb%2 ==0: # The reminder of division of an even over 2 is zero
            pocketColor="Black"
        else:
            pocketColor="Red"
            
    elif pocketNb >=11 and pocketNb <=18:
        if  pocketNb%2 ==0: # even
            pocketColor="Red"
        else:
            pocketColor="Black"

    elif pocketNb >=19 and pocketNb <=28:
        if  pocketNb%2 ==0: # even
            pocketColor="Black"
        else:
            pocketColor="Red"   
    elif pocketNb >=29 and pocketNb <=36:
        if  pocketNb%2 ==0: # even
            pocketColor="Red"
        else:
            pocketColor="Black"

    print('The Pocket Color is', pocketColor)