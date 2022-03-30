from tkinter import*
import math

foablak = Tk()

def szamitas():
    r = int(sugarb.get())
    m = int(magasg.get())
    mennyiseg = math.pi * r * r * m
    mennyib.delete(0, END)
    mennyib.insert(0, str(terfogat)+ 'cm³')

    sugar = round (7.874 * terfogat, 2)
    sugarg.delete (0, END)
    sugarg.insert (0, str(vassuruseg))

    magassag = round (0.65 * terfogat, 2)
    magasg.delete (0, END)
    magasg.insert (0, str(fasuruseg))
    
foablak.geometry('550x550')
kep = PhotoImage(file = 'C:\\Users\\vargaczgergo\\Desktop\\IKT-tkinterVG\\boroshordo.gif')
foablak.iconphoto(True, kep)

mennyiseg = Label(foablak, text= 'Bor mennyisége:')
mennyiseg.grid(column = 1, row = 1)
mennyib = Entry(foablak)
mennyib.grid(column = 2, row = 1, columnspan = 2)

sugar= Label(foablak, text= 'Hordó sugara:')
sugar.grid(column = 1, row = 2)
sugarg = Entry(foablak)
sugarg.grid(column = 2, row = 2, columnspan = 2)

magassag = Label(foablak, text= 'Hordó magassága:')
magassag.grid(column = 1, row = 3)
magasg = Entry(foablak)
magasg.grid(column = 2, row = 3, columnspan = 2)

gomb1 = Button(foablak, text = 'kiszámítás')
gomb1.grid(column = 3, row = 4)


foablak.mainloop()