from tkinter import *
import pyautogui
def pencere_ac():
    acilan_pencere = Toplevel()
    baslik = Label(acilan_pencere,text="Ana pencereden Açılan pencere")
    baslik.pack()

if __name__ == '__main__':
    ana_pencere = Tk()

    buton1 = Button(ana_pencere, text="giriş",command=pencere_ac)
    buton1.pack()
    mainloop()