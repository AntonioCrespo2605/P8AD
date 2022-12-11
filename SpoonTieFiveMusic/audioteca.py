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
edit_icon=PhotoImage(file="src/proyect_images/editarpeque.png")
more_artists_icon=PhotoImage(file="src/proyect_images/tresp.png")
more_songs_icon=PhotoImage(file="src/proyect_images/mas.png")

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
                arrowR.grid_forget()
        changeDisksView()                

#reads againg the xml file
def readXML():
        global tree, root, numDisks
        tree = ET.parse(filename)
        root=tree.getroot()
        numDisks=len(root)

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

"""
Disco Creator interface and code:
***********************************************************************************************************************************************
"""
#creates a new window asking the information about the new album
def windowNewAlbum():

        #images
        global electronic_black, rock_black, jazz_black, pop_black, classic_black, reggaeton_black, trap_black, other_black, add_artist_icon

        #add album main interface
        newAlbumwndw = Toplevel(wndw)
        newAlbumwndw.title("Crea aquí tu nuevo disco!!!")
        newAlbumwndw.geometry("840x900")
        newAlbumwndw['bg']='black'
        
        #labels and texts
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

        artists.grid(row=3, column=2, columnspan=3, sticky="w")

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
                text="Año :",
                font="Verdana 20",
                background="black",
                fg="#00bf36"
        ).grid(row=4, column=1, pady=15)

        inputyear = Text(newAlbumwndw,
                        height = 1,
                        width = 10,
                        font="Verdana 30"
                        )
        inputyear.grid(row=4, column=2, columnspan=2, sticky="w")                

        Label(
                newAlbumwndw,
                text="Géneros :",
                font="Verdana 20",
                background="black",
                fg="#00bf36"
        ).grid(row=5, column=1, pady=15)

        #Ok adn Cancel buttons
        bok=Button(
                newAlbumwndw,
                text="Crear",
                font="Verdana 20",
                background="#00bf36"
        )
        bok.grid(row=8, column=1)

        Button(
                newAlbumwndw,
                text="Cancelar",
                font="Verdana 20",
                background="grey",
                command= lambda: newAlbumwndw.destroy()
        ).grid(row=8, column=4, pady=15)


        #genres buttons and names
        bElectronic=Button(
                newAlbumwndw,
                background="black",
                width=100,
                height=100,
                image=electronic_black
        )
        bElectronic.grid(column=1, row=6, pady=30, padx=15)

        Label(
                newAlbumwndw,
                background="black",
                text="Electrónica",
                fg="#00bf36",
                font="Verdana 10"
        ).grid(column=1, row=6, sticky="s", pady=20)

        bRock=Button(
                newAlbumwndw,
                background="black",
                width=100,
                height=100,
                image=rock_black
        )
        bRock.grid(column=2, row=6, padx=15)

        Label(
                newAlbumwndw,
                background="black",
                text="Rock",
                fg="#00bf36",
                font="Verdana 10"
        ).grid(column=2, row=6, sticky="s", pady=20)

        bJazz=Button(
                newAlbumwndw,
                background="black",
                width=100,
                height=100,
                image=jazz_black
        )
        bJazz.grid(column=3, row=6, padx=15)

        Label(
                newAlbumwndw,
                background="black",
                text="Jazz",
                fg="#00bf36",
                font="Verdana 10"
        ).grid(column=3, row=6, sticky="s", pady=20)

        bPop=Button(
                newAlbumwndw,
                background="black",
                width=100,
                height=100,
                image=pop_black
        )
        bPop.grid(column=4, row=6, padx=15)

        Label(
                newAlbumwndw,
                background="black",
                text="Pop",
                fg="#00bf36",
                font="Verdana 10"
        ).grid(column=4, row=6, sticky="s", pady=20)

        bClassic=Button(
                newAlbumwndw,
                background="black",
                width=100,
                height=100,
                image=classic_black
        )
        bClassic.grid(column=1, row=7, padx=15, pady=15)

        Label(
                newAlbumwndw,
                background="black",
                text="Clásica",
                fg="#00bf36",
                font="Verdana 10"
        ).grid(column=1, row=7, sticky="s")

        bReggaeton=Button(
                newAlbumwndw,
                background="black",
                width=100,
                height=100,
                image=reggaeton_black
        )
        bReggaeton.grid(column=2, row=7, padx=15)

        Label(
                newAlbumwndw,
                background="black",
                text="Reggaeton",
                fg="#00bf36",
                font="Verdana 10"
        ).grid(column=2, row=7, sticky="s")

        bTrap=Button(
                newAlbumwndw,
                background="black",
                width=100,
                height=100,
                image=trap_black
        )
        bTrap.grid(column=3, row=7, padx=15)

        Label(
                newAlbumwndw,
                background="black",
                text="Trap",
                fg="#00bf36",
                font="Verdana 10"
        ).grid(column=3, row=7, sticky="s")

        bOthers=Button(
                newAlbumwndw,
                background="black",
                width=100,
                height=100,
                image=other_black
        )
        bOthers.grid(column=4, row=7, padx=15)

        Label(
                newAlbumwndw,
                background="black",
                text="Otros",
                fg="#00bf36",
                font="Verdana 10"
        ).grid(column=4, row=7, sticky="s")

        #this is used for knowing which genres has been selected
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

        #when the add_button is clicked it gets the text in the artist input box and add it to the list
        #it also cut the artists String if it is too long
        artistsnames=[]
        def addArtistToList():
                current_artist=inputartist.get("1.0", "end-1c").strip()
                if(current_artist != ''):
                        artistsnames.append(current_artist)

                artists_in_format=''
                cont=1
                for art in artistsnames:
                        artists_in_format+=art
                        if(cont!=len(artistsnames)):
                                artists_in_format+=', '
                        cont+=1

                
                if(len(artists_in_format)>20):
                        artists_in_format_aux=''
                        for x in range(17):
                                artists_in_format_aux+=artists_in_format[x]
                        artists_in_format_aux+='...'
                        artists_in_format=artists_in_format_aux

                artists.configure(text=artists_in_format)                

        #calling the last function in the add_artist button
        add_artist.config(command=addArtistToList)

        #changes the genres images alternating between bright and dark for each one
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
        
        #calling the select_deselect function for each genre button
        bElectronic.configure(command= lambda : select_deselect("electronic"))
        bRock.configure(command= lambda: select_deselect("rock"))
        bPop.configure(command= lambda: select_deselect("pop"))
        bJazz.configure(command= lambda: select_deselect("jazz"))
        bClassic.configure(command= lambda: select_deselect("classic"))
        bReggaeton.configure(command= lambda: select_deselect("reggaeton"))
        bTrap.configure(command= lambda: select_deselect("trap"))
        bOthers.configure(command= lambda: select_deselect("others"))

        #it opens a new window with errors 
        def errorWindow(message):
                errorwndw = Toplevel(newAlbumwndw)
                errorwndw.title("ERROR")
                errorwndw.geometry("870x250")
                errorwndw['bg']='black'
                Label(
                        errorwndw,
                        text="Se han detectado los siguientes errores:",
                        font="Verdana 25",
                        background="black",
                        fg="red"
                ).grid(row=0, column=0)

                Label(
                        errorwndw,
                        text=message,
                        font="Verdana 12",
                        background="black",
                        fg="white"
                ).grid(row=1, column=0)

                Button(
                        errorwndw,
                        text="Aceptar",
                        background="#00bf36",
                        command= lambda: errorwndw.destroy()
                ).grid(row=2, column=0, pady=20)

        def successfullDisk():
                readXML()
                first_page()
                changeDisksView()
                swndw = Toplevel(newAlbumwndw)
                swndw.title("Creado con éxito")
                swndw.geometry("580x300")
                swndw['bg']='black'
                Label(
                        swndw,
                        text="Tu disco se ha creado con éxito:",
                        font="Verdana 25",
                        background="black",
                        fg="#00bf36"
                ).grid(row=0, column=0)

                Label(
                        swndw,
                        text="Puedes empezar a añadir canciones a \ntu disco desde el menú principal",
                        font="Verdana 12",
                        background="black",
                        fg="#00bf36"
                ).grid(row=1, column=0, pady=40)

                Button(
                        swndw,
                        text="Aceptar",
                        background="#00bf36",
                        command= lambda: swndw.destroy()
                ).grid(row=2, column=0, pady=20)

        #obtaining current Year
        currentDateTime = datetime.datetime.now()
        date = currentDateTime.date()
        year = date.strftime("%Y")

        #when the create button is clicked it checks all the data and creates a new disk in the xml
        def diskCreator():
                allOk=True
                errorMessage=''
                if(len(artistsnames)==0):
                        errorMessage+="\n*El nuevo disco tiene que tener algún artista asociado."
                        allOk=False

                year_aux=inputyear.get("1.0", "end-1c")        
                
                if(year_aux.isnumeric()):
                        if(int(year_aux)>int(year) or int(year_aux)<0 ):
                                errorMessage+="\n*El año debe ser un entero entre 0 y "+str(year)
                else:
                        errorMessage+="\n*El año no se corresponde con un número entero. Comprueba que se trata de un entero entre 0 y "+str(year)
                        allOk=False                

                disk_name_aux=inputname.get("1.0", "end-1c").strip()
                if(len(disk_name_aux)==0):
                        errorMessage+="\n*El disco debe tener un nombre asociado"
                        allOk=False

                anyGenreSelected=False
                
                for g in genres_selected:
                        if(genres_selected[g]==True):
                                anyGenreSelected=True
                                break

                if(anyGenreSelected==False):
                        errorMessage+="\n*El disco debe tener asociado al menos un género musical"
                        allOk=False

                if(allOk==False):
                        errorWindow(errorMessage)
                else:
                        disc=ET.SubElement(root, 'disco')
                        disc.set('nombre', disk_name_aux)
                        disc.set('anho', year_aux)
                        disc.set('imagen', "")
                        for g in genres_selected:
                                if(genres_selected[g]==True):
                                        genre=ET.SubElement(disc, 'genero')
                                        genre.text=g
                        
                        for a in artistsnames:
                                artist=ET.SubElement(disc,'artista')
                                artist.text=a
                        songs=ET.SubElement(disc, 'canciones')                        
                        tree.write(filename)

                        successfullDisk()

        bok.config(command=diskCreator)

