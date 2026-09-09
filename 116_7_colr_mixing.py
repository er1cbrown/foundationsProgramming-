# Color Mixing 116 - 7
# MZK
# 9/23/2016

#we get the data from the user
color1=input("Please enter the first color ")
color2=input("Please enter the second color ")

if color1 != "red" or color1 != "yellow" or color1 != "blue":
    print(color1, "is not a primary color")
    
# I did not use elif below because I want to display two error messages
# if the user inputs two non primary colors
if color2!= "red" or color2 != "yelow" or color2 != "blue":
    print(color2, "is not a primary color")
  
elif (color1=="red" and  color2=="blue") or (color2=="red" and  color1=="blue"):
    print("You get purple")

elif (color1=="red" and  color2=="yellow") or (color2=="red" and  color1=="yellow"):
    print("You get orange")

elif (color1=="blue" and  color2=="yellow") or (color2=="blue" and  color1=="yellow"):
    print("\nYou get green")

