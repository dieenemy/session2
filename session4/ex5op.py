# #a
# from random import randint

# word = "champion"
# character = list(word)
# for _ in range(len(character)):
#     i = randint(0, len(character) - 1)
#     ch = character[i]

#     print(ch, end=" ")

#     character.pop(i)

# print()

# user_guess = input("Your guess? ")
# if user_guess == word:
#     print("hura")
# else:
#     print(":(")
#b
from random import randint

lists = ["hexagon", "meticulous", "champion"]

i = randint(0, len(lists) - 1)
a = lists[i]
word = lists[i]

for k in range(len(a)):               
    j = randint(0, (len(a) - 1))
    a = list(a)
    ch = a[j]
    print(ch,end=" ")
    a.pop(j)
print()

user_guess = input("Your answer: ")
if user_guess == word:
    print("Hura")
else:
    print(":(") 


