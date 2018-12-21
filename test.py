clothings = ["T-shirt","Sweater"]
n = input("Welcome to our shop, what do you want (C, R, U, D)?")

if n == "C":
    new = input("Enter new item: ")
    clothings.append(new)
    print("Our items:", end=" ")
    print(*clothings,sep=", ")
if n == "R":
    print(*clothings,sep=", ")
if n == "C":
    po = int(input("update pos? "))
    new_item = input("new item? ")
    clothings[po-1] = new_item
    print("Our items:", end=" ")
    print(*clothings,sep=", ")
if n == "D":
    dele = int(input("Delete position? "))
    clothings.pop(dele-1)
    print("Our items: ", end = "")
    print(*clothings,sep=", ")