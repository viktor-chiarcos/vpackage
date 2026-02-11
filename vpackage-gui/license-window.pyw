#!/bin/python3

from tkinter import *
License=Tk()

scrollbar = Scrollbar(License)
scrollbar.pack( side = RIGHT, fill=Y )
License.minsize(width=1350 , height=700)#0)

mycanvas = Canvas(License, yscrollcommand = scrollbar.set, xscrollcommand = scrollbar.set, width=1350 , height=700 )

with open("./vpackage-path.log","rt") as inhalt:
   datei=inhalt.read().strip().split("\n")[-1]+"/LICENSE"
   with(open(datei,"rt")) as mehr_inhalt:
      zeile=mehr_inhalt.readlines()#+["Inhalt"]

en=Label(License,text="Englische Lizenz")
en.pack()
mylist = Listbox(License)
for line in zeile:
   zeilen = line
   mylist.insert(END, zeilen)
   
mylist.pack( fill=BOTH )
"""
de=Label(License, text="Deutsche Lizenz")
with open("./vpackage-path.log","rt") as inhalt2:
   datei=inhalt2.read().strip().split("\n")[-1]+"/LICENSE.de.md"
   with(open(datei,"rt")) as mehr_inhalt2:
      zeile2=mehr_inhalt2.readlines()#+["Inhalt"]

mylist2 = Listbox(License)
for line in zeile:
   zeilen = line
   mylist.insert(END, zeile2)
   
mylist2.pack( fill=BOTH )
"""
scrollbar.config( command = mycanvas.yview )
scrollbar.config( command = mycanvas.xview )
License.mainloop()