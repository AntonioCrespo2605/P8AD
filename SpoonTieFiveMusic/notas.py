import xml.etree.ElementTree as ET
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
import datetime
import shutil
import os
from tkinter import filedialog

"""
filename="MusicaXML/audioteca.xml"
tree = ET.parse(filename)
root=tree.getroot()
cont=0
for canciones in root[0].iter("canciones"):
    canciones.remove(canciones[9])   

tree.write(filename)"""

filename=filedialog.askopenfilename(title = "Select file",filetypes = (('mp3 Files.', '*.mp3'),))
if(filename!=""):
    newfilename="./src/mp3/"
    head=os.path.split(filename)
    newfilename+=head[1]
    if(os.path.exists(newfilename)==False):
            shutil.copy(filename, newfilename)
    linkmp3=newfilename


