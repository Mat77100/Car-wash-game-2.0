from CarWashGame2CLASSES import *
import random
import threading
import tkinter as tk
import time

p1 = player(50,1,50)

is_open = False


startmenu = tk.Tk(screenName="startmenu",baseName="startmenu",)
startmenu.geometry("400x200")
intro = tk.Label(startmenu, text="Hello! Welcome to").pack()
title = tk.Label(startmenu,text= "Car Wash Game 2.0",font="bold 30 italic").pack()

def main():
    main = tk.Toplevel(startmenu)
    main.geometry("500x300")
    startmenu.withdraw()
    Quitbtn = tk.Button(main,text="QUIT",font="5",command=startmenu.destroy).pack()
    Balance = tk.Label(main,text=f"Balance: £{p1.GetBalance()}",font="20")
    Balance.pack()
    tk.Button(main,text="Open the car wash station!",font=40, command=carwashmenu).pack()
    def updateBalance():
        Balance.config(text=f"Balance: £{p1.GetBalance()}")
        main.after(200,updateBalance)
    updateBalance()

def carwashmenu():
    global is_open
    if is_open == False:
        menu = tk.Toplevel(startmenu)
        is_open = True
        Carwash1 = CarWash(1,50,100,3,0)
        def AddLoop():
            while True:
                if random.randint(1,10) < p1.GetFame():
                    Carwash1.AddToQ()
                time.sleep(1)
        def washLoop():
            while True:
                Carwash1.WashFoQ(p1)
                time.sleep(1)
        threading.Thread(target=AddLoop, daemon=True).start()
        threading.Thread(target=washLoop, daemon=True).start()
        CurrentQ = tk.Label(menu,font="80")
        CurrentQ.pack()
        def US():
            Carwash1.UpgradeSpeed(p1)
        def UQ():
            Carwash1.UpgradeQ(p1)
        UpgradeFame=tk.Button(menu,text=f"Upgrade fame: £{p1.GetCostF()} -- current level - {p1.GetFame()}",command=p1.UpgradeFame)
        UpgradeSpeed=tk.Button(menu,text=f"Upgrade wash speed: £{Carwash1.GetCostSpeed()} -- current clean delay - {Carwash1.GetSpeed()}",command=US)
        UpgradeQ=tk.Button(menu,text=f"Upgrade queue size: £{Carwash1.GetCostQueue()} -- current queue max length - {Carwash1.GetQueueSlots()}",command=UQ)
        UpgradeFame.pack()
        UpgradeSpeed.pack()
        UpgradeQ.pack()
        def UpdateLabels():
            UpgradeFame.config(text=f"Upgrade fame: £{p1.GetCostF()} -- current level - {p1.GetFame()}")
            UpgradeSpeed.config(text=f"Upgrade wash speed: £{Carwash1.GetCostSpeed()} -- current clean delay - {Carwash1.GetSpeed()}")
            UpgradeQ.config(text=f"Upgrade queue size: £{Carwash1.GetCostQueue()} -- current queue max length - {Carwash1.GetQueueSlots()}")
            Qtext = "Current Queue: "
            for car in Carwash1.GetCurrentQ():
                if car == "Empty":
                    Qtext +="■"
                elif car.GetSizeMult() > 1.3:
                    Qtext += "🚙, "
                else:
                    Qtext += "🚗, "
            CurrentQ.config(text=Qtext,font="80")
            menu.after(200, UpdateLabels)
        UpdateLabels()

    else:
        print("Already open!")
    


Playbtn = tk.Button(startmenu, text="PLAY!", width=20, height=10, font="Helvetica 15 bold italic",command=main).pack()
startmenu.mainloop()

