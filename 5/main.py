from tkinter import *
import random
import time
def random_c():
    return random.randint(1,1000)



def zmey():
    global x,y
    x_z=20
    y_z=20
    while 1 :
        x_z+=0.001
        y_z+=random_c()
        frame2.place(x=x_z,y=y_z,anchor='c')
        root.update()
        if x == x_z and y == y_z:
            frame1.place(x=random_c(),y=random_c(),anchor='c')
        time.sleep(1)

root=Tk()
root.title("new progarm")
root.geometry("1000x1000")


x=500
y=500
print("0")

frame2 = Frame(root, width=15, height=15, bg="green")
frame2.place(x=x,y=y,anchor='c')


frame1 = Frame(root, width=15, height=15, bg="red")
frame1.place(x=random_c(),y=random_c(),anchor='c')
root.update()
time.sleep(5)
zmey()
print("1")
root.mainloop()