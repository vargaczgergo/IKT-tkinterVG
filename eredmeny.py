from tkinter import*
ablak1 = Tk()
ablak1.title('A téglatest adatai')
ablak1.minsize(width = 300, height = 100)

def ujablak():
    abl2 = Toplevel(ablak1)
    abl2.title('Eredmények')
    abl2.minsize(width = 300, height = 100)

    sz1 = Label(abl2, text = 'Felszín: ')
    sz2 = Label(abl2, text = 'Térfogat: ')
    m1 = Entry(abl2)
    m2 = Entry(abl2)

    sz1.grid(row = 1)
    sz2.grid(row = 2)
    m1.grid(row = 1, column = 2, sticky = W)
    m2.grid(row = 2, column = 2, sticky = W)

    a = eval(mezo1.get())
    b = eval(mezo1.get())
    c = eval(mezo1.get())

    felszin = 2*(a*b+a*c+b*c)
    terfogat = a*b*c

    m1.delete(0, END)
    m1.insert(0, str(felszin))
    m2.delete(0, END)
    m2.insert(0, str(terfogat))
    
    abl2.mainloop()

szoveg1 = Label(ablak1, text = 'a:')
szoveg2 = Label(ablak1, text = 'b:')
szoveg3 = Label(ablak1, text = 'c:')
gomb1 = Button(ablak1, text = 'Számítás', command = ujablak)
mezo1 = Entry(ablak1)
mezo2 = Entry(ablak1)
mezo3 = Entry(ablak1)

szoveg1.grid(row = 1)
szoveg2.grid(row = 2)
szoveg3.grid(row = 3)
gomb1.grid(row = 4, column = 2, sticky = W)
mezo1.grid(row = 1, column = 2, sticky = W)
mezo2.grid(row = 2, column = 2, sticky = W)
mezo3.grid(row = 3, column = 2, sticky = W)

ablak1.mainloop()


    