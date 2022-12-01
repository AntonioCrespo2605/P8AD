import xml.etree.ElementTree as ET
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilenames

#needed variables
page=0

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
arrowLeft_icon=PhotoImage(file="src/flechaizq.png")

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
        fg="#00bf36")
l4.grid(row=2, column=1, columnspan=2, sticky="s")        

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
        fg="#949494")
l5.grid(row=1, column=0)         

l6=Label(wndw,
        text="cambiar xml",
        font="Verdana 15",
        background="black",
        fg="#949494")
l6.grid(row=1, column=3)                       

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
        list_d.append(d)
        list_n.append(n)        
        if(numDisks>=i+1):
                if(i%2==0):
                        list_d[i].grid(row=nrow, column=ncolumn, sticky="e", padx=15, pady=15)
                else:
                        list_d[i].grid(row=nrow, column=ncolumn, sticky="w", padx=15, pady=15)
                name=limitname(root[i].attrib["nombre"])
                list_n[i].grid(row=nrow, column=ncolumn, sticky="s")
                list_n[i].configure(text=name)

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
        global root
        global page
        global numDisks
        global list_d
        global list_n
        position=page*6
        
        nrow=4
        ncolumn=1
        for i in range(6):
                if(position+1<=numDisks):
                        if(i%2==0):
                                list_d[i].grid(row=nrow, column=ncolumn, sticky="e", padx=15, pady=15)
                        else:
                                list_d[i].grid(row=nrow, column=ncolumn, sticky="w", padx=15, pady=15)       
                        list_n[i].grid(row=nrow, column=ncolumn, sticky="s")

                        list_n[i].config(
                                text=limitname(root[position].attrib["nombre"])
                        )
                else:
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



 

wndw.mainloop()


  


