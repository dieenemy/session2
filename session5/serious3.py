print("Answer the following algebra question:")
print("If x = 8, then waht is the value of 4(x + 3) ?")
answer = [35,36,40,44]

for i in range(len(answer)):
    print(i + 1, answer[i],sep='.')

n = int(input("Your choice:"))
if n == 4:
    print("bingo")
else:
    print(":(")