while True:
    i = int(input("Guess my number (1-100): "))
    if i < 51:
        print("Too small :(")
    elif 51 < i <= 100:
    
        print("Too large")
    else:
        print("Bingo")
        break
  