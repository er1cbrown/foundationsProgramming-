from turtle import *
home()
color('red','blue')
begin_fill()
forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)
end_fill()

penup() # to move the cursor without drawing
forward(200) # 200 to be away enough from the first rectangle
pendown()
#clear()
#reset() reset everything to default
#---------------------------
color('blue','orange')
begin_fill()
forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)
end_fill()

penup() # to move the cursor without drawing
left(270)
forward(250) # 200 to be away enough from the first rectangle
pendown()
color('orange','green')
begin_fill()
circle(100)
end_fill()
