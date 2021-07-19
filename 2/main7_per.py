kyrs = [73, 87, 1.19]
cods_val = ["$", "RUB", "EUR"]


def perevod_main(i):
    vvod=[0,0,0]
    itog_vvod = [1, 1, 1]
    while not (itog_vvod==[2,2,2] or vvod==i):
        vvod[0], vvod[1], vvod[2] = vvod_per(i)
        if not (vvod == [1,1,1]):
            itog_vvod[0], itog_vvod[1], itog_vvod[2] = stop(vvod)
            if not ((itog_vvod==[1,1,1] or itog_vvod == [2,2,2])):
                itog=perevod(itog_vvod[0], itog_vvod[1], itog_vvod[2],i)
                if i == [1, 1, 1]:
                    return(itog)
                    vvod=i


def stop(start):
    if start == [1, 1, 1]:
        return 1, 1, 1
    elif start[0] == "RES" or (len(start) == 2 and start[1] == "RES") or (len(start) == 2 and start[2] == "RES"):
        print("kak hosh")
        return 1, 1, 1
    elif start[0] == "STOP" or (len(start) == 2 and start[1] == "STOP") or (len(start) == 2 and start[2] == "STOP"):
        otvet = input("TOCHNO? ")
        if otvet == "da"or otvet == "1" or otvet == "DA":
            print("ydachi")
            return 2, 2, 2
    elif len(start) != 3:
        print("sintax error2")
        return 1, 1, 1
    elif str(start[0]).isdigit() == 0 or str(start[1]).isdigit() == 1 or str(start[2]).isdigit() == 1:
        print("sintax error3")
        return 1, 1, 1
    elif int(start[0]) <= 0:
        print("y deneg net")
        return 1, 1, 1
    else:
        return start


def vvod_per(i):
    cod1 = input("cho est {}? ".format(cods_val)).split()
    if len(cod1) != 2:
        print("sintax error1")
        return 1, 1, 1
    if not i==[1,1,1]:  
        cod2 = input("tebe chego {}? ".format(cods_val))
    else:
        cod2='$'
    return cod1[0], cod1[1], cod2


def perevod(sum, cod1, cod2, i):
    znak_1_val = {
        # cods_val=["$","RUB","EUR"]
        cods_val[0]+cods_val[0]: int(sum),
        cods_val[1]+cods_val[1]: int(sum),
        cods_val[2]+cods_val[2]: int(sum),
        cods_val[1]+cods_val[0]: int(sum)/kyrs[0],
        cods_val[2]+cods_val[0]: int(sum)*kyrs[2],
        # cods_val=["$","RUB","EUR"]
        cods_val[0]+cods_val[1]: int(sum)*kyrs[0],
        cods_val[2]+cods_val[1]: int(sum)*kyrs[1],
        cods_val[1]+cods_val[2]: int(sum)/kyrs[1],
        cods_val[0]+cods_val[2]: int(sum)/kyrs[2],  # kyrs=[73,87,1.19]
    }
    cod = cod1+cod2
    if cod in znak_1_val:
        if not i == [1, 1, 1]:
            print("Rezyltat: {0:0.2f} ".format(znak_1_val[cod]))
        else:
            return znak_1_val[cod]
