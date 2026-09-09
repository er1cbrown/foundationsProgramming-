# converting arabic into roman numbers

araNumber=int(input("Give me a number between 1-10 "))
romanNumber='undefined' # give a default value to the variable romanNumber

if araNumber>=0 and araNumber<=10:
    print("We are doing the conversion of ", araNumber)
    if araNumber==1:
        romanNumber='I'
    elif araNumber==2:
        romanNumber='II'
    #etc.
else:
    print("outside of our range 1-10")

# outside of the if statement
# always prints independently of anything else
print("Roman equivalent is", romanNumber)

####----------------------
romanNumber='undefined' # give a default value to the variable romanNumber

# another way to implement the code
if araNumber==1:
    romanNumber='I'
elif araNumber==2:
    romanNumber='II'
    #etc until you reach 10
elif araNumber<0 and araNumber>10:
    print("outside of our range 1-10")
    
# outside of the if statement
# always prints independently of anything else
print("Roman equivalent is (bis)", romanNumber)