"""
here ends the disco creator window
***********************************************************************************************************************************************
"""
#adding the new disk window to its button
l1newdisk.configure(command=windowNewAlbum)  

#function to delete disks
def deleteDisk(pos):
        global page, root, tree, filename
        pos_in_audiolibrary=(page*6)+pos
        
        alertwndw = Toplevel(wndw)
        alertwndw.title("¡¡¡Atención!!!")
        alertwndw.geometry("280x200")
        alertwndw['bg']='black'
        
        Label(
                alertwndw,
                text="Atención:",
                font="Verdana 25",
                background="black",
                fg="yellow"
        ).grid(row=0, column=0, columnspan=2)
        
        disk_remove_name="disco"
        #disk_remove_name=root[pos_in_audiolibrary].attrib('nombre')

        Label(
                alertwndw,
                text="Está a punto de eliminar el disco\n" + disk_remove_name+"\n¿Está segur@?",
                font="Verdana 12",
                background="black",
                fg="white"
        ).grid(row=1, column=0, columnspan=2)

        def remove():
                root.remove(root[pos_in_audiolibrary])
                tree.write(filename)
                readXML()
                first_page()
                changeDisksView()
                alertwndw.destroy()

        Button(
                alertwndw,
                text="Borrar disco",
                background="red",
                command=remove
        ).grid(row=2, column=0, pady=30)

        Button(
                alertwndw,
                text="Déjalo estar",
                background="#00bf36",
                command=lambda: alertwndw.destroy()
        ).grid(row=2, column=1)        



