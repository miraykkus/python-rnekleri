from tkinter import *

window = Tk()
window.title("merhaba")
lbl = Label(window, text="merhaba")
lbl.grid(column=0, row=0)
window.geometry('500x400')

#buton ekleme
btn = Button(window, text="tikla")
btn.grid(column=1, row=1)

def tiklandi():
    lbl.configure(text="tiklandi") #butona tıklayınca çalışcak fonk


btn2 = Button(window, text="tikla", bg="purple", command=tiklandi) #renkli buton ve tıklayınca fonk çalıştırma
btn2.grid(column=1, row=3)


window.mainloop()