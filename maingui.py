from tkinter import *
import tkinter as tk
from tkinter import ttk
from pathlib import Path
import pandas as pd
import os
import csv
from tkinter import filedialog
from airportCodes import loadAirports, getAirportCode
from cleartrip import getClearTripFlights
from easymytrip import getEasyMyTripFlights
from ixigo import getIxigoflights
from makemytrip import getMakeMyTripFlights
from emailmethod import sendEmail
from saveascsv import saveascvs

window = Tk()

window.geometry("1800x900")
window.configure(bg="#FFFFFF")

canvas = Canvas(window, bg = "#FFFFFF", bd =0, highlightthickness=0, relief = "ridge")
canvas.pack(side=LEFT, expand = True, fill = BOTH)


canvas.create_text(856,18,anchor="nw",text="Best flight price finder",fill="#000000",font=("Inter", 20 * -1))

canvas.create_line(85,50,1835,50)

canvas.create_text(160,70,anchor="nw",text="Enter your starting point :",fill="#000000",font=("Inter", 20 * -1))

entry_1 = Entry(bd=0,bg="#D9D9D9",fg="#000716",highlightthickness=0)
entry_1.place(x=420,y=70,width=217.0,height=31.0)
canvas.create_text(800,70,anchor="nw",text="Enter your end point :",fill="#000000",font=("Inter", 20 * -1))

entry_2 = Entry(bd=0,bg="#D9D9D9",fg="#000716",highlightthickness=0)
entry_2.place(x=1040,y=70,width=217.0,height=31.0)


button_1 = Button(text="search",borderwidth=0,highlightthickness=0,command=lambda: buttonpush(),relief="flat")
button_1.place(x=1400,y=70,width=210.0,height=40.0)


#csv
canvas.create_text(234,728,anchor="nw",text="Enter or browse path to save csv:",fill="#000000",font=("Inter", 20 * -1))

entry_3 = Entry(bd=0,bg="#D9D9D9",fg="#000716",highlightthickness=0)
entry_3.place(x=234,y=768,width=217.0,height=31.0)

button_2 = Button(text="browse and download",borderwidth=0,highlightthickness=0,command=lambda: getdir(),relief="flat")
button_2.place(x=234,y=818,width=210.0,height=40.0)

label1 = canvas.create_text(234,888,anchor="nw",text="",fill="#000000",font=("Inter", 20 * -1))



#email
canvas.create_text(976,728,anchor="nw",text="Enter your email to send csv :",fill="#000000",font=("Inter", 20 * -1))

entry_4 = Entry(bd=0,bg="#D9D9D9",fg="#000716",highlightthickness=0)
entry_4.place(x=976,y=768,width=217.0,height=31.0)

button_3 = Button(text="send mail",borderwidth=0,highlightthickness=0,command=lambda: sendmail(),relief="flat")
button_3.place(x=976,y=818,width=210.0,height=40.0)


label = canvas.create_text(976,888,anchor="nw",text="",fill="#000000",font=("Inter", 20 * -1))

flights1 =[]
flights2 =[]

def getdir():
    path = str(filedialog.askdirectory())
    path.replace('\\', '/',100)
    entry_3.insert(0,path)
    createCsv(entry_3.get())
   

def createCsv(path):
    global flights1
    global flights2
    path = saveascvs(path,flights1, flights2)
    if len(path)>0:
        canvas.itemconfig(label1, text=f"csv saved at {path}")
    else:
        canvas.itemconfig(label1, text="please enter correct path")
    

def sendmail():
    createCsv("./")
    path = "./flightsdata.csv"
    if sendEmail(path, entry_4.get()):
        canvas.itemconfig(label, text= "email sent")
    else:
        canvas.itemconfig(label, text= "please enter correct email")

def buttonpush():
    fromcity = entry_1.get()
    tocity = entry_2.get()
    
    loadAirports()
    fromcitycode = getAirportCode(fromcity)
    tocitycode = getAirportCode(tocity)
    print(fromcitycode)
    print(tocitycode)
    #flights3 =[]
    #flights4 =[]
    #getClearTripFlights(fromcitycode, tocitycode, flights1)
    getEasyMyTripFlights(fromcitycode, tocitycode, flights1)
    getIxigoflights(fromcitycode, tocitycode, flights2)
    #getMakeMyTripFlights(fromcitycode, tocitycode, flights4)
    

    #createfirsttable(flights1)
    createfirsttable(flights1);
    createsecondtable(flights2)
    #createthridtable(flights3)
    #createfouthtable(flights4)


