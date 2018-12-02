clothings = ["T-shirt","Sweater"]
enter = str(input("what do you want (C, R, U, D)"))
if enter == "C":
    new = input("Enter new item: ")
    clothings.append(new)
    print("Our items: ", end = "")
    print(*clothings,sep=", ")
elif enter == "R":
    print("Our items: ", end = "")
    print(*clothings,sep=", ")
elif enter == "U":
    po = int(input("update pos? "))
    new_item = input("new item? ")
    clothings[po-1] = new_item
    print("Our items: ", end = "")
    print(*clothings,sep=", ")
elif enter == "D":
    dele = int(input("Delete position? "))
    clothings.pop(dele-1)
    print("Our items: ", end = "")
    print(*clothings,sep=", ")