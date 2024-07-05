from tkinter import *
import tkinter as tk
from mor3 import Database
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
print(data["sno"])
print(data["id"])
print(data["name"])
print(data["position"])
print(data["in"])
print(data["out"])
print(data["status"])




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
   if status[i] is 1:
      column.append("present")
   elif status[i] is 0:
      column.append("left")
   elif status[i] is -1:
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
    window.geometry("700x250")
    root.destroy()
    label = Label(window, text="now you edit the datas")
    label.pack()
    

    def add():
        label = Label(window)
        label.pack()
    
        window1 = tk.Tk()
        window1.geometry("700x250")

    button=Button(window,text="add", command= add)
    button.pack()

  







button=Button(root,text="edit", command= onclick)   
button.pack()



root.mainloop()

    






