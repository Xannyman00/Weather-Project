import tkinter as tk
import Scripts.humidity as humid
import Scripts.wind as wind
import Scripts.temperature as temp
import Scripts.rain as rain
import Scripts.events as events

root = tk.Tk()
root.title("P-Test")
root.geometry("250x250")
root.resizable(False, False)
root.grid()

def runevents():
    pass

def runhumid():
    pass

def runwind():
    pass

def runtemp():
    pass

def runrain():
    pass

tk.Label(root, text = "Weather Analysis for Eminence Indiana").grid(column=0,row=0)

tk.Label(root, text = "2011-2022").grid(column=0,row=1)
tk.Label(root, text = "\nClick an option below to view data").grid(column=0,row=2)

tk.Button(root, text = "Wind Data", command = lambda: wind.run()).grid(column=0,row=3)
tk.Button(root, text = "Humidity", command = lambda: humid.run()).grid(column=0,row=4)
tk.Button(root, text = "Precipitation", command = lambda: rain.run()).grid(column=0,row=5)
tk.Button(root, text = "Temperatures", command = lambda: temp.run()).grid(column=0,row=6)
tk.Button(root, text = "Weather Events", command = lambda: events.run()).grid(column=0,row=7)
tk.Button(root, text = "Quit Program", command = lambda: root.destroy()).grid(column=0,row=8)

tk.Label(root, text = "\nXander, Brian, Eh, Alden").grid(column=0,row=9)

root.mainloop()
