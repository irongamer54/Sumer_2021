cods_znak = ["+", "-", "*", "/", "%", "//", "**"]
def clculator(i):

    reset = 0
    while 2 != reset:
        Vvod = vvod(cods_znak)
        reset = check(Vvod)
        if reset == 0:
            raschet(Vvod)


def check(vvod):

    if vvod[0] == "STOP"or (len(vvod) == 2 and vvod[1] == "STOP") or (len(vvod) == 3 and vvod[2] == "STOP"):
        otvet = input("TOCHNO? ")
        if otvet == "da"or otvet == "1" or otvet == "DA":
            print("ydachi")
            reset = 2
    elif vvod[0] == "RES"or (len(vvod) == 2 and vvod[1] == "RES") or (len(vvod) == 3 and vvod[2] == "RES"):
        reset = 1
    elif len(vvod) != 3:
        print("sintax error")
        reset = 1
    elif vvod[0].isdigit() == 0 or vvod[1].isdigit() == 1 or vvod[2].isdigit() == 0:
        print("sintax error")
        reset = 1
    elif not vvod[1] in cods_znak:
        print("ne isvestny znak")
        reset = 1
    elif vvod[1] == "/"and vvod[2] == "0":
        print("na nol ne delyat")
        reset = 1
    else:
        reset = 0
    return reset


def raschet(vvod):
    vvod[0] = int(vvod[0])
    vvod[2] = int(vvod[2])
    znak_deystviya = {
        cods_znak[0]: vvod[0] + vvod[2],
        # cods_znak=["+","-","*","/","%","//","**"]
        cods_znak[1]: vvod[0] - vvod[2],
        cods_znak[2]: vvod[0] * vvod[2],
        cods_znak[3]: vvod[0] / vvod[2],
        cods_znak[4]: vvod[0] % vvod[2],
        cods_znak[5]: vvod[0] // vvod[2],
        cods_znak[6]: vvod[0] ** vvod[2],
    }
    b = vvod[1]
    print("Rezyltat: {0:0.2f} ".format(znak_deystviya[b]))


def vvod(cods_znak):
    return input("vvedite vrogenie (v vide: (a {} b) ) : ".format(cods_znak)).split()
