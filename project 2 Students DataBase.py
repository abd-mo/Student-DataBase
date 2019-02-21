# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 22:22:56 2018

@author: abdelrahman
"""


import tkinter as tk
import sqlite3


class body():
    Number=0  
    def __init__(self,Name='',sur_name='',Student_id=0,university='',Faculty='',Department='',grade=0,Phone=0,gpa=0,mail=0):
        body.Number+=1
        #new_st.img=image
        self.name=Name
        self.surname=sur_name
        self.StudentId=Student_id
        self.uni=university
        self.fact=Faculty
        self.dep=Department
        self.mob=Phone
        self.email=mail
        self.GPA=gpa
        self.grade=grade
        
#initaliz main page        
    def main(self):
        interface=tk.Tk()
        interface.geometry('600x250+300+300')
        interface.title("Student Database ")
        tk.Button(text='add new student',width = 25,height=2,command=lambda:newStudent.new_student()).place(x=10,y=30)
        tk.Button(text='View student',width = 25,height=2,command=lambda:ViewStudent.view_student()).place(x=10,y=80)
        tk.Button(text='Delete student',width = 25,height=2,command=lambda:DeletStudent.delete_student()).place(x=10,y=130)
        tk.Button(text='Clear DataBase',width = 25,height=2,command=lambda:ClearData.clear_DataBase()).place(x=10,y=180)

      
        tk.Button(text='Exit',width = 15,command=lambda:interface.destroy()).place(x=470,y=215)
        interface.mainloop()
                
#create data base      
    def DB(self,x,y=''):
        db = sqlite3.connect('data_base.db')
        cursor = db.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS 
             Student_inf(name text,surname text,ID int,uni text,faculty text,Dep text,grade int,GPA FLOAT,mob int,mail text)''')
        cursor.execute(x,y)
        db.commit()
        db.close()
        
#create the add functionn        
    def new_student(self):
        new_st=tk.Tk()
        new_st.geometry('550x600+600+200')
        new_st.title('new student')
        tk.Label(new_st,text="Name:").place(x=20,y=150)
        E1=new_st.entry = tk.Entry(new_st,width=30)
        E1.place(x=90,y=150)
        tk.Label(new_st,text="Surname:").place(x=20,y=190)
        E2=new_st.entry = tk.Entry(new_st,width=30)
        E2.place(x=90,y=190)
        tk.Label(new_st,text="StudentID:").place(x=20,y=230)
        E3=new_st.entry = tk.Entry(new_st,width=30)
        E3.place(x=90,y=230)
        tk.Label(new_st,text="University:").place(x=20,y=270)
        E4=new_st.entry = tk.Entry(new_st,width=30)
        E4.place(x=90,y=270)
        tk.Label(new_st,text="Faculty:").place(x=20,y=310)
        E5=new_st.entry = tk.Entry(new_st,width=30)
        E5.place(x=90,y=310)
        tk.Label(new_st,text="Department:").place(x=20,y=350)
        E6=new_st.entry = tk.Entry(new_st,width=30)
        E6.place(x=90,y=350)
        tk.Label(new_st,text="Grade:").place(x=20,y=390)
        E7=new_st.entry = tk.Entry(new_st,width=30)
        E7.place(x=90,y=390)
        tk.Label(new_st,text="GPA:").place(x=20,y=430)
        E8=new_st.entry = tk.Entry(new_st,width=30)
        E8.place(x=90,y=430)
        tk.Label(new_st,text="Phone:").place(x=20,y=470)
        E9=new_st.entry = tk.Entry(new_st,width=30)
        E9.place(x=90,y=470)
        tk.Label(new_st,text="E-mail:").place(x=20,y=510)
        E10=new_st.entry = tk.Entry(new_st,width=30)
        E10.place(x=90,y=510)
        tk.Label(new_st,text="Add New Student",font='"bold" 30',fg="indian red").place(x=110,y=30)
        tk.Label(new_st,text="------------------------------------",font='"bold" 30 ').place(x=45,y=70)
        def func():
             newOne=body(E1.get(),E2.get(),E3.get(),E4.get(),E5.get(),E6.get(),E7.get(),E8.get(),E9.get(),E10.get())
             data_base.DB("INSERT INTO Student_inf VALUES (?,?,?,?,?,?,?,?,?,?)",(newOne.name,newOne.surname,newOne.StudentId,newOne.uni,newOne.fact,newOne.dep,newOne.grade,newOne.GPA,newOne.mob,newOne.email))  
        tk.Button(new_st, text="Add Student",command=lambda:func()).place(x=450,y=550)
        tk.Button(new_st, text="  main  ",command=lambda:new_st.destroy()).place(x=380,y=550)
        new_st.mainloop()
        
        
#create the delete function 
       
    def delete_student(self):
             delete =tk.Tk()
             delete.geometry('600x250')
             delete.title("delete student")
             mystring =tk.StringVar(delete)
             def del_data():
                 
                  data_base.DB("delete from Student_inf where ID= '%d' " % int(mystring.get()))
#                  
             tk.Label(delete,text="Enter Student ID ",font='"bold" 20').place(x=30,y=30) 
             tk.Button(delete,text='main',width = 15,command=lambda:delete.destroy()).place(x=470,y=210)
             tk.Entry(delete,textvariable = mystring,width=30,bd=3,selectbackground='blue').place(x=30,y=80)
             tk.Button(delete, text='delete', height = 1, width = 10,command=del_data).place(x=140,y=120)
             delete.mainloop()
             
                        
#Initialize the clear function            
    def clear_DataBase(self):
            clear_Data=tk.Tk()
            clear_Data.geometry('400x150+300+300')
            clear_Data.title('warring')
            tk.Label(clear_Data,text="Are you sure to clear all your data!!",font='"bold" 15',fg="indian red").place(x=20,y=50)
            def apply():
                   data_base.DB("delete from Student_inf ")
                   clear_Data.destroy()
            def close():
                  clear_Data.destroy()
            clear_Data.button = tk.Button(clear_Data, text="clear",command=lambda:apply()).place(x=350,y=100)
            clear_Data.button = tk.Button(clear_Data, text="cancel",command=lambda:close()).place(x=300,y=100)
            clear_Data.mainloop()
            
            
#create the view function          
    def view_student(self):
            StudentV=body()
    
            view =tk.Tk()
            view.geometry('600x250')
            view.title("update student")
            mystring =tk.StringVar(view)
            def data(z):
                 import tkinter as tk
                 import sqlite3
                 db=sqlite3.connect("data_base.db")
                 cursor = db.cursor()

                 sql = "SELECT * FROM Student_inf \
                       WHERE  ID = '%d'" % int(z)
                 try:
                    cursor.execute(sql)
                    results = cursor.fetchall()
                    for row in results:
                           StudentV.name =row[0]
                           StudentV.surname = row[1]
                           StudentV.StudentId = row[2]
                           StudentV.uni = row[3]
                           StudentV.fact = row[4]
                           StudentV.dep = row[5]
                           StudentV.grade = row[6]
                           StudentV.GPA = row[7]
                           StudentV.mob= row[8]
                           StudentV.email = row[9]

                    print("name=%s,surname=%s,ID=%d,uni=%s,factulty=%s,dep=%s,grade=%d,gpa=%d,mob=%d,mail=%s" % \
                         (StudentV.name, StudentV.surname,StudentV.StudentId, StudentV.uni, StudentV.fact, StudentV.dep,StudentV.grade ,StudentV.GPA ,StudentV.mob ,StudentV.email))
                    new=tk.Tk()
                    new.geometry('550x600+600+200')
                    new.title('new student')
                 
                    tk.Label(new,text="Student Information",font='"bold" 30',fg="indian red").place(x=110,y=30)
                    tk.Label(new,text="------------------------------------",font='"bold" 30 ').place(x=45,y=70)
                    tk.Label(new,text="Name:",fg="indian red",font='10').place(x=20,y=150)
                    tk.Label(new,text=StudentV.name,font='"bold" 12',).place(x=90,y=150)
                    
                    tk.Label(new,text="Surname:",fg="indian red",font='10').place(x=20,y=190)
                    tk.Label(new,text=StudentV.surname,font='"bold" 12',).place(x=90,y=190)
                    
                    tk.Label(new,text="Student Id:",fg="indian red",font='10').place(x=20,y=230)
                    tk.Label(new,text=StudentV.StudentId,font='"bold" 12').place(x=110,y=230)
                    
                    tk.Label(new,text="University:",fg="indian red",font='10').place(x=20,y=270)
    
                    tk.Label(new,text=StudentV.uni,font='"bold" 12',).place(x=110,y=270)
                    tk.Label(new,text="Faculty:",fg="indian red",font='10').place(x=20,y=310)

                    tk.Label(new,text=StudentV.fact,font='"bold" 12').place(x=110,y=310)
                    tk.Label(new,text="Department:",fg="indian red",font='10').place(x=20,y=350)
      
                    tk.Label(new,text=StudentV.dep,font='"bold" 12').place(x=110,y=350)
                    tk.Label(new,text="Grade:",fg="indian red",font='10').place(x=20,y=390)
    
                    tk.Label(new,text=StudentV.grade,font='"bold" 12').place(x=90,y=390)
                    tk.Label(new,text="GPA:",fg="indian red",font='10').place(x=20,y=430)
 
                    tk.Label(new,text=StudentV.GPA,font='"bold" 12').place(x=90,y=430)
                    tk.Label(new,text="Phone:",fg="indian red",font='10').place(x=20,y=470)
      
                    tk.Label(new,text=StudentV.mob,font='"bold" 12',).place(x=90,y=470)
                    tk.Label(new,text="E-mail:",fg="indian red",font='10').place(x=20,y=510)
                    tk.Label(new,text=StudentV.email,font='"bold" 12 ').place(x=90,y=510)
                    new.button = tk.Button(new, text=" exite ",command=lambda:new.destroy()).place(x=380,y=550)
                    new.mainloop()
                 except:

                      print ("Error!!")
                 db.close() 
            
                       
            tk.Label(view,text='Enter Student ID',font='"bold" 20').place(x=30,y=30)     
            tk.Entry(view,textvariable = mystring,width=30,bd=3,selectbackground='blue').place(x=30,y=80)
            tk.Button(view,text='view',width=10,command=lambda:data(mystring.get())).place(x=140,y=120)
            tk.Button(view,text='main',width=15,command=lambda:view.destroy()).place(x=470,y=210)
        
            view.mainloop()
    
#intialize data base
data_base=body()            
#add a new student
newStudent=body()
#delete student
DeletStudent=body()
#clear data base
ClearData=body()
#view student
ViewStudent=body()
#start program
Start=body()
Start.main()















        
