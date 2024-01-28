from turtle import*

color("darkblue", "aqua")
bgcolor("white")
speed(3)
pensize(2)
begin_fill()
while True:
    forward(350)
    right(150)
    if abs(pos()) < 8:
        break
end_fill()

color("darkblue", "red")
bgcolor("black")
speed(3)
pensize(2)
begin_fill()
while True:
    backward(350)
    right(150)
    if abs(pos()) < 8:
        break
end_fill()




#color("darkblue", "green")
#bgcolor("Brown")
#speed(3)
#pensize(2)
#begin_fill()

#while True:
#    backward(200)
#    left(150)
#    if abs(pos()) < 8:
#       break
#end_fill()

done()