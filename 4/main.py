from tkinter import *
cliks=0
btn=[]
itog="" 
v=0
itogov=0
def btn_clk(i,a):
    global v,itog,itogov
    znak_deystviya = {
    '0':"+",
    '1':"-" ,    
    '2':"*" ,
    '3':"/",
    '4':"%" ,
    '5':"//",
    '6':"**",
    '7':"=" ,
}
    if a ==1:
        if i=='7':
            try:
                itogov=eval(itog)
                lable_text2.set("itog:{}".format(itogov)) 
                print(itogov)
                itog=''
            except:
                itogov="EROR"
                lable_text2.set("itog:{}".format(itogov)) 
                itogov=0
                itog=''
        else:
            lable_text.set("itog:{}".format(itog))
            itog+=znak_deystviya[i]

    else:
        itog+=str(i)
    lable_text.set("itog:{}".format(itog))
    print(itog)
  
cods_znak=["+","-","*","/","%","//","**","="]


root=Tk()
root.title("new progarm")
root.geometry("500x500")
lable_text2=StringVar()
lable_text2.set("itog:{}".format(itogov))
lable_text=StringVar()
lable_text.set("vvod:{}".format(itog))

#button_text = StringVar()
#button_text.set("cliks {}".format(cliks))
y=0.1
c=0
btn.append (Button(text=c,command=lambda i=c: btn_clk(str(i),0)))
btn[c].place(relx=0.2,rely=0.2,anchor='c',height=50, width=50)
c=1
for j in range(3):
    y+=0.1
    x=0.2
    for i in range(3):
        x+=0.1
        
        btn.append (Button(text=c,command=lambda i=c: btn_clk(str(i),0)))
        btn[c].place(relx=x,rely=y,anchor='c',height=50, width=50)
        c+=1




y=0.1
for i in range(len(cods_znak)):
    y+=0.1
    btn.append (Button(text=cods_znak[i],command=lambda i=i: btn_clk(str(i),1)))
    c+=1
    btn[c-1].place(relx=0.6,rely=y,anchor='c',height=50, width=50)


lable= Label(textvariable=lable_text)
lable2= Label(textvariable=lable_text2)
lable.place(relx=.5,rely=.02,anchor='c',height=10, width=500)
lable2.place(relx=.5,rely=.10,anchor='c',height=10, width=500)
root.mainloop()
