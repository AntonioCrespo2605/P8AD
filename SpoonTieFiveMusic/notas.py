import xml.etree.ElementTree as ET
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename

ventana=Tk()


cont=0

def hideWidget():
    global cont
    print(cont)
    cont+=1

b=Button(
    ventana,
    width=1,
    height=1,
    background="black",
    text="hola",
    command=hideWidget
)

b.grid(column=0, row=0)



ventana.mainloop()

