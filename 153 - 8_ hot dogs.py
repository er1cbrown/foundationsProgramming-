from math import ceil # for ceiling rounding

# we initialize our two variables
nbPersons=int(input("number of persons attending the event? "))
nbHDPerson=int(input("number of HD per person? "))

nbHDPackage=10
nbBunsPackage=8

nbNeededHD=nbHDPerson*nbPersons
nbNeededBuns=nbHDPerson*nbPersons*2 # we assume we need two buns per HD
# we calculate the required packages of bun and hd
nbReqHDPackages=ceil(nbNeededHD/nbHDPackage) # we round bc we can only buy entire packages not fractions of packages
nbReqBunPackages=ceil(nbNeededBuns/nbBunsPackage)

# we calculate the lefotover: nb purchased - nb needed
nbHDleft   = (nbReqHDPackages*10)- nbNeededHD
nbBunsLeft = (nbNeededBuns*8) - nbNeededBuns

# display
print() # empty line
print('nb needed pkg of hot dogs', nbReqHDPackages)
print('nb needed pkg bus', nbReqBunPackages)
print() # empty line
print('nb lef hot dogs', nbHDleft)
print('nb lef buns', nbReqBunPackages)
