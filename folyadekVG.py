from tkinter import*
import math


def szamitas ():
    if len(sugarg.get()) == 0 or len(magasg.get()) == 0 or len(mennyib.get()) == 0 or type(sugarg.get()) != int or type(magasg()) != int or type(mennyib.get()) != int:
        beleg.delete (0, END)
        beleg.insert (0, 'Nem fér bele a bor' )
        telitettg.delete (0,END)
        telitettg.insert (0, 'Nem fér bele a bor' )
        terfogatb.delete (0,END)
        terfogatb.insert (0, 'Nem fér bele a bor' )

    r = int(sugarg.get())
    m = int(magasg.get())
    borl = int(mennyib.get())
    meg = 0
    telitet = 0

    if borl <= 0 or r <= 0 or m <= 0:
        beleg.delete (0, END)
        beleg.insert (0, 'Nem szükséges kiszámítani' )
        telitettg.delete (0,END)
        telitettg.insert (0, 'Nem szükséges kiszámítani' )
        terfogatb.delete (0,END)
        terfogatb.insert (0, 'Nem szükséges kiszámítani' )
    else:

        terfogat = round (math.pi * r * r * m * 0.001)
        terfogatb.delete (0, END)
        terfogatb.insert (0, str(terfogat)+' l' )

        meg = terfogat - borl
        telitet = round (borl * (100 / terfogat))

        if borl > terfogat:
            beleg.delete (0, END)
            beleg.insert (0, 'Túl kicsi a hordó.' )
            telitettg.delete (0,END)
            telitettg.insert (0, 'Túl kicsi a hordó.' )
        else:
            beleg.delete (0, END)
            beleg.insert (0, str(meg)+' l')
            telitettg.delete (0, END)
            telitettg.insert (0, str(telitet)+' %')

foablak = Tk()
gyoker = 'C:\\Users\\Gergő\\Desktop\\IKT-tkinterVG\\folyadekVG.py'

img = PhotoImage(file= gyoker + "boroshordo.gif")
foablak.iconphoto(True, img)

mennyiseg = Label(foablak, text= 'Bor mennyisége(l):')
mennyiseg.grid(column = 1, row = 1)
mennyib = Entry(foablak)
mennyib.grid(column = 2, row = 1, columnspan = 2)

sugar= Label(foablak, text= 'Hordó sugár(r):')
sugar.grid(column = 1, row = 2)
sugarg = Entry(foablak)
sugarg.grid(column = 2, row = 2, columnspan = 2)

magassag = Label(foablak, text= 'Hordó magasság(dm):')
magassag.grid(column = 1, row = 3)
magasg = Entry(foablak)
magasg.grid(column = 2, row = 3, columnspan = 2)


terfogat = Label(foablak, text= 'Ennyi a hordó kapacitása(l): ')
terfogat.grid(column = 1, row = 5)
terfogatb = Entry(foablak)
terfogatb.grid(column = 2, row = 5, columnspan = 2)

bele= Label(foablak, text= 'Ennyi fér még bele(l):')
bele.grid(column = 1, row = 6)
beleg = Entry(foablak)
beleg.grid(column = 2, row = 6, columnspan = 2)

telitett = Label(foablak, text= 'Ennyi százalékig van a hordó:')
telitett.grid(column = 1, row = 7)
telitettg = Entry(foablak)
telitettg.grid(column = 2, row = 7, columnspan = 2)

gomb1 = Button(foablak, text = 'Számítás', command = szamitas)
gomb1.grid(column = 3, row = 4)


foablak.mainloop()