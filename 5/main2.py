from tkinter import *
root=Tk()
canvas=Canvas(root,width=500,height=500)
canvas.pack()

pers_obj = PhotoImage(file="pers.png")
canvas.create_image(50,50,anchor= NW, image=pers_obj)
root.mainloop()