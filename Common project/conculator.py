from ast import Num
from tkinter import *
from PIL import Image,ImageTk


valu=[]
root = Tk()
root.title("Đĩ chó nguyễn")
labeltitle=Label(root,text='Number',fg="blue")
labeltitle.grid(column=0,row=0)
labeltitle2=Label(root,text='RESULT',fg="blue")
labeltitle2.grid(column=2,row=0)



e=Entry(root,width=30,borderwidth=5)
e.grid(column=0,row=1,padx=1,pady=5,columnspan=2)
rslt=Label(root,text=0,width=5,borderwidth=5,bg="red")
rslt.grid(column=2,row=1,padx=5,pady=5)

def tru():
    global rslt
    rslt.grid_forget()
    c=float(valu[0]-valu[-1])
    rslt=Label(root,text=c,width=10,borderwidth=5,bg="red")
    rslt.grid(column=2,row=1,padx=5,pady=5)
    valu.clear()
    valu.append(c)
def cong():
    global rslt
    rslt.grid_forget()
    c=float(valu[0]+valu[-1])
    rslt=Label(root,text=c,width=10,borderwidth=5,bg="red")
    rslt.grid(column=2,row=1,padx=5,pady=5)
    valu.clear()
    valu.append(c)
def nhan():
    global rslt
    rslt.grid_forget()
    c=float(valu[0]*valu[-1])
    rslt=Label(root,text=c,width=10,borderwidth=5,bg="red")
    rslt.grid(column=2,row=1,padx=5,pady=5)
    valu.clear()
    valu.append(c)
def chia():
    global rslt
    rslt.grid_forget()
    if valu[-1]!=0:
        c=float(valu[0]/valu[-1])
        valu.clear()
        valu.append(c)
    else:
        c="thg ngu sao chia cho 0 duoc!!"
        valu.clear()
        valu.append(0)
    rslt=Label(root,text=c,width=10,borderwidth=5,bg="red")
    rslt.grid(column=2,row=1,padx=5,pady=5)
def clearance():
    
    rslt.grid_forget()
    valu.clear()
    clear()
    
def ope(a):
    e.insert(END,a)
def clear():
    e.delete(0,END)
def minus():
    
    if e.get()!="":
        valu.append(float(e.get()))
    if len(valu)==1:
        valu.append("-")
    elif len(valu)==2 and valu[-1]!="-":
        valu[-1]="-"
    elif len(valu)==3:
        if valu[1]=="+":
            cong()
            valu.append("-")
        elif valu[1]=="-":
            tru()
            valu.append("-")
        elif valu[1]=="*":
            nhan()
            valu.append("-")
        elif valu[1]=="/":
            chia()
            valu.append("-")
    clear()
    print(valu)
def plus():
    if e.get()!="":
        valu.append(float(e.get()))
    if len(valu)==1:
        valu.append("+")
    elif len(valu)==2 and valu[-1]!="+":
        valu[-1]="+"
    elif len(valu)==3:
        if valu[1]=="+":
            cong()
            valu.append("+")
        elif valu[1]=="-":
            tru()
            valu.append("+")
        elif valu[1]=="*":
            nhan()
            valu.append("+")
        elif valu[1]=="/":
            chia()
            valu.append("+")
    clear()
    print(valu)
def evall():
    plus()
def button(a,x,y):
    but7=Button(root,text=a,padx=40,pady=20,command=lambda:ope(a))
    but7.grid(column=x,row=y)
def divi():
    if e.get()!="":
        valu.append(float(e.get()))
    if len(valu)==1:
        valu.append("/")
    elif len(valu)==2 and valu[-1]!="/":
        valu[-1]="/"
    elif len(valu)==3:
        if valu[1]=="+":
            cong()
            valu.append("/")
        elif valu[1]=="-":
            tru()
            valu.append("/")
        elif valu[1]=="*":
            nhan()
            valu.append("/")
        elif valu[1]=="/":
            chia()
            valu.append("/")
    clear()
    print(valu)
def multi():
    if e.get()!="":
        valu.append(float(e.get()))
    if len(valu)==1:
        valu.append("*")
    elif len(valu)==2 and valu[-1]!="*":
        valu[-1]="*"
    elif len(valu)==3:
        if valu[1]=="+":
            cong()
            valu.append("*")
        elif valu[1]=="-":
            tru()
            valu.append("*")
        elif valu[1]=="*":
            nhan()
            valu.append("*")
        elif valu[1]=="/":
            chia()
            valu.append("*")
    clear()
    print(valu)
button(1,0,2)
button(2,1,2)
button(3,2,2)
button(4,0,3)
button(5,1,3)
button(6,2,3)
button(7,0,4)
button(8,1,4)
button(9,2,4)
button(0,0,5)
def button(a,x,y):
    but7=Button(root,text=a,padx=39,pady=20,command=plus)
    but7.grid(column=x,row=y,columnspan=1)
button("+",1,5)
def button(a,x,y):
    but7=Button(root,text=a,padx=41,pady=20,command=minus)
    but7.grid(column=x,row=y,columnspan=1)
button("-",2,5)
def button(a,x,y):
    but7=Button(root,text=a,width=1,padx=40,pady=20,command=divi)
    but7.grid(column=x,row=y,columnspan=1)
button("/",1,6)
def button(a,x,y):
    but7=Button(root,text=a,padx=41,pady=20,command=multi)
    but7.grid(column=x,row=y,columnspan=1)
button("*",2,6)
but7=Button(root,text="Clear",padx=30,pady=20,command=clearance)
but7.grid(column=0,row=6,columnspan=1)
but7=Button(root,text="=",padx=137,pady=20,command=evall)
but7.grid(column=0,row=9,columnspan=3)
root.mainloop()
