from os import close
import time
from main7_cl import *
from main7_per import *
 
#users=[["vlad","2006"]]


def main():
    while 1:
        menu()

def  get_mode(mods):
    mod=input()
    if mod in mods:
        return mod
    else:
        return 0 

def new_user():
    print("neW_user")
    user=[0,0,0]
    user = input("vvedite login i porol chrez probel : ").split()
    if len(user)!=2:
        print("error")
        stop=1
    else:
        code = chek(user[0])
        if code == 0:
            while 1:
                flag = 1
                if len(user[1]) < 3:
                    print("min 3 simvola")
                    user[1] = input()
                    flag=0
                if flag == 1:
                    print("povtori porol")
                    if input()== user[1]:
                        break
                
            user.append(perevod_main([1,1,1]))
            users.append(user)
            zapol_file()
    return users
def zapol_file():
    users1 = open("users", 'w')
    for i in range(len(users)):
        users1.write("{} {} {}\n".format(users[i][0], users[i][1], users[i][2]))      
    users1.close()

def perevesti(i):
    print("est: {0:0.2f} $".format(float(users[i][2])))
    user_name=input("vvedite polzovanel bez probel : ")
    for j in range(len(users)):
        if users[j][0] == user_name:
            print("pol cysh")
            sum=perevod_main([1, 1, 1])
            if sum > float(users[i][2]):
                print("nedostatochno sredstv")
                return 0
            else:
                print("perevojy")
                users[j][2] = float(users[j][2])+sum
                users[i][2] = float(users[i][2])-sum
                zapol_file()
                his = open("his", 'a')
                his.write("{} перевел {} пользователю {}\n".format(
                    users[i][0], sum, users[j][0]))
                his.close()
            return 1
    print("polzovot ne nayden")
    return 0
def enter(): 
    print("user")
    user=input("vvedite login i porol chrez probel : ").split()
    if len(user) != 2:
        print(" sintax error")
        return 0
    for i in range(len(users)+1):
        if i == len(users):
            print("polzovot ne nayden")
            return 0
        if users[i][0]==user[0]:
            print("login vern")
            for j in range(5):
                if users[i][1] == user[1]:
                    print("inside")
                    inside(i)
                    return 1
                else:
                    print("porol ne vern")
                    print("povtori popIT ky")
                    user[1]=input()
                    #if len(user)!=2:
                    #    print("oshibka porolya")
                    print("popIT ok ostalos {}".format(5-j-1))
            print("porol ne vern popitok net")
            return 0

def admin_chek(i):
    if users[i][0] == "admin_0w0":
        user_name = input("vvedite login  bez probel : ")
        flag = 1
        for j in range(len(users)):
            if users[j][0] == user_name:
                print("pol cysh")
                return i = j
    
    
            
def popol(user):
    print("est: {0:0.2f} $".format(float(users[user][2])))
    sum=perevod_main([1, 1, 1])
    users[user][2] = float(users[user][2])+sum
    print("Rezyltat: {0:0.2f} $".format(users[user][2]))
    zapol_file()
    his = open("his", 'a')
    his.write("{} пополнил счет на {} \n".format(
        users[i][0], sum)) 
    his.close()
def name(i):
    i = admin_chek(i)

    if input("ti yveren? ")== "da":
        user_name=input("vvedite login  bez probel : ")
        if chek(user_name)==0:
            his = open("his", 'a')
            if flag == 1:
                his.write("admin:")
            his.write("{} сменил имя на - {}  \n".format(
                users[i][0], user_name))
            his.close()
            users[i][0] = user_name
            zapol_file()

def porol(i):
    if users[i][0]=="admin_0w0":
        user_name = input("vvedite login  bez probel : ")
        flag=1
        for j in range(len(users)):
            if users[j][0] == user_name:
                print("pol cysh")   
                i=j  
    #print(i)
    #print(users[i][1])
    if input("ti yveren? ") == "da":
        user_porol=input("vvedite porol bez probel : ")
        if len(user_porol) < 3:
           print("min 3 simvola")
           return 0
        else:
            print(" yspeshno")
            print(user_porol)
            his = open("his", 'a')
            if flag == 1:
                his.write("admin:")
            his.write("{} сменил пароль на - {}  \n".format(
                users[i][0], user_porol))
            his.close()
            users[i][1] = user_porol
            zapol_file()

def info(i):
    for j in range(len(users)):
        print(users[j])
def plzo(i):
    
    for J in range(len(users)):
        print(users[J][0])

def istor(i):
    his = open("his", 'r')
    his2 = his.read().split('\n')
    for i in range(len(his2)):
        print(his2[i])
    his.close()

def inside(i):
    while 1:

        print()
        print()
        print("polzovatel {}, balance {}".format(users[i][0], users[i][2]))
        print()
        print("1 - смена логина")
        print("2 - смена пароля")
        print("3 - список пользователей")
        print("4 - калькулятор")
        print("5 - конвертор валют")
        print("6 - пополнить счет")
        print("7 - перевести деньги")
        if users[i][0] == "admin_0w0":
            print("8 - все про ползователей")
            print("9 - история")
        print("любой знак - выход")
        mods2 = {
            '1': name,
            '2': porol,
            '3': plzo,
            '4': clculator,
            '5': perevod_main,
            '6': popol,
            '7': perevesti,
            '8': info,
            '9': istor
        }
        mod = get_mode(mods2)
        if mod:
            print()
            print()
            if int(mod) > 7 and users[i][0] != "admin_0w0":
                mod="1dawdw"
                mods2[mod](i)
            else:
                mods2[mod](i)
        else:
            print()
            print()
            print()
            return 0


def menu():
    print()
    print()
    mods={
        '1': enter,
        '2': new_user,
        '3': exit
    }
    print("1 - sing in")
    print("2 - sing up")
    print("3 - exit")
    print(users)
    mod=get_mode(mods)
    if mod:
        print()
        print()
        mods[mod]()

    
    #mods[get_mode(mods)]

def chek(user_name):
    for i in range(len(users)):
        if users[i][0] == user_name:
            print("pol cysh")
            return 1
    print("polzovot ne nayden")
    return 0


if __name__ == "__main__":
    users1 = open("users", 'r')
    users = users1.read().split('\n')
    for i in range(len(users)):
        users[i] = users[i].split()
    users.pop(len(users)-1)
    #print(users)
    users1.close()
    main()
