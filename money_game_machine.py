# page 117-Exercise 10
# money counting game
# MZK

# Here we get the values from the user
# since the number cannot be a fraction, we convert into integer

nbPennies=int(input("Please input the number of pennies "))
nbNickles=int(input("Please input the number of nickles "))
nbDimes=int(input("Please input the number of dimes "))
nbQuarters=int(input("Please input the number of quarters "))

# We calculated the weighted sum in cents
# we don't need parenthesis here because multiplication has
# a higher priority than addition
amountCents=nbPennies+nbNickles*5+nbDimes*10+nbQuarters*25

if amountCents==100:
    print("congratulation you win!")
elif amountCents<100:
    print("Sorry the amount is less than 100")
else:
    print("Sorry the amount is more than 100", nbPennies)
