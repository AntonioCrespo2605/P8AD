import xml.etree.ElementTree as ET
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import datetime
import os

#needed variables
page=0
visibleDisks=[0,1,2,3,4,5]

#xml file
filename="MusicaXML/audioteca.xml"

#main window configuration
wndw=Tk()
wndw['bg']="black"
wndw.title("SpoonTieFive")
app_icon=PhotoImage(file="src/icono.png")
wndw.iconphoto(True,app_icon)
wndw.geometry("870x1000")

#Images
icon_new = PhotoImage(file = "src/anhadirverde2.png")
icon_change_green=PhotoImage(file = "src/cambiarverde2.png")
icon_cd=PhotoImage(file = "src/disco.png")
arrow_icon=PhotoImage(file = "src/flecha.png")
arrowLeft_icon=PhotoImage(file="src/flechaizq.png")
delete_icon=PhotoImage(file="src/borrar.png")
electronic_icon=PhotoImage(file="src/e.png")

#Basic Labels and Buttons
l1newdisk=Button(wndw,
        image=icon_new,
        background="black",
        width=60,
        height=60)
l1newdisk.grid(row=0, column=0)

l2=Label(wndw,
        text="Spoon Tie Five",
        font="Verdana 40",
        background="black",
        fg="#00bf36").grid(row=0, column=1, columnspan=2, rowspan=2, padx=100) 

l3xml=Button(wndw,
        image=icon_change_green,
        background="black",
        width=60,
        height=60)
l3xml.grid(row=0, column=3)

l4file=Label(wndw,
        text="fichero: audioteca.xml",
        font="Verdana 15",
        background="black",
        fg="#00bf36")
l4file.grid(row=2, column=1, columnspan=2, sticky="s")        

l4_2=Label(
        wndw,
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
        wndw,
        text="a",
        fg="black",
        background="black",
        height=4
).grid(row=3, column=0, columnspan=4)

#functions
def limitname(disknameaux):#returns a cuted string if it is too long 
        diskname=""
        for i in range(9):
                if i<len(disknameaux):diskname+=disknameaux[i]
        return diskname        

#root for xml
tree = ET.parse(filename)
root=tree.getroot()

#DISKS INTERFACE
numDisks=len(root)
list_d=[]
list_n=[]
list_p=[]
nrow=4
ncolumn=1
for i in range(6):
        d=Button(
                wndw,
                image=icon_cd,
                width=150,
                height=150
        )

        n=Label(
                wndw,
                font="Verdana 15"
        )

        p=Button(
                wndw,
                image=delete_icon,
                width=20,
                height=20,
                background="black"
        )

        list_d.append(d)
        list_n.append(n)
        list_p.append(p)        
        if(numDisks>=i+1):
                if(i%2==0):
                        list_d[i].grid(row=nrow, column=ncolumn, sticky="e", padx=15, pady=15)
                        list_p[i].grid(row=nrow, column=ncolumn, sticky="ne", pady=15, padx=15)
                else:
                        list_d[i].grid(row=nrow, column=ncolumn, sticky="w", padx=15, pady=15)
                        list_p[i].grid(row=nrow, column=ncolumn, sticky="nw",padx=15, pady=15)
                        
                name=limitname(root[i].attrib["nombre"])
                list_n[i].configure(text=name)
                list_n[i].grid(row=nrow, column=ncolumn, sticky="s")

                if(i%2==1):
                        ncolumn=1
                        nrow+=1
                else:
                        ncolumn=2

#creating right and left arrows
arrowR=Button(
        wndw,
        image=arrow_icon,
        width=30,
        height=30,
        background="white"
)

arrowL=Button(
        wndw,
        image=arrowLeft_icon,
        width=30,
        height=30,
        background="white"
)

#more functions
def changeDisksView():
        global root, page, numDisks, list_d, list_n, list_p, visibleDisks
        position=page*6
        visibleDisks=[page, page+1, page+2, page+3, page+4, page+5]

        nrow=4
        ncolumn=1
        for i in range(6):
                if(position+1<=numDisks):
                        if(i%2==0):
                                list_d[i].grid(row=nrow, column=ncolumn, sticky="e", padx=15, pady=15)
                                list_p[i].grid(row=nrow, column=ncolumn, sticky="ne", pady=15, padx=15)
                        else:
                                list_d[i].grid(row=nrow, column=ncolumn, sticky="w", padx=15, pady=15)
                                list_p[i].grid(row=nrow, column=ncolumn, sticky="nw",padx=15, pady=15)       
                        list_n[i].grid(row=nrow, column=ncolumn, sticky="s")

                        list_n[i].config(
                                text=limitname(root[position].attrib["nombre"])
                        )
                else:
                        list_p[i].grid_forget()
                        list_n[i].grid_forget()
                        list_d[i].grid_forget()

                if(i%2==1):
                        ncolumn=1
                        nrow+=1
                else:
                        ncolumn=2        
                position+=1                


