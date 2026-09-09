# Magic Dates page 116 - 6
# MZK
# 9/23/2016

#we get the data from the user
month=int(input("Please enter the month "))
day=int(input("Please enter the day "))
year=int(input("Please enter the last towo digits of a year "))

#product will be compared to year
product = month*day

if product == year:
    print("This is a magic date")
else:
    print("The date is not magic")

