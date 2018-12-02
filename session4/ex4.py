# 4.1
# print("Hello, my name is Tung and there are my sheep sizes")
size = [5, 7, 300, 90, 24, 50, 75]
# print(size)

# 4.2
# print("Hello, my name is Tung and there are my sheep sizes")
# print(size)
# n = max(size)
# print("Now my biggest sheep has size", n ,end=" ")
# print("let's shear it")

# 4.3
# print("Hello, my name is Tung and here is my flock")
# print(size)
# size.remove(n)
# print("After shearing, here is my flock")
# print(size)

# 4.4
# print("Hello, my name is Tunga and here is my flock")
# print(size)
# n = max(size)
# print("Now my biggest sheep has size", n ,end=" ")
# print("let's shear it")
# size.remove(n)
# print("After shearing, here is my flock")
# print(size)
# for i in range(len(size)):
#     size[i] = size[i] + 50
# print("One month is passed, now here is my flock: ")
# print(size)

# 4.5
print("Hello, my name is Tung and here is my flock")
print(size)
for i in range(1,5):
    print("MONTH", i, end=":")
    print()
    for j in range(len(size)):
        size[j] = size[j] + 50
    print("One month is passed, now here is my flock: ")
    print(size)

    n = max(size)
    print("Now my biggest sheep has size", n ,end=" ")
    print("let's shear it")

    size.remove(n)
    print("After shearing, here is my flock")
    print(size)

size_sum = sum(size)
print("My flock has sizes in total: ", size_sum)
money = size_sum * 2
print("I would get ", size_sum, end = " * 2$ = ")
print(money)





