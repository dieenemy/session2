from turtle import *
colors = ['red', 'blue', 'brown', 'yellow', 'grey']

# speed(0)



for i in range (3,8):
    if i ==3:
        color(colors[0])
    elif i == 4:
        color(colors[1])
    elif i ==5:
        color(colors[2])
    elif i ==6:
        color(colors[3])
    elif i == 7:
        color(colors[4]) 
    for j in range(i):
        forward(100)
        left(360 / i)

mainloop()