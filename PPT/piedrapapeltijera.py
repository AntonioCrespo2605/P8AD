import tkinter as tkt 
from tkinter import *
import random

ventana = tkt.Tk()
ventana.title("Piedra Papel Tiijera")
ventana.geometry("1500x1000")
ventana['bg']='pink'

Label(ventana,
      text = "Piedra Papel Tijera",
      font = "Verdana 30 italic bold",
      fg = "black",
      background="pink"
      ).pack(pady=30)   

piedra = PhotoImage(file = "imagenesPiedraPapelTijera/piedra.png")
papel = PhotoImage(file = "imagenesPiedraPapelTijera/papel.png")
tijera = PhotoImage(file = "imagenesPiedraPapelTijera/tijera.png")

Label(ventana,
      text = "Escoje una opción:",
      font = "verdana 15 italic",
      fg = "black",
      background="pink"
      ).pack(pady = 30)

frame = Frame(ventana)
frame.pack()

contmaq=0
cont=0

posibles={
      0:"piedra",
      1:"papel",
      2:"tijera"
}  
#functions
def isPiedra():
    elec = posibles[random.randint(0, 2)]
    if elec == "papel":
        contmaq=contmaq+1
        lres.config(image=papel) 
    elif elec=="tijera":
        cont=cont+1
        lres.config(image=tijera) 
    else :
        lres.config(image=piedra) 

def isPapel():
    elec = posibles[str(random.randint(0, 2))]
    if elec == "tijera":
        contmaq=contmaq+1
    elif elec=="piedra":
        cont=cont+1

def isTijera():
    elec = posibles[str(random.randint(0, 2))]
    if elec == "piedra":
        contmaq=contmaq+1
    elif elec=="papel":
        cont=cont+1


#Buttons
l1 = Button(frame,
           image = piedra,
           command = isPiedra
           )

l1['bg']="pink"           
 
l2 = Button(frame,
           image = papel,
           command = isPapel
           )

l2['bg']="pink"           
 
l3 = Button(frame, 
           image = tijera,
           command=isTijera
           )

l3['bg']="pink"

l1.pack(side = LEFT)
l2.pack(side = LEFT)
l3.pack(side = LEFT)

frame2=Frame(ventana)
frame2['bg']="pink"

frame2.pack()

l4 = Label(
      frame2,
      text="Tus victorias:",
      font="verdana 15 italic",
      background="pink"
)


l5 = Label(
      frame2,
      font = "verdana 15 italic",
      text = "                     La máquina ha elegido:        ",
      fg = "black",
      background="pink"
)

l6 = Label(
      frame2,
      font = "verdana 15 italic",
      text="Victorias de la máquina:",
      background="pink"
)

l4.pack(side = LEFT, pady=30)
l5.pack(side = LEFT, pady=30)
l6.pack(side = LEFT, pady=30)

frame3=Frame(ventana)
frame3['bg']="pink"
frame3.pack()


nada = PhotoImage(file = "imagenesPiedraPapelTijera/nada.png")
lpuntprop=Label(
      frame3,
      text=str(cont)+"   ",
      font="verdana 100",
      background="pink"
)
lres=Label(
      frame3,
      image=nada,
      background="pink"
)

lpuntmaq=Label(
      frame3,
      text="   "+str(contmaq),
      font="verdana 100",
      background="pink"
)
lpuntprop.pack(side = LEFT)
lres.pack(side = LEFT)
lpuntmaq.pack(side = LEFT)








ventana.mainloop()
