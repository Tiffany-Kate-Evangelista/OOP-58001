from tkinter import *
window = Tk()
window.geometry("450x300+20+10")
window.title("The Grid Manager")
ent1 = Entry(window, bd = 3, justify = "center", bg = "#a1fc03")
ent1.grid(row = 0, column = 0)
ent1.insert(0,"row 0, column 0")

ent2 = Entry(window, bd = 3, justify = "center", bg = "#a1fc03")
ent2.grid(row = 0, column = 1)
ent2.insert(0,"row 0, column 1")

ent3 = Entry(window, bd = 3, justify = "center", bg = "#a1fc03")
ent3.grid(row = 0, column = 2)
ent3.insert(0,"row 0, column 2")

ent4 = Entry(window, bd = 3, justify = "center", bg = "#53d41c")
ent4.grid(row = 1, column = 0)
ent4.insert(0,"row 1, column 0")

ent5 = Entry(window, bd = 3, justify = "center", bg = "#53d41c")
ent5.grid(row = 1, column = 1)
ent5.insert(0,"row 1, column 1")

ent6 = Entry(window, bd = 3, justify = "center", bg = "#53d41c")
ent6.grid(row = 1, column = 2)
ent6.insert(0,"row 1, column 2")

ent7 = Entry(window, bd = 3, justify = "center", bg = "#3fb827")
ent7.grid(row = 2, column = 0)
ent7.insert(0,"row 2, column 0")

ent8 = Entry(window, bd = 3, justify = "center", bg = "#3fb827")
ent8.grid(row = 2, column = 1)
ent8.insert(0,"row 2, column 1")

ent9 = Entry(window, bd = 3, justify = "center", bg = "#3fb827")
ent9.grid(row = 2, column = 2)
ent9.insert(0,"row 2, column 2")

ent10 = Entry(window, bd = 3, justify = "center", bg = "#419630")
ent10.grid(row = 3, column = 1, columnspan = 1)
ent10.insert(0,"row 3, column 1")

yscroll = Scrollbar(window, orient = VERTICAL)
yscroll.grid(row = 5, column = 2, rowspan = 4, padx = (0, 100), pady = 5, sticky = NS)

datalist = ["Student 1", "Student 2", "Student 3", "Student 4", "Student 5", "Student 6", "Student 7", "Student 8", "Student 9", "Student 10", "Student 11", "Student 12","Student 13",]
var = StringVar()

lb = Listbox(window, fg = "white", bg = "#3e7034", listvariable = var, width = 15, height = 6, yscrollcommand = yscroll.set)
lb.grid(row = 5, column = 1, padx = (100, 0), pady = 5, sticky = E)
var.set(tuple(datalist))
yscroll["command"] = lb.yview()


window.mainloop()