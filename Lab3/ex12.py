from ex11 import is_inside
a = is_inside([100, 120], [140, 60, 100, 200])
if a == False:
    print("Your function is correct")
else:
    print("Oops, there's a bug")