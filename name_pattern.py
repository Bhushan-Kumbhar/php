name = input("Enter your name : ")

for i in range(len(name)):
    for j in range(i):
        print(" ",end="")
    print(name[i])