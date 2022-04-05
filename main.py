from tkinter import *
from tkinter import ttk
window = Tk()

window.geometry("800x400+10+20")
window.title("Main GUI")

button = Button (window, text = "Button", fg = "red", font = ("Verdana", 16))
button.place(x=103, y=50)

label = Label (window, text = "This is a label", fg = "blue", bg = "orange")
label.place(x=40, y=120)

txtfld = Entry (window, text = "This is a text field", bd = 5)
txtfld.place(x=130, y=118)

v1 = IntVar()
radiobutton = Radiobutton (window, text = "Male",variable = v1, value = 1)
radiobutton1 = Radiobutton (window, text = "Female",variable = v1, value = 2)
radiobutton.place(x=40, y=170)
radiobutton1.place(x=40, y=150)

v2 = StringVar()
v2.set('Student 1')
data = "Student 1", "Student 2", "Student 3"
combo = ttk.Combobox (window, values = data)
combo.place(x=130, y=250)

data = "Student 1", "Student 2", "Student 3"
lb = Listbox (window, height = 5, selectmode = "single")
for num in data:
    lb.insert(END, num)
lb.place(x=130, y=150)


window.mainloop()
