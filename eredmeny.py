from tkinter import*

abl1 = Tk()
abl1.title('A téglatest adatai')
abl1.minsize(width=300, height = 100)

def ujablak():
    abl2 = Toplevel(abl1)
    abl2.title('Eredmények')
    abl2.minsize(width = 300, height = 100)

    sz1 = Label(abl2, text = 'Felszín:')
    sz2 = Label(abl2, text = 'Térfogat:')
    m1 = Entry(abl2)
    m2 = Entry(abl2)

    sz1.grid(row =1)
    sz2.grid(row =2)
    sz1.grid(row =1, column =2, sticky = W)
    sz2.grid(row =2, column =2, sticky = W)

    a = eval(mezo1.get())
    b = eval(mezo2.get())
    c = eval(mezo3.get())

    felszin = 2*(a*b+a*c+b*c)
    terfogat = a*b*c

    m1.delete(0,END)
    m1.insert(0,str(felszin))
    m2.delete(0,END)
    m2.insert(0,str(terfogat))

    abl2.mainloop()
    