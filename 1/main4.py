def main():
    cods=["$","RUB","EUR"]
    stop=1
    while stop:
        start = get_money(cods)
        start = STOP(start)
        if start[0]==1 and start[1]==2:
            if start[2]==3:
                stop=perevod(0, 1, "STOP!!!",cods)
        else: 
            key = n_valt(cods)
            stop=perevod(start[0], start[1],key,cods)
    
def STOP(start):
    if start[0] == "STOP" or start[1] == "STOP":
        print("kak hosh")
        return 1, 2, 0
    elif start[0] == "STOP!!!" or start[1] == "STOP!!!":
        return 1, 2, 3
    elif int(start[0]) <= 0:
        print("y tebz deneg net? ny katic togda")
        return 1, 2, 0
    else:
        return start

def get_money(cods):
    start = input("cho est {}? ".format(cods)).split()
    return start

def n_valt(cods):
    return input("tebe chego {}? ".format(cods))

def perevod (sum,key1,key,cods):
    sum=int(sum)
    kyrs=[73,87,1.19]
   # EUR = 87
   # USD = 73
   # E_D = 1.19
    if key == "STOP" or key1 == "0":
        print("kak hosh")
        return 1
    if key == "STOP!!!" or key1 == "1":
        print("kak hosh")
        return 0
    if key ==  cods[0]:
        if key1 ==  cods[1]:
            print("vasgi dengi {0:0.2f} $".format(sum/kyrs[0]))
        elif key1 ==  cods[2]:
            print("vasgi dengi {0:0.2f} $".format(sum*kyrs[2]))
        else:
            print("ti typoy? y tebya chto za volyta")
            return 1
             
    elif key ==  cods[2]:
        if key1 ==  cods[1]:
            print("vasgi dengi {0:9.2f} EUR".format(sum/kyrs[1]))
        elif key1 ==  cods[0] :
            print("vasgi dengi {0:9.2f} EUR".format(sum/kyrs[2]))
        else:
            print("ti typoy? y tebya chto za volyta")
            return 1
             
    elif key ==  cods[1]:
        if key1 ==  cods[2]:
            print("vasgi dengi {0:9.2f} RUB".format(sum*kyrs[1]))
        elif key1 ==  cods[0]:
            print("vasgi dengi {0:9.2f} RUB".format(sum*kyrs[0]))
        else:
            print("ti typoy? y tebya chto za volyta")
            return 1
            
    else:
        print("ti typoy? tede chego")
        return 1

        

if __name__ == "__main__":
    main()
