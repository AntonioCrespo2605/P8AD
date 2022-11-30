import xml.etree.ElementTree as ET
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename

cadena="hola"
print(cadena[5])

filename = askopenfilename(filetypes=[("XML", ".xml")])
if(filename==""):
    filename="MusicaXML/audioteca.xml"
tree = ET.parse(filename)

audioteca_raiz=tree.getroot()

#MOSTRAR DISCOS
def mostrar_discos(audioteca_raiz):
    for child in audioteca_raiz:
        print(child.attrib["nombre"])

#MOSTRAR CANCIONES EN FUNCION AL DISCO
def mostrar_canciones(audioteca_raiz):
    cont=0
    for child in audioteca_raiz:
        print(str(cont)+"-"+child.attrib["nombre"])
        cont+=1
    print("escribe pos")
    pos=int(input())
    
    for child in audioteca_raiz[pos]:
        for subchild in child:
            print(subchild.attrib["nombre"])
            
#BORRAR DISCO
def borrar_disco(tree, audioteca_raiz, filename):
    cont=0
    for child in audioteca_raiz:
        print(str(cont)+"-"+child.attrib["nombre"])
        cont+=1
    print("escribe pos")
    pos=int(input())

    cont=0
    for child in audioteca_raiz:
        if(cont==pos):
            audioteca_raiz.remove(child)
        cont+=1
    
    tree.write(filename)

#MENU
repeat=True
while repeat:
    repeat=True

    print("1-Mostrar discos\n2-Mostar canciones de un disco\n3-borrar disco\n4-salir")
    op=int(input())

    if(op==1):
        mostrar_discos(audioteca_raiz)
    elif(op==2):
        mostrar_canciones(audioteca_raiz)
    elif(op==3):
        borrar_disco(tree, audioteca_raiz, filename)
    elif(op==4):
        repeat=False    
    else:
        print("opcion desconocida")



"""
l8=Button(
        image=icon_cd,
        width=150,
        height=150
).grid(row=4,column=1, padx=10, pady=10, sticky="e")

l9=Label(
        text="disco1",
        font="Verdana 15",
        fg="black",
        background="white"
).grid(row=4,column=1, sticky="s")

l10=Button(
        image=icon_cd,
        width=150,
        height=150
).grid(row=4,column=2, padx=10, pady=10, sticky="w")

l11=Label(
        text="disco2",
        font="Verdana 15",
        fg="black",
        background="white"
).grid(row=4,column=2, sticky="s")
"""
  
"""
cont=0#the cont is used to know the position of the disk in the root
for child in root:
        if(cont<6):
                c=(cont%2)+1#if the cont is pair the disk must be in the first column. Else it must be in the second
                
                if cont%2==0:
                        r=(cont/2)+4
                else:
                        r=((cont-1)/2)+4        
                disknameaux=child.attrib["nombre"]
                
                diskname=""
                for i in range(9):
                        if i<len(disknameaux):diskname+=disknameaux[i]


                Button(
                        image=icon_cd,
                        width=150,
                        height=150
                ).grid(row=int(r), column=int(c), padx=10, pady=10, sticky="e")

                Label(
                        text=diskname,
                        font="Verdana 15",
                        fg="black",
                        background="white"
                ).grid(row=int(r), column=int(c), sticky="s")
        
        cont+=1
        if(cont>5):
                break;
"""

