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
app_icon=PhotoImage(file="src/proyect_images/icono.png")
wndw.iconphoto(True,app_icon)
wndw.geometry("870x1000")

#Images
icon_new = PhotoImage(file = "src/proyect_images/anhadirverde2.png")
icon_change_green=PhotoImage(file = "src/proyect_images/cambiarverde2.png")
icon_cd=PhotoImage(file = "src/proyect_images/disco.png")
arrow_icon=PhotoImage(file = "src/proyect_images/flecha.png")
arrowLeft_icon=PhotoImage(file="src/proyect_images/flechaizq.png")
delete_icon=PhotoImage(file="src/proyect_images/borrar.png")
electronic_icon=PhotoImage(file="src/proyect_images/e.png")
electronic_black=PhotoImage(file="src/proyect_images/ebn.png")
rock_icon=PhotoImage(file="src/proyect_images/r.png")
rock_black=PhotoImage(file="src/proyect_images/rbn.png")
jazz_icon=PhotoImage(file="src/proyect_images/jazz.png")
jazz_black=PhotoImage(file="src/proyect_images/jazzbn.png")
pop_icon=PhotoImage(file="src/proyect_images/pop.png")
pop_black=PhotoImage(file="src/proyect_images/popbn.png")
classic_icon=PhotoImage(file="src/proyect_images/clasica.png")
classic_black=PhotoImage(file="src/proyect_images/clasicabn.png")
reggaeton_icon=PhotoImage(file="src/proyect_images/reggaeton.png")
reggaeton_black=PhotoImage(file="src/proyect_images/reggaetonbn.png")
trap_icon=PhotoImage(file="src/proyect_images/trap.png")
trap_black=PhotoImage(file="src/proyect_images/trapbn.png")
other_icon=PhotoImage(file="src/proyect_images/otros.png")
other_black=PhotoImage(file="src/proyect_images/otrosbn.png")
add_artist_icon=PhotoImage(file="src/proyect_images/nuevoartista2.png")

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
        text="añadir disco",
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
        global electronic_black, rock_black, jazz_black, pop_black, classic_black, reggaeton_black, trap_black, other_black, add_artist_icon

        #add album main interface
        newAlbumwndw = Toplevel(wndw)
        newAlbumwndw.title("Crea aquí tu nuevo disco!!!")
        newAlbumwndw.geometry("870x870")
        newAlbumwndw['bg']='black'
        
        #
        Label(
                newAlbumwndw,
                text="A",
                font="Verdana 100",
                background="black",
                fg="black"
        ).grid(row=0, column=0)

        Label(
                newAlbumwndw,
                text="Crea tu nuevo disco",
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

        inputname = Text(newAlbumwndw,
                        height = 1,
                        width = 15,
                        font="Verdana 30"
                        )
  
        inputname.grid(row=1, column=2, columnspan=3, pady=10, padx=10, sticky="w")

        Label(
                newAlbumwndw,
                text="Artista :",
                font="Verdana 20",
                background="black",
                fg="#00bf36"
        ).grid(row=2, column=1)

        Label(
                newAlbumwndw,
                text="Artistas :",
                font="Verdana 20",
                background="black",
                fg="#00bf36"
        ).grid(row=3, column=1, pady=15)

        artists=Label(
                newAlbumwndw,
                font="Verdana 20",
                background="black",
                fg="#00bf36"
        )

        artists.grid(row=3, column=2, columnspan=3)

        inputartist = Text(newAlbumwndw,
                        height = 1,
                        width = 10,
                        font="Verdana 30"
                        )
  
        inputartist.grid(row=2, column=2, columnspan=2, pady=10, padx=10, sticky="w")

        add_artist=Button(
                newAlbumwndw,
                width=30,
                height=30,
                image=add_artist_icon,
                background="black"
        )

        add_artist.grid(row=2, column=4)

        Label(
                newAlbumwndw,
                text="Géneros :",
                font="Verdana 20",
                background="black",
                fg="#00bf36"
        ).grid(row=4, column=1, pady=15)

        bok=Button(
                newAlbumwndw,
                text="Crear",
                font="Verdana 20",
                background="#00bf36"
        ).grid(row=7, column=1)

        Button(
                newAlbumwndw,
                text="Cancelar",
                font="Verdana 20",
                background="grey",
                command= lambda: newAlbumwndw.destroy()
        ).grid(row=7, column=4, pady=15)


        #genres buttons and names
        bElectronic=Button(
                newAlbumwndw,
                background="black",
                width=100,
                height=100,
                image=electronic_black
        )
        bElectronic.grid(column=1, row=5, pady=30, padx=15)

        Label(
                newAlbumwndw,
                background="black",
                text="Electrónica",
                fg="#00bf36",
                font="Verdana 10"
        ).grid(column=1, row=5, sticky="s", pady=20)

        bRock=Button(
                newAlbumwndw,
                background="black",
                width=100,
                height=100,
                image=rock_black
        )
        bRock.grid(column=2, row=5, padx=15)

        Label(
                newAlbumwndw,
                background="black",
                text="Rock",
                fg="#00bf36",
                font="Verdana 10"
        ).grid(column=2, row=5, sticky="s", pady=20)

        bJazz=Button(
                newAlbumwndw,
                background="black",
                width=100,
                height=100,
                image=jazz_black
        )
        bJazz.grid(column=3, row=5, padx=15)

        Label(
                newAlbumwndw,
                background="black",
                text="Jazz",
                fg="#00bf36",
                font="Verdana 10"
        ).grid(column=3, row=5, sticky="s", pady=20)

        bPop=Button(
                newAlbumwndw,
                background="black",
                width=100,
                height=100,
                image=pop_black
        )
        bPop.grid(column=4, row=5, padx=15)

        Label(
                newAlbumwndw,
                background="black",
                text="Pop",
                fg="#00bf36",
                font="Verdana 10"
        ).grid(column=4, row=5, sticky="s", pady=20)

        bClassic=Button(
                newAlbumwndw,
                background="black",
                width=100,
                height=100,
                image=classic_black
        )
        bClassic.grid(column=1, row=6, padx=15, pady=15)

        Label(
                newAlbumwndw,
                background="black",
                text="Clásica",
                fg="#00bf36",
                font="Verdana 10"
        ).grid(column=1, row=6, sticky="s")

        bReggaeton=Button(
                newAlbumwndw,
                background="black",
                width=100,
                height=100,
                image=reggaeton_black
        )
        bReggaeton.grid(column=2, row=6, padx=15)

        Label(
                newAlbumwndw,
                background="black",
                text="Reggaeton",
                fg="#00bf36",
                font="Verdana 10"
        ).grid(column=2, row=6, sticky="s")

        bTrap=Button(
                newAlbumwndw,
                background="black",
                width=100,
                height=100,
                image=trap_black
        )
        bTrap.grid(column=3, row=6, padx=15)

        Label(
                newAlbumwndw,
                background="black",
                text="Trap",
                fg="#00bf36",
                font="Verdana 10"
        ).grid(column=3, row=6, sticky="s")

        bOthers=Button(
                newAlbumwndw,
                background="black",
                width=100,
                height=100,
                image=other_black
        )
        bOthers.grid(column=4, row=6, padx=15)

        Label(
                newAlbumwndw,
                background="black",
                text="Otros",
                fg="#00bf36",
                font="Verdana 10"
        ).grid(column=4, row=6, sticky="s")

        genres_selected={}
        genres_selected["electronic"]=[False]
        genres_selected["rock"]=[False]
        genres_selected["jazz"]=[False]
        genres_selected["pop"]=[False]
        genres_selected["classic"]=[False]
        genres_selected["reggaeton"]=[False]
        genres_selected["trap"]=[False]
        genres_selected["others"]=[False]

        #functions
        artistsnames={}
        def addArtistToList():
                add_artist

        def select_deselect(key):
                
                global electronic_icon, electronic_black, rock_icon, rock_black, jazz_icon, jazz_black, pop_icon, pop_black, classic_icon, classic_black, reggaeton_icon, reggaeton_black, trap_icon, trap_black, other_icon, other_black
                if(genres_selected[key]==True):
                        if(key=="electronic"):
                                bElectronic.configure(image=electronic_black)
                                genres_selected[key]=False
                        elif(key=="rock"):
                                bRock.configure(image=rock_black)
                                genres_selected[key]=False
                        elif(key=="pop"):
                                bPop.configure(image=pop_black)
                                genres_selected[key]=False
                        elif(key=="jazz"):
                                bJazz.configure(image=jazz_black)
                                genres_selected[key]=False
                        elif(key=="classic"):
                                bClassic.configure(image=classic_black)
                                genres_selected[key]=False
                        elif(key=="reggaeton"):
                                bReggaeton.configure(image=reggaeton_black)
                                genres_selected[key]=False
                        elif(key=="trap"):
                                bTrap.configure(image=trap_black)
                                genres_selected[key]=False
                        elif(key=="others"):
                                bOthers.configure(image=other_black)
                                genres_selected[key]=False                                                        
                else:
                        if(key=="electronic"):
                                bElectronic.configure(image=electronic_icon)
                                genres_selected[key]=True        
                        elif(key=="rock"):
                                bRock.configure(image=rock_icon)
                                genres_selected[key]=True
                        elif(key=="pop"):
                                bPop.configure(image=pop_icon)
                                genres_selected[key]=True
                        elif(key=="jazz"):
                                bJazz.configure(image=jazz_icon)
                                genres_selected[key]=True
                        elif(key=="classic"):
                                bClassic.configure(image=classic_icon)
                                genres_selected[key]=True
                        elif(key=="reggaeton"):
                                bReggaeton.configure(image=reggaeton_icon)
                                genres_selected[key]=True
                        elif(key=="trap"):
                                bTrap.configure(image=trap_icon)
                                genres_selected[key]=True
                        elif(key=="others"):
                                bOthers.configure(image=other_icon)
                                genres_selected[key]=True 
        
        bElectronic.configure(command= lambda : select_deselect("electronic"))
        bRock.configure(command= lambda: select_deselect("rock"))
        bPop.configure(command= lambda: select_deselect("pop"))
        bJazz.configure(command= lambda: select_deselect("jazz"))
        bClassic.configure(command= lambda: select_deselect("classic"))
        bReggaeton.configure(command= lambda: select_deselect("reggaeton"))
        bTrap.configure(command= lambda: select_deselect("trap"))
        bOthers.configure(command= lambda: select_deselect("others"))                        




l1newdisk.configure(command=windowNewAlbum)    


wndw.mainloop()