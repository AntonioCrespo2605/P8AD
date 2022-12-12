import xml.etree.ElementTree as ET
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
import datetime

filename="MusicaXML/audioteca2.xml"
tree = ET.parse(filename)
root=tree.getroot()


for canciones in root[0].iter("canciones"):
    c=ET.SubElement(canciones, "cancion")
    c.set('nombre', 'cancionpython')
    c.set('duracion', '5:30')
    c.set('link', '')
    
tree.write(filename)




