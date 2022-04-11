from tkinter import *
from tkinter import ttk
window=Tk()
window.title('Midterm in OOP')
window.geometry("500x200+10+10")

def fullname():
    name['text'] = 'myname'

label = Label(text='Enter your full name:', fg='purple')
label.place(x=60, y=70)

button = Button(text='Click to display your full name', fg='green', command=fullname)
button.place(x=60, y=145)

entername = Entry(textvariable='myname', bd='5')
entername.place(x=265, y=65)

name = Entry(text='This is my full name', bd='5')
name.place(x=265, y=145)


window.mainloop()