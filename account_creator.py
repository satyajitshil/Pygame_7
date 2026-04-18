from tkinter import *

tk = Tk()
tk.title("Account Creator")
tk.geometry("400x400")

frame = Frame(master=tk,height=200, width=360, bg="#6ac2bc")

lbl_1=Label(frame, text="Enter your Full Name",bg="#1d75f5",fg="#ffffff")
lbl_2=Label(frame, text="Enter you Gmail",bg="#1d75f5",fg="#ffffff")
lbl_3=Label(frame, text="Enter your Password",bg="#1d75f5",fg="#ffffff")

name_entry=Entry(frame)
mail_entry=Entry(frame)
pass_entry=Entry(frame,show="*")

def display():
    name = name_entry.get()
    greet = "Hey "+name+"\n"
    message = "Thank you for creating an account."

    text_box.insert(END, greet)
    text_box.insert(END, message)

text_box = Text(bg="#1d75f5",fg="#ffffff",height=10,width=50)
btn = Button(text="Sign Up",command=display, bg="#1d75f5",fg="#000000" )

frame.place(x=20,y=0)
lbl_1.place(x=20,y=20)
name_entry.place(x=150,y=20)
lbl_2.place(x=20,y=80)
mail_entry.place(x=150,y=80)
lbl_3.place(x=20,y=140)
pass_entry.place(x=150,y=140)
btn.place(x=150,y=200)
text_box.place(x=20,y=240)

tk.mainloop()
