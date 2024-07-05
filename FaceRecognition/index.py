import tkinter as tk
from tkinter import messagebox

from tkinter import *
import tkinter as tk

# Import Module
from tkinter import *
from PIL import Image, ImageTk


def admin_button_clicked():
    entered_password = password_entry.get()
    if entered_password == "mor3":
        #messagebox.showinfo("🔐 Admin Access Granted", "Welcome...mor3!")
        root.destroy()
        import raj
        
        
    else:
        messagebox.showwarning("🚫 Access Denied", "Incorrect password. Try again.")
def camera_button_clicked():
    #camera_button['state'] = 'disable'
    #camera_button['text'] = 'Opening...'
    camera_button['bg'] = 'white'  
    camera_button['fg'] = '#2d4c54'
    #messagebox.showinfo("📷 Camera Activated", "opening camera...")
    root.destroy()
    import new_camera
    #carmera run

 #main window
root = tk.Tk()
root.title("MORcube Admin Page")
root.geometry("1400x700")
root.configure(bg="#2d4c54")

#widgets styling admin
frame = tk.Frame(root, bg="#54a19c", bd=5, relief=tk.GROOVE)
frame.place(relx=0.2, rely=0.6, anchor="center")
password_label = tk.Label(frame, text="🔒 Enter Password:", bg="#54a19c", fg="white", font=("Arial", 18))
password_label.pack(pady=(20, 10))
password_entry = tk.Entry(frame, show="*", bg="white", fg="black", font=("Arial", 16), bd=3)
password_entry.pack(pady=10)
admin_button = tk.Button(frame, text="Admin 🔐", fg="white", bg="#2d4c54", command=admin_button_clicked, font=("Arial", 16, "bold"), bd=3)
admin_button.pack(pady=15)

#widgets styling camara
frame = tk.Frame(root, bg="#54a19c", bd=5, relief=tk.GROOVE)
frame.place(relx=0.8, rely=0.6, anchor="center")
attendence_label = tk.Label(frame, text="For attendence", bg="#54a19c", fg="white", font=("Arial", 18))
attendence_label.pack(pady=(20, 4))
attendence_label = tk.Label(frame, text= " 📷 ", bg="#54a19c", fg="white", font=("Arial", 30))
attendence_label.pack(pady=(25,5 ))
camera_button = tk.Button(frame, text="Activate Camera now ", fg="white", bg="#2d4c54", command=camera_button_clicked, font=("Arial", 16, "bold"), bd=3)
camera_button.pack(pady=15)

# title l
frame = tk.Frame(root, bg="white", bd=5, relief=tk.GROOVE)
frame.place(relx=0.3, rely=0.2, anchor="center")
password_label = tk.Label(frame, text="Welcome to MOR cube", bg="white", fg="deepskyblue", font=("Arial", 18))
password_label.pack(pady=(20, 10))

# title 2
frame = tk.Frame(root, bg="white", bd=5, relief=tk.GROOVE)
frame.place(relx=0.7, rely=0.2, anchor="center")
password_label = tk.Label(frame, text=" Attendence Rigestration", bg="white", fg="deepskyblue", font=("Arial", 18))
password_label.pack(pady=(20, 10))

# Create Tkinter Object00000

# Read the Image
image = Image.open("C:\\Users\\okesh\\OneDrive\Desktop\\FaceRecognition\\logo.jpg")

# Resize the image using resize() method
resize_image = image.resize((260,260))

img = ImageTk.PhotoImage(resize_image)

# create label and add resize image
label1 = Label(image=img,width= 260, height= 260, anchor= E )
label1.image = img
label1.pack()

# Execute Tkinter
#root.mainloop()



#run tkinte4r main loop
root.mainloop()
