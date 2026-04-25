from tkinter import *


tk = Tk()
tk.title("Account Creator")
tk.geometry("400x400")

frame = Frame(master=tk,height=200, width=360, bg="#6ac2bc")

lbl_1=Label(frame, text="Enter your Birth Year",bg="#1d75f5",fg="#ffffff")
lbl_2=Label(frame, text="Enter Current Year",bg="#1d75f5",fg="#ffffff")


birth_year_entry=Entry(frame)
modern_year_entry=Entry(frame)


def display():
    birth = birth_year_entry.get()
    modern = modern_year_entry.get()
    app_age = int(modern) - int(birth)
    message = "You are approximately "+str(app_age)+" years old."

    text_box.insert(END, message)


text_box = Text(bg="#1d75f5",fg="#ffffff",height=10,width=50)
btn = Button(text="Calculate",command=display, bg="#1d75f5",fg="#000000" )

frame.place(x=20,y=0)
lbl_1.place(x=20,y=20)
birth_year_entry.place(x=150,y=20)
lbl_2.place(x=20,y=80)
modern_year_entry.place(x=150,y=80)
btn.place(x=150,y=200)
text_box.place(x=20,y=240)

tk.mainloop()


