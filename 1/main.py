a = input().split()
print(a)
while a[1] != "0":
    a = input().split()
    if a[1] != "0":
        if a[1] == "*":
            print("result: " + str(int(a[0])*int(a[2])))
        elif a[1] == "+":
            print("result: " + str(int(a[0])+int(a[2])))
        elif a[1] == "-":
            print("result: " + str(int(a[0])-int(a[2])))
        elif a[1] == "/" and a[1] != 0:
            print("result: " + str(int(a[0])/int(a[2])))
        else:
            print("eror ?_?")
    print("PRODOLZIT?")
    if input() != "da" or input() != "1":
        a[1] = 0
