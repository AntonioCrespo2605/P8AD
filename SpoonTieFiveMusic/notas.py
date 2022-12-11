import xml.etree.ElementTree as ET
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
import datetime

filename="MusicaXML/audioteca.xml"
tree = ET.parse(filename)
root=tree.getroot()


for cancion in root[0].iter('artista'):
    print(cancion.text)