def createfirsttable(flights):
    #table = ttk.Treeview(window,yscrollcommand=table_scroll.set)

    canvas.create_text(85,150,anchor="nw",text="easymytrip",fill="#000000",font=("Inter", 20 * -1))
    table = ttk.Treeview(canvas)
    table['column'] = ('flightname', 'starttime', 'endtime', 'totaljourneytime', 'totalstops', 'price')
    table.pack()

    table_scroll = Scrollbar(table)
    table_scroll = Scrollbar(table,orient='vertical')
    table_scroll.pack(side=RIGHT,fill=Y)
    table_scroll.config(command=table.yview)
    table.config(yscrollcommand=table_scroll.set)

#format our column
    table.column("#0", width=0,  stretch=NO)
    table.column("flightname",anchor=CENTER, width=80)
    table.column("starttime",anchor=CENTER,width=80)
    table.column("endtime",anchor=CENTER,width=80)
    table.column("totaljourneytime",anchor=CENTER,width=80)
    table.column("totalstops",anchor=CENTER,width=80)
    table.column("price",anchor=CENTER,width=80)

#create a heading
    table.heading("#0",text="",anchor=CENTER)
    table.heading("flightname",text="Name",anchor=CENTER)
    table.heading("starttime",text="starttime",anchor=CENTER)
    table.heading("endtime",text="endtime",anchor=CENTER)
    table.heading("totaljourneytime",text="totaljourney",anchor=CENTER)
    table.heading("totalstops",text="totalstops",anchor=CENTER)
    table.heading("price",text="price",anchor=CENTER)

    i =0
    for index in range(len(flights)):
        table.insert(parent='',index='end',values=(flights[index].flightname, flights[index].starttime, flights[index].endtime, flights[index].totaljourneytime, flights[index].totalstops, flights[index].price))
        i = i+1
    #for i in range(100):
    #    table.insert(parent='', index='end', iid=f'{i}', values=('afd', 'jdkfaafa', 'vaevaef', 'veavea', 'veavae', 'vat'))

    table.place(x=85, y=200,width=586, height=437)


def createsecondtable(flights):
    #table = ttk.Treeview(window,yscrollcommand=table_scroll.set)
    canvas.create_text(820,150,anchor="nw",text="Ixigo :",fill="#000000",font=("Inter", 20 * -1))
    table = ttk.Treeview(canvas)
    table['column'] = ('flightname', 'starttime', 'endtime', 'totaljourneytime', 'totalstops', 'price')
    table.pack()

    table_scroll = Scrollbar(table)
    table_scroll = Scrollbar(table,orient='vertical')
    table_scroll.pack(side=RIGHT,fill=Y)
    table_scroll.config(command=table.yview)
    table.config(yscrollcommand=table_scroll.set)

#format our column
    table.column("#0", width=0,  stretch=NO)
    table.column("flightname",anchor=CENTER, width=80)
    table.column("starttime",anchor=CENTER,width=80)
    table.column("endtime",anchor=CENTER,width=80)
    table.column("totaljourneytime",anchor=CENTER,width=80)
    table.column("totalstops",anchor=CENTER,width=80)
    table.column("price",anchor=CENTER,width=80)

#create a heading
    table.heading("#0",text="",anchor=CENTER)
    table.heading("flightname",text="Name",anchor=CENTER)
    table.heading("starttime",text="starttime",anchor=CENTER)
    table.heading("endtime",text="endtime",anchor=CENTER)
    table.heading("totaljourneytime",text="totaljourney",anchor=CENTER)
    table.heading("totalstops",text="totalstops",anchor=CENTER)
    table.heading("price",text="price",anchor=CENTER)

    i =0
    for index in range(len(flights)):
        table.insert(parent='',index='end',values=(flights[index].flightname, flights[index].starttime, flights[index].endtime, flights[index].totaljourneytime, flights[index].totalstops, flights[index].price))
        i = i+1
