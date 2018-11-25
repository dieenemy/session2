from turtle import *

# speed(0)



for i in range (3,7):
    if i ==3:
        color("blue")
    elif i == 5:
        color("blue")
    else:
        color("red")
    for j in range(i):
        forward(100)
        left(360 / i)

# print(canh)
# canh = 2
# for i in range (4):
#    canh += 1

# for i in range(3):
#     forward(100)
#     left(120)
# for i in range(4):
#     forward(100)
#     left(90)
# for i in range(5):
#     forward(100)
#     left(72)
# for i in range(6):
#     forward(100)
#     left(60)









mainloop()