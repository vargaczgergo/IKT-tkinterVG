from tkinter import*


foablak = Tk()



foablak.geometry('550x550')
foablak.title('hordó')
vaszon=Canvas(foablak, width=160, height=160, bg='white')
kep = PhotoImage(file = 'C:\\Users\\vargaczgergo\\Desktop\\IKT-tkinterVG\\hordo.png')

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