#    for i in range(100):
#        table.insert(parent='', index='end', iid=f'{i}', values=('afd', 'jdkfaafa', 'vaevaef', 'veavea', 'veavae', 'vat'))

    table.place(x=820, y=200,width=586, height=437)


def createthridtable(flights):
    #table = ttk.Treeview(window,yscrollcommand=table_scroll.set)
    table = ttk.Treeview(canvas)
    table['column'] = ('flightname', 'starttime', 'endtime', 'totaljourneytime', 'totalstops', 'price')
    table.pack()

    table_scroll = Scrollbar(table)
    table_scroll = Scrollbar(table,orient='vertical')
    table_scroll.pack(side=RIGHT,fill=Y)
    table_scroll.config(command=table.yview)
    table.config(yscrollcommand=table_scroll.set)

#format our column
    table.column("#0", width=0,  stretch=NO)
    table.column("flightname",anchor=CENTER, width=80)
    table.column("starttime",anchor=CENTER,width=80)
    table.column("endtime",anchor=CENTER,width=80)
    table.column("totaljourneytime",anchor=CENTER,width=80)
    table.column("totalstops",anchor=CENTER,width=80)
    table.column("price",anchor=CENTER,width=80)

#create a heading
    table.heading("#0",text="",anchor=CENTER)
    table.heading("flightname",text="Name",anchor=CENTER)
    table.heading("starttime",text="starttime",anchor=CENTER)
    table.heading("endtime",text="endtime",anchor=CENTER)
    table.heading("totaljourneytime",text="journeyduration",anchor=CENTER)
    table.heading("totalstops",text="stops",anchor=CENTER)
    table.heading("price",text="price",anchor=CENTER)

    i =0
    for index in range(len(flights)):
        table.insert(parent='',index='end',values=(flights[index].flightname, flights[index].starttime, flights[index].endtime, flights[index].totaljourneytime, flights[index].totalstops, flights[index].price))
        i = i+1

    table.place(x=85, y=587,width=586, height=437)

def createfouthtable(flights):
    #table = ttk.Treeview(window,yscrollcommand=table_scroll.set)
    table = ttk.Treeview(canvas)
    table['column'] = ('flightname', 'starttime', 'endtime', 'totaljourneytime', 'totalstops', 'price')
    table.pack()

    table_scroll = Scrollbar(table)
    table_scroll = Scrollbar(table,orient='vertical')
    table_scroll.pack(side=RIGHT,fill=Y)
    table_scroll.config(command=table.yview)
    table.config(yscrollcommand=table_scroll.set)

#format our column
    table.column("#0", width=0,  stretch=NO)
    table.column("flightname",anchor=CENTER, width=80)
    table.column("starttime",anchor=CENTER,width=80)
    table.column("endtime",anchor=CENTER,width=80)
    table.column("totaljourneytime",anchor=CENTER,width=80)
    table.column("totalstops",anchor=CENTER,width=80)
    table.column("price",anchor=CENTER,width=80)

#create a heading
    table.heading("#0",text="",anchor=CENTER)
    table.heading("flightname",text="Name",anchor=CENTER)
    table.heading("starttime",text="starttime",anchor=CENTER)
    table.heading("endtime",text="endtime",anchor=CENTER)
    table.heading("totaljourneytime",text="totaljourney",anchor=CENTER)
    table.heading("totalstops",text="totalstops",anchor=CENTER)
    table.heading("price",text="price",anchor=CENTER)

    i =0
    for index in range(len(flights)):
        table.insert(parent='',index='end',values=(flights[index].flightname, flights[index].starttime, flights[index].endtime, flights[index].totaljourneytime, flights[index].totalstops, flights[index].price))
        i = i+1
    #for i in range(100):
        #table.insert(parent='', index='end', iid=f'{i}', values=('afd', 'jdkfaafa', 'vaevaef', 'veavea', 'veavae', 'vat'))

    table.place(x=962, y=587,width=586, height=437)


window.resizable(True, True)
window.mainloop()
