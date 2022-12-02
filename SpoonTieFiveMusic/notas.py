import xml.etree.ElementTree as ET
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
import datetime

filename="MusicaXML/audioteca2.xml"
tree = ET.parse(filename)
root=tree.getroot()



currentDateTime = datetime.datetime.now()
date = currentDateTime.date()
year = date.strftime("%Y")
print(year)



root.append()
fichero=ET.ElementTree(root)
fichero.write(filename)