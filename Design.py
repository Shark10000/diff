from tkinter import *
from getlist import diffeq
diffeq = diffeq()

def buttonpress(equat):
    answer = diffeq.simple(equat)
    ls2 = Label(frame, text=answer, font='Times 25')
    ls2.pack()


window = Tk()
window.title("Калькулятор дифференциальных уравнений")
window.geometry('500x400')
frame = Frame(window)
entry = Entry(frame, font='Times 25')
lbl = Label(frame, text="Введите сюда уравнение", font='Times 25')
solbutton = Button(frame, text="Ok", font='Times 20')
solbutton.bind('<Button-1>', lambda e, f="": buttonpress(entry.get()))

#всё пакуется
frame.pack()
lbl.pack()
entry.pack()
solbutton.pack()

#открытие окна
window.mainloop()
