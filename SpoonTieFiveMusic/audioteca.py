import xml.etree.ElementTree as ET
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilenames

#needed variables
pages=1

#xml file
filename="MusicaXML/audioteca.xml"

#main window configuration
wndw=Tk()
wndw['bg']="black"
wndw.title("SpoonTieFive")
icono=PhotoImage(file="src/icono.png")
wndw.iconphoto(True,icono)
wndw.geometry("870x1000")

#Images
icon_new = PhotoImage(file = "src/anhadirverde2.png")
icon_change_green=PhotoImage(file = "src/cambiarverde2.png")
icon_cd=PhotoImage(file = "src/disco.png")
arrow_icon=PhotoImage(file = "src/flecha.png")

#Basic Labels and Buttons
l1=Button(wndw,
        image=icon_new,
        background="black",
        width=60,
        height=60).grid(row=0, column=0)

l2=Label(wndw,
        text="Spoon Tie Five",
        font="Verdana 40",
        background="black",
        fg="#00bf36").grid(row=0, column=1, columnspan=2, rowspan=2, padx=100) 

l3=Button(wndw,
        image=icon_change_green,
        background="black",
        width=60,
        height=60).grid(row=0, column=3)

l4=Label(wndw,
        text="fichero: cambiar en codigo",
        font="Verdana 15",
        background="black",
        fg="#00bf36").grid(row=2, column=1, columnspan=2, sticky="s")

l4_2=Label(
        text="a",
        font="Verdana 15",
        background="black",
        fg="black",
        height=3
).grid(row=2, column=0 )

l5=Label(wndw,
        text="añadir album",
        font="Verdana 15",
        background="black",
        fg="#949494").grid(row=1, column=0) 

l6=Label(wndw,
        text="cambiar xml",
        font="Verdana 15",
        background="black",
        fg="#949494").grid(row=1, column=3)               

l7=Label(
        text="a",
        fg="black",
        background="black",
        height=4
).grid(row=3, column=0, columnspan=4)

#functions


#root for xml
tree = ET.parse(filename)
root=tree.getroot()

#disks interface
#first disk space:
numDisks=len(root)


d1=Button(
        image=icon_cd,
        width=150,
        height=150
).grid(row=4, column=1, sticky="e", padx=15, pady=10)

n1=Label(

).grid(row=4, column=1, sticky="s")
#second disk interface:
d2=Button(
        image=icon_cd,
        width=150,
        height=150
).grid(row=4, column=2, sticky="w", padx=15, pady=10)

n2=Label(

).grid(row=4, column=2, sticky="s")
#third disk interface:
d3=Button(
        image=icon_cd,
        width=150,
        height=150
).grid(row=5, column=1, sticky="e", padx=15, pady=10)

n3=Label(
        
).grid(row=5, column=1, sticky="s")
#fourth disk space:
d4=Button(
        image=icon_cd,
        width=150,
        height=150
).grid(row=5, column=2, sticky="w", padx=15, pady=10)

n4=Label(

).grid(row=5, column=2, sticky="s")
#fifth disk interface:
d5=Button(
        image=icon_cd,
        width=150,
        height=150
).grid(row=6, column=1, sticky="e", padx=15, pady=10)

n5=Label(

).grid(row=6, column=1, sticky="s")
#sixth disk interface:
d6=Button(
        image=icon_cd,
        width=150,
        height=150
).grid(row=6, column=2, sticky="w", padx=15, pady=10)

n6=Label(

).grid(row=6, column=2, sticky="s")

#right arrow configuration
if(len(root)>6):
        flecha=Button(
                image=arrow_icon,
                width=30,
                height=30,
                background="white"
        ).grid(row=7, column=2)

        spaceaux=Label(
                background="black",
                text=" ",
                fg="white",
                height=10
        ).grid(row=7, column=1)



 

wndw.mainloop()


  


