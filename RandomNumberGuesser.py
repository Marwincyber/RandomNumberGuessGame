import random
yeti = random.randint(1,20)
print("I picked a number from one to twenty")
print("Try to guess the number")
for guess in range (1,12):
    observe = int(input("Give me your best guess\n"))
    if observe == yeti:
        print("Good job you have guessed it right!")
        break
    elif observe < yeti:
        print("Too low")
    else:
        print("Too high")
