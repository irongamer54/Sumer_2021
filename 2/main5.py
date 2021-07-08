import time

def clculator():
    cods=["+","-","*","/","%","//","**"]
    reset=0
    while not reset:
        Vvod=vvod(cods)
        reset=check(Vvod,cods)
        if reset != 1:
            raschet(Vvod,cods)
        reset=0

    input()

def check(vvod,cods):
    
    if vvod[0] == "STOP"or (len(vvod) == 2 and vvod[1] == "STOP") or (len(vvod) == 3 and vvod[2] == "STOP"):
        otvet=input("TOCHNO? ")
        if otvet == "da"or otvet == "1" or otvet == "DA":
            print("ydachi")
            time.sleep(2)
            exit()
    elif vvod[0] == "RES"or (len(vvod) == 2 and vvod[1] == "RES") or (len(vvod) == 3 and vvod[2] == "RES"):
        reset=1
    
        reset = 1
    elif  vvod[0].isdigit() == 0 or vvod[1].isdigit() == 1 or vvod[2].isdigit() == 0:
        print("sintax error")
        reset=1
    elif not vvod[1] in cods:
        print("ne isvestny znak")
        reset = 1
    elif vvod[1] == "/"and vvod[2] == "0":
        print("na nol ne delyat")
        reset=1
    else:
        reset=0
    return reset

def raschet(vvod,cods):
    vvod[0]=int(vvod[0])
    vvod[2]=int(vvod[2])
    znak_deystviya = {
    cods[0]: vvod[0] + vvod[2],
    cods[1]: vvod[0] - vvod[2],
    cods[2]: vvod[0] * vvod[2],
    cods[3]: vvod[0] / vvod[2],
    cods[4]: vvod[0] % vvod[2],
    cods[5]: vvod[0] // vvod[2],
    cods[6]: vvod[0] ** vvod[2],
    }
    b=vvod[1]
    print("Rezyltat: {0:0.2f} ".format(znak_deystviya[b]))

def vvod(cods): 
    return input("vvedite vrogenie (v vide: (a {} b) ) : ".format(cods)).split()

if __name__=="__main__":
    clculator()
