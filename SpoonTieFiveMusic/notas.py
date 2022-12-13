import xml.etree.ElementTree as ET
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
import datetime


filename="MusicaXML/audioteca.xml"
tree = ET.parse(filename)
root=tree.getroot()

cont=0
for canciones in root[0].iter("canciones"):
    canciones.remove(canciones[9])   

tree.write(filename)




