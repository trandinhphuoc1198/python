from tkinter.constants import SUNKEN
from PIL import Image,ImageTk,ImageFilter
import pathlib
import tkinter
root = tkinter.Tk()
imagefold=pathlib.Path('C:/Users/g1nta/AppData/Local/ZaloPC/2065141770268655419/ZaloDownloads/picture/')
imagefile=imagefold.glob('*/*.jpg')
root.geometry('300x300')
x=[]
n=[0]
c=0
for i in imagefile:
    if c==10:
        break
    original=Image.open(i)
    original.thumbnail((500,500))
    b=ImageTk.PhotoImage(original)
    x.append(b)
    c+=1
label1=tkinter.Label(image=x[0],width=500,height=200)
label1.grid(column=0,row=0,columnspan=10)
now=tkinter.Message(text=1,padx=5,pady=5,relief=SUNKEN)
now.grid(column=2,row=1)
def forward():
    n.append(n[-1]+1)
    cur=n[-1]
    global label1
    global now
    label1.grid_forget()
    now.grid_forget()
    if cur>=len(x):
        label22=tkinter.Message(text="out of range")
        label22.grid(column=0,row=0,columnspan=3)
        return None
    label1=tkinter.Label(image=x[cur],width=500,height=200)
    label1.grid(column=0,row=0,columnspan=3)
    now=tkinter.Message(text=cur+1,padx=5,pady=5)
    now.grid(column=2,row=1)
def back():
    n.append(n[-1]-1)
    cur=n[-1]
    global label1
    global now
    label1.grid_forget()
    now.grid_forget()
    if abs(cur)>=len(x):
        label22=tkinter.Message(text="out of range")
        label22.grid(column=0,row=0,columnspan=3)
        return None
    label1=tkinter.Label(image=x[cur],width=500,height=200)
    label1.grid(column=0,row=0,columnspan=3)
    now=tkinter.Message(text=cur+1,padx=5,pady=5)
    now.grid(column=2,row=1)
nextbutton=tkinter.Button(root,text="Next",padx=5,pady=5,command=forward)
nextbutton.grid(column=3,row=1)
out=tkinter.Button(root,text="back",padx=5,pady=5,command=back)
out.grid(column=0,row=1)
root.mainloop() 