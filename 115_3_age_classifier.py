#age classifier page 115 - 2
# MZK
# 9/23/2016

# I am assming here that the age is a float
age=float(input("Could you please tell me the person's age? "))

if age <=1:
    print("It's an infant")
elif age >1 and age < 13:
    print("It's a child")
elif age >=13 and age < 20:
    print("It's a teenaager")
else:
    print("It's a adult")
