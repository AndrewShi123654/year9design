from tkinter import *
master = Tk()
master.config(background="red")
label = Label(master, text="hockey pool")
label.config(background="purple")
label.config(foreground="white")
label.pack()
button=Button(master,text="QUIT", fg="orange",command=quit)
button.pack(side=BOTTOM)
listbox=Listbox(master)
listbox.config(background="green")
listbox.config(foreground="blue")
listbox.pack()
listbox.insert()(END,"player,Goals")
lst = [["conner mcdavid",208],["sidney crosby",234],["steven stamkos",187],["austain mathues"],70]
for item in lst:
    listbox.insert(END, ite,[0] + "-" + str(item[1]))

mainloop()