def showDisksRight():
        global arrowR
        global arrowL
        global page
        page+=1
        lastDiskOfGroup=(page*6)+5
        
        if(numDisks<=lastDiskOfGroup+1):
                arrowR.grid_forget()
        arrowL.grid(row=7, column=1)
        changeDisksView()

def showDisksLeft():
        global arrowR
        global arrowL
        global page
        page-=1
        if(page==0):
                arrowL.grid_forget()
        arrowR.grid(row=7, column=2)
        changeDisksView()

#arrows configuration
if(numDisks>6):
        arrowR.config(command=showDisksRight)
        arrowR.grid(row=7, column=2)
        arrowL.config(command=showDisksLeft)
        spaceaux=Label(
                wndw,
                background="black",
                text=" ",
                fg="white",
                height=10
        ).grid(row=7, column=0)

#function for updating disks
def changeXML():
        global root, tree, filename, numDisks, page, arrowR, l4file
        lastfilename=filename
        first_page()
        filename=filedialog.askopenfilename(title = "Select file",filetypes = (("XML Files","*.xml"),))
        if(len(filename)<4):
                filename=lastfilename
        tree = ET.parse(filename)
        root=tree.getroot()
        f=open(filename, 'r')
        l4file.configure(text="fichero: "+os.path.basename(f.name))
        numDisks=len(root)
        page=0
        if(numDisks>6):
                arrowR.grid(row=7, column=2)
        else:
                arrowR.grid_forget
        changeDisksView()                

#returns to the first page to avoid bugs
def first_page():
        global arrowL, page, numDisks, arrowR
        arrowL.grid_forget()
        page=0
        if numDisks>6:
                arrowR.grid(row=7, column=2)
        else:
                arrowR.grid_forget()        
        changeDisksView()

#adding the command to the xml button
l3xml.configure(
        command=changeXML
)

#obtain current year for using as default year on the disks
currentDateTime = datetime.datetime.now()
date = currentDateTime.date()
year = date.strftime("%Y")

#creates a new window asking the information about the new album
def windowNewAlbum():
        #images
        global electronic_icon

        newAlbumwndw = Toplevel(wndw)
        newAlbumwndw.title("Crea aquí tu nuevo disco!!!")
        newAlbumwndw.geometry("870x870")
        newAlbumwndw['bg']='black'
        
        Label(
                newAlbumwndw,
                text="A",
                font="Verdana 100",
                background="black",
                fg="black"
        ).grid(row=0, column=0)

        Label(
                newAlbumwndw,
                text="Crea tu nuevo álbum",
                font="Verdana 40",
                background="black",
                fg="#00bf36"  
        ).grid(row=0, column=1, columnspan=4)
        
        Label(
                newAlbumwndw,
                text="Nombre :",
                font="Verdana 20",
                background="black",
                fg="#00bf36"
        ).grid(row=1, column=1)

        Label(
                newAlbumwndw,
                text="Artista :",
                font="Verdana 20",
                background="black",
                fg="#00bf36"
        ).grid(row=2, column=1)

        Label(
                newAlbumwndw,
                text="Géneros :",
                font="Verdana 20",
                background="black",
                fg="#00bf36"
        ).grid(row=3, column=1)

        bok=Button(
                newAlbumwndw,
                text="Crear",
                font="Verdana 20",
                background="#00bf36"
        ).grid(row=6, column=1)

        bCancel=Button(
                newAlbumwndw,
                text="Cancelar",
                font="Verdana 20",
                background="grey"
        ).grid(row=6, column=4)

        #genres
        bElectronic=Button(
                newAlbumwndw,
                background="black",
                width=100,
                height=100,
                image=electronic_icon
        ).grid(column=1, row=4)

        bRock=Button(
                newAlbumwndw,
                background="black",
                width=100,
                height=100,
                image=electronic_icon
        ).grid(column=2, row=4)

        bJazz=Button(
                newAlbumwndw,
                background="black",
                width=100,
                height=100,
                image=electronic_icon
        ).grid(column=3, row=4)

        bPop=Button(
                newAlbumwndw,
                background="black",
                width=100,
                height=100,
                image=electronic_icon
        ).grid(column=4, row=4)

        bClassic=Button(
                newAlbumwndw,
                background="black",
                width=100,
                height=100,
                image=electronic_icon
        ).grid(column=1, row=5)

        bReggaeton=Button(
                newAlbumwndw,
                background="black",
                width=100,
                height=100,
                image=electronic_icon
        ).grid(column=2, row=5)

        bTrap=Button(
                newAlbumwndw,
                background="black",
                width=100,
                height=100,
                image=electronic_icon
        ).grid(column=3, row=5)

        bOthers=Button(
                newAlbumwndw,
                background="black",
                width=100,
                height=100,
                image=electronic_icon
        ).grid(column=4, row=5)

l1newdisk.configure(command=windowNewAlbum)    


wndw.mainloop()