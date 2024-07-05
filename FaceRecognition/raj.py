
from tkinter import *
import tkinter as tk
from mor3 import Database
from tkinter import messagebox
db=Database()

root = tk.Tk()
root.title("project")
root.geometry("1400x700")


label = Label(root,text="admine data base")
label.pack()

table_frame = tk.Frame(root)
table_frame.pack()

labels = []



data=db.employee_fetch()
#print(data["sno"])
#print(data["id"])
#print(data["name"])
#print(data["position"])
#print(data["in"])
#print(data["out"])
#print(data["status"])




sno=data["sno"]
id_=data["id"]
name=data["name"]
position=data["position"]
in_=data["in"]
out=data["out"]
status=data["status"]





for i in range(len(id_)):
   row_labels = []
   column=[]
   column.append(sno[i])
   column.append(id_[i])
   column.append(name[i])
   column.append(position[i])
   column.append(in_[i])
   column.append(out[i])
   if int(status[i]) == 1:
      column.append("present")
   elif int(status[i]) == 0:
      column.append("left")
   elif int(status[i]) == -1:
      column.append("absent")
   for j in range(7):
   # Create a label for each cell in the table
      label = tk.Label(table_frame, text=str(column[j]))
      label.grid(row=i, column=j, padx=10, pady=10) # Position the label in the table  
      row_labels.append(label)
   labels.append(row_labels)


def onclick():
    label = Label(root)
    label.pack()

    
    window = tk.Tk()
    window.title("EDIT")
    window.geometry("1400x700")
    root.destroy()
    label = Label(window, text="now you edit the datas")
    label.pack()
    

    def add():
        label = Label(window)
        label.pack()
    
        window1 = tk.Tk()
        window1.geometry("700x250")
        
        label = Label(window1,text="name")
        label.pack()
        
        input_1= Entry(window1,width=10)
        input_1.pack()
        
        label = Label(window1,text="position")
        label.pack()
        
        input_2= Entry(window1,width=10)
        input_2.pack()
            
                
        def add1(in1,in2):
            newid=db.employee_add(str(in1),str(in2))
            button["state"]="disable"
            messagebox.showinfo("New Employee added","New Employee id ---> "+str(newid)+"\nName ---> "+str(in1)+"\nPosition ---> "+str(in2))
            label=Label(window1,text="New Employee id ---> "+str(newid))
            label.pack()
           
            
        button=Button(window1,text="add employee", command= lambda:add1(input_1.get(),input_2.get()))

        button.pack()

    button=Button(window,text="add", command= add)

    button.pack()
    def remove():
        label = Label(window)
        label.pack()
    
        window1 = tk.Tk()
        window1.geometry("700x250")
        window1.title("project")
        window1.geometry("1400x700")
        label = Label(window1,text="emp_id")
        
        label.pack()
        input_= Entry(window1,width=10)
        input_.pack()
        def show():
            id_,pos=db.employee_details(input_.get())         
            label=Label(window1,text="Name: "+str(id_)+"\nPosition: "+str(pos))
            label.pack()
            button['state']="active"
        def remove():
           if db.employee_disable(input_.get()):
              messagebox.showinfo("Employee Removed","Employee "+str (input_.get())+" is now disabled")
        button=Button(window1,text="show",command=lambda:show())
        button.pack()
        
        button=Button(window1,text="remove",command=lambda:remove())
        button.pack()
        button['state']="disabled"


    button=Button(window,text="remove", command= remove)

    button.pack()
    def changeposition():
        label = Label(window)
        label.pack()
    
        window1 = tk.Tk()
        window1.geometry("700x250")
        #root.title("project")
        window1.geometry("1400x700")
        label = Label(window1,text="emp_id")
        
        label.pack()
        input_1= Entry(window1,width=10)
        input_1.pack()
        def show():
            id_,pos=db.employee_details(input_1.get())      
            label=Label(window1,text="Name: "+str(input_1.get())+"\nPosition: "+str(pos))
            label.pack()
            button['state']="active"
        def update():
           if db.employee_update(input_1,input_2):
              messagebox.showinfo("Employee Position Updated","Employee "+input_1.get()+" is now "+input_2.get())
        button=Button(window1,text="show",command=lambda:show())
        button.pack()
        label = Label(window1,text="emp_id")
        
        label.pack()
        input_2= Entry(window1,width=10)
        input_2.pack()
        
        button=Button(window1,text="update",command=lambda:update())
        button.pack()
        button['state']="disabled"

    button=Button(window,text="changeposition", command= changeposition)

    button.pack()



  








button=Button(root,text="edit", command= onclick)   
button.pack()



root.mainloop()

    