list_p[0].configure(command=lambda:deleteDisk(0))
list_p[1].configure(command=lambda:deleteDisk(1))
list_p[2].configure(command=lambda:deleteDisk(2))
list_p[3].configure(command=lambda:deleteDisk(3))
list_p[4].configure(command=lambda:deleteDisk(4))
list_p[5].configure(command=lambda:deleteDisk(5))        


def disckInferface(pos):
        global page, root
        diskwndw = Toplevel(wndw)
        diskwndw.title("DISCO")
        diskwndw.geometry("800x800")
        diskwndw['bg']='black'
        pos_in_audiolibrary=(page*6)+pos

        Label(
                diskwndw,
                background="black",
                image=arrow_icon,
                width=100,
                height=100
        ).grid(row=0, column=0)

        Label(
                diskwndw,
                background="white",
                image=delete_icon,
                width=155,
                height=155
        ).grid(row=1, column=1, rowspan=3, columnspan=2, padx=20)

        limage_disk=Label(
                diskwndw,
                background="black",
                image=icon_cd,
                width=150,
                height=150
        )
        limage_disk.grid(row=1, column=1, rowspan=3, columnspan=2)

        Label(
                diskwndw,
                text=root[pos_in_audiolibrary].attrib["anho"],
                background="white",
                fg="white",
                font="Verdana 17"
        ).grid(row=1, column=1)

        lyear=Label(
                diskwndw,
                text=root[pos_in_audiolibrary].attrib["anho"],
                background="black",
                fg="#00bf36",
                font="Verdana 15"
        )
        lyear.grid(row=1, column=1)

        ltitle=Label(
                diskwndw,
                text=root[pos_in_audiolibrary].attrib["nombre"],
                background="black",
                fg="#00bf36",
                font="Verdana 30"
        )
        ltitle.grid(row=1, column=3, columnspan=5)

        bedit=Button(
                diskwndw,
                background="black",
                image=edit_icon,
                width=55,
                height=55
        )
        bedit.grid(column=8, row=1)

        #genres availables in disk
        lg1=Label(
                diskwndw,
                background="white",
                image=delete_icon,
                width=20,
                height=20 
        )
        lg1.grid(row=2, column=3, sticky="s", pady=5)

        lg2=Label(
                diskwndw,
                background="white",
                image=delete_icon,
                width=20,
                height=20 
        )
        lg2.grid(row=2, column=4, pady=5, padx=5, sticky="s")

        lg3=Label(
                diskwndw,
                background="white",
                image=delete_icon,
                width=20,
                height=20 
        )
        lg3.grid(row=2, column=5, sticky="s", pady=5)

        lg4=Label(
                diskwndw,
                background="white",
                image=delete_icon,
                width=20,
                height=20 
        )
        lg4.grid(row=2, column=6, padx=5, sticky="s", pady=5)

        lg5=Label(
                diskwndw,
                background="white",
                image=delete_icon,
                width=20,
                height=20 
        )
        lg5.grid(row=3, column=3, sticky="n")

        lg6=Label(
                diskwndw,
                background="white",
                image=delete_icon,
                width=20,
                height=20 
        )
        lg6.grid(row=3, column=4, sticky="n")

        lg7=Label(
                diskwndw,
                background="white",
                image=delete_icon,
                width=20,
                height=20 
        )
        lg7.grid(row=3, column=5, sticky="n")

        lg8=Label(
                diskwndw,
                background="white",
                image=delete_icon,
                width=20,
                height=20 
        )
        lg8.grid(row=3, column=6, sticky="n")

        artists_long=""
        count_artist=0
        for a in root[pos_in_audiolibrary].iter('artista'):
                count_artist+=1
                if(count_artist==1):
                        artists_long+=a.text
                elif(count_artist!=4):
                        artists_long+="\n"+a.text

        if(count_artist>3):
                artists_long+="\ny "+str(count_artist-3)+" más"

        lartists=Label(
                diskwndw,
                text=artists_long,
                background="black",
                fg="#00bf36",
                font="Verdana 15"
        )        
        lartists.grid(row=2, column=7, rowspan=2)

        bmore_artists=Button(
                diskwndw,
                background="white",
                image=more_artists_icon,
                width=55,
                height=55
        )
        bmore_artists.grid(column=8, row=3)
                       
        badd_songs=Button(
                diskwndw,
                background="white",
                image=more_songs_icon,
                width=55,
                height=55
        )
        badd_songs.grid(column=1, row=4)                        

        count_songs=0
        
        for s in root[pos_in_audiolibrary].iter('cancion'):
                count_songs+=1

        print(count_songs)        

        page_song=0

        

list_d[0].configure(command=lambda:disckInferface(0))


wndw.mainloop()