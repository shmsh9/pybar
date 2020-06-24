#!/usr/bin/python3
from time import strftime
from tkinter import Tk,Label,Canvas

global Modules
Modules =   {
                'Battery': {'label':'BatteryPercentage()', 'eval':True, 'space':2 },
                'Date': {'label':"strftime('%D %H:%M:%S')", 'eval':True, 'space':1},
            }

def generateModules():
    longString = ' '
    for module in Modules:
        if(Modules[module]['eval'] == True):
            longString += eval(Modules[module]['label'])
        else:
            longString += Modules[module]['label']

        if(Modules[module]['space'] != 0):
            longString += ' '*(Modules[module]['space'])
        else:
            longString += ' '
    
    Label.config(text=longString, font=(44))
    Label.after(1000,generateModules)
    Label.pack()
    return 0

def BatteryPercentage():
    percentage = open('/sys/class/power_supply/BAT0/capacity','r').readline().strip()
    return percentage+"%"

def Main():
    Window = Tk()
    Window.wait_visibility(Window)
    Window.wm_attributes("-alpha", 0.8)
    Window.title("pybar")

    global can
    can = Canvas(Window)
    can.pack()
    global Label
    Label = Label(can)


    Window.after(0, generateModules)
    Window.mainloop()
    return 0

Main()