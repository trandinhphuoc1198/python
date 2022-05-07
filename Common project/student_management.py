import re,pathlib
class student:
    id=0
    def __init__(self,name,gender,math,english):
        self.name=name
        self.gender=gender
        self.math=math
        self.english=english
        self.id=self.id+1
        student.id+=1
    @property
    def ave(self):
        ave=(self.math+self.english)/2
        return ave
    def ranking(self):
        if self.ave>7:
            return "very Good"
        elif self.ave>5:
            return "normal"
        else:
            return "bad"
    @classmethod
    def add_student(cls,info):
        return cls(info[0],info[1],info[2],info[3])
a2=student("Tran Dinh Phuoc","Male",10,13)
a3=student("Tran Dinh Phuoc","Male",5,2)
a4=student("Tran Dinh Phuoc","Male",10,1)
a5=student("Tran hui","Male",2,3)
class1=[a2,a3,a4,a5]

def add():
    a1=input("Input name: ")
    a2=input("Input gender: ")
    a3=int(input("Input match: "))
    a4=int(input("Input english: "))
    lst=[a1,a2,a3,a4]
    class1.append(student.add_student(lst))
    print(" add successfull!")

def display(lst):
    print('---'*22)
    print('%01s'%'No.','%03s'%'ID','%17s'%'Name     ','%14s'%'Gender','%11s'%'Math','%11s'%'English','%10s'%'Average','%15s'%'Ranking')
    for x,y in enumerate(lst):
        x+=1
        print('%01s'%x,end='')
        print('%05s'%y.id,end='')
        print('%19s'%y.name,end='')
        print('%15s'%y.gender,end='')
        print('%12s'%y.math,end='')
        print('%10s'%y.english,end='')
        print('%12s'%y.ave,end='')
        print('%15s'%y.ranking())
    print('---'*22)

def search():
    lst=[]
    word = input("Search: ")
    for x in class1:
        if word in x.name:
            lst.append(x)
    display(lst)

def delete():
    display(class1)
    id= int(input("Delete id: "))
    for x,y in enumerate(class1):
        if y.id==id:
            class1.pop(x)
            print(id,"Deleted")
    
def arrange():
    y=input("Sorted by: ")
    if y.lower() =="name":
        lst=sorted(class1,key=lambda x:x.name,reverse=True)
    if y.lower() =="id":
        lst=sorted(class1,key=lambda x:x.id,reverse=False)
    if y.lower() =="average":
        lst=sorted(class1,key=lambda x:x.ave,reverse=True)
    display(lst)

def update():
    lst=[]
    a=int(input("Student's id that need changed: "))
    for y,x in enumerate(class1):
        if x.id==a:
            a=y
            lst.append(x)
            break
    display(lst)
    b=input("Change: ").split('=')
    if re.match(r"ma",b[0]):
        class1[a].math=int(b[1])
    elif re.match(r"en",b[0]):
        class1[a].english=int(b[1])
    elif re.match(r"na",b[0]):
        class1[a].name=b[1]
    lst[0]=class1[a]
    display(lst)

while True:
    print("---"*22,'\n\t\t\tMenu\n1.Display\n2.Search\n3.Add\n4.Delete\n5.Update\n6.Arrange\n','---'*22)
    a=int(input("Choice: "))
    if not a:break
    elif a == 1: 
        display(class1)
    elif a== 2:search()
    elif a== 3:add()
    elif a==4:delete()
    elif a==5:update()
    elif a==6:arrange()
    else:break


with open('./result.txt',mode='w') as f:
    
    for y,x in enumerate(class1):
        f.write(str(x.id)+',')
        f.write(str(x.name)+',')
        f.write(str(x.gender)+',')
        f.write(str(x.math)+',')
        f.write(str(x.english)+',')
        f.write(str(x.ave)+',')
        f.write(str(x.ranking())+'\n')
       