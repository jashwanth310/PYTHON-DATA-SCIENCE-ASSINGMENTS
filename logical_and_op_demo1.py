from tkinter import*
from tkinter import messagebox
#tkinter is the module used to
#create GUI
#initialize window
window=Tk()
window.geometry("450x250")
window.config(bg="white")
window.title("Email VALIDATION")
#user defined functions
def email_validation():
    email_id = e1.get()
    password = e2.get()
    remail_id = "alladi@gmail.com"
    rpassword = "12345"
    if (email_id == remail_id and  password == rpassword):
        messagebox.showinfo("REPORT","HEY BOY! its U")
    else:
         messagebox.showinfo("REPORT", "OOPS! GET LOST")

#lable1:email id
l1=Label(window,text="email id:",font=40)
l1.grid(row=0,column=0)
#entry box
e1=Entry(window)
e1.grid(row=0,column=1)
#lable2:password
l2=Label(window,text="password:",font=40)
l2.grid(row=1,column=0)
#entry box
e2=Entry(window)
e2.grid(row=1,column=1)
#Button:
b1=Button(window,text="press me",command=email_validation)
b1.grid(row=2,column=1)

window.mainloop()
