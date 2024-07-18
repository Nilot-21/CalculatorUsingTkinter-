from tkinter import *

def click(event):
    global scvalue
    text=event.widget.cget("text")
    if text=="=":
        if scvalue.get().isdigit():
            value=int(scvalue.get())
        else:
            value=eval(screen.get())
        scvalue.set(value)
        screen.update()
    elif text=="C":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get()+text)
        screen.update()

#open a new window
root=Tk()
#set the dimension
root.geometry("630x900")
#set the title
root.title("Calculator")
#represent a string varible
scvalue=StringVar()
#screen value is empty
scvalue.set("")
#to provide the input
screen=Entry(root,textvar=scvalue,font='Lucida 30 bold')
screen.pack(fill=X,ipadx=8,pady=8,padx=8)
f=Frame(root,bg="grey")
b=Button(f,text="9",padx=5,pady=6,font="Lucida 30 bold")
b.pack(side="left",padx=18,pady=5)
b.bind("<Button-1>",click)
b=Button(f,text="8",padx=5,pady=6,font="Lucida 30 bold")
b.pack(side="left",padx=18,pady=5)
b.bind("<Button-1>",click)
b=Button(f,text="7",padx=5,pady=6,font="Lucida 30 bold")
b.pack(side="left",padx=18,pady=5)
b.bind("<Button-1>",click)
f.pack()

f=Frame(root,bg="grey")
b=Button(f,text="6",padx=5,pady=6,font="Lucida 30 bold")
b.pack(side="left",padx=18,pady=5)
b.bind("<Button-1>",click)
b=Button(f,text="5",padx=5,pady=6,font="Lucida 30 bold")
b.pack(side="left",padx=18,pady=5)
b.bind("<Button-1>",click)
b=Button(f,text="4",padx=5,pady=6,font="Lucida 30 bold")
b.pack(side="left",padx=18,pady=5)
b.bind("<Button-1>",click)
f.pack()

f=Frame(root,bg="grey")
b=Button(f,text="3",padx=5,pady=6,font="Lucida 30 bold")
b.pack(side="left",padx=18,pady=5)
b.bind("<Button-1>",click)
b=Button(f,text="2",padx=5,pady=6,font="Lucida 30 bold")
b.pack(side="left",padx=18,pady=5)
b.bind("<Button-1>",click)
b=Button(f,text="1",padx=5,pady=6,font="Lucida 30 bold")
b.pack(side="left",padx=18,pady=5)
b.bind("<Button-1>",click)
f.pack()


f=Frame(root,bg="grey")
b=Button(f,text="*",padx=9,pady=6,font="Lucida 30 bold")
b.pack(side="left",padx=17,pady=5)
b.bind("<Button-1>",click)
b=Button(f,text="-",padx=9,pady=6,font="Lucida 30 bold")
b.pack(side="left",padx=17,pady=5)
b.bind("<Button-1>",click)
b=Button(f,text="0",padx=9,pady=6,font="Lucida 30 bold")
b.pack(side="left",padx=17,pady=5)
b.bind("<Button-1>",click)
f.pack()

f=Frame(root,bg="grey")
b=Button(f,text="=",padx=5,pady=6,font="Lucida 30 bold")
b.pack(side="left",padx=18,pady=5)
b.bind("<Button-1>",click)
b=Button(f,text="%",padx=5,pady=6,font="Lucida 30 bold")
b.pack(side="left",padx=18,pady=5)
b.bind("<Button-1>",click)
b=Button(f,text="/",padx=5,pady=6,font="Lucida 30 bold")
b.pack(side="left",padx=18,pady=5)
b.bind("<Button-1>",click)
f.pack()

f=Frame(root,bg="grey")
# b=Button(f,text="=",padx=5,pady=6,font="Lucida 30 bold")
# b.pack(side="left",padx=15,pady=5)
# b.bind("<Button-1>",click)
# b=Button(f,text="%",padx=5,pady=6,font="Lucida 30 bold")
# b.pack(side="left",padx=15,pady=5)
# b.bind("<Button-1>",click)
b=Button(f,text="C",padx=5,pady=6,font="Lucida 30 bold")
b.pack(side="left",padx=15,pady=5)
b.bind("<Button-1>",click)
f.pack()

root.mainloop()