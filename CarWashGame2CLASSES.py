#last modified 05/02/2026
import time
import random

class player:
    def __init__(self, money, fame, costF):
        self.money = money
        self.fame = fame
        self.costF = costF
        #self.locations = []
    def GetBalance(self):
        return self.money
    def EditBalance(self,Amount):
        self.money += Amount
    def GetFame(self):
        return self.fame
    def GetCostF(self):
        return self.costF
    def UpgradeFame(self):
        if self.money >= self.costF:
            self.money - costF
            self.costF + (costF * 0.6)
            self.fame + 1
            print(f"Upgrade compleate! Fame at {self.fame}")
        else:
            print("\033[31m**Upgrade Failed** ---> Balance too low\033[0m")
    def GetMoneyPerSecond(self):
        T1 = self.money
        time.sleep(1)
        T2 = self.money
        return T2-T1

p1 = player(0,1,50)

class WashStation:
    def __init__(self,speed,costSpeed,costQueue,QueueSlots,BoQ):
        self.speed = speed
        self.costSpeed = costSpeed
        self.costQueue = costQueue
        self.QueueSlots = QueueSlots
        self.BoQ = BoQ
        self.Q = ["Empty"]*self.QueueSlots
    def GetCurrentQ(self):
        return self.Q
    def GetSpeed(self):
        return self.speed
    def GetCostQueue(self):
        return self.costQueue
    def GetCostSpeed(self):
        return self.costSpeed
    def AddToQ(self):
        pass
    def WashFoQ(self):
        if self.Q[0] != "Empty":
            Selected = self.Q[0]
            dirt = 15*Selected.GetSizeMult()
            while dirt != 0:
                dirt -= 1
                time.sleep(self.speed)
            print(f"Vehicle cleaned! it paid £{Selected.GetPay()}")
            p1.EditBalance(Selected.GetPay())
            for i in range(0, self.QueueSlots-1):
                self.Q[i] = self.Q[i+1]
    def UpgradeQ(self):
        if p1.GetBalance()< self.costQueue:
            print("\033[31m**Upgrade Failed** ---> Balance too low\033[0m")
        else:
            self.QueueSlots +=1
            self.Q = ["Empty"]*self.QueueSlots
            p1.EditBalance(-self.costQueue)
            self.costQueue = self.costQueue * 2
            print(f"Upgrade compleate! New queue has {self.QueueSlots} queue slots")
    def UpgradeSpeed(self):
        if p1.GetBalance() < self.costSpeed:
            print("\033[31m**Upgrade Failed** ---> Balance too low\033[0m")
        else:
            self.speed = round(self.speed * 0.75,3)
            p1.EditBalance(-self.costSpeed)
            self.costSpeed = self.costSpeed + (self.costSpeed * 0.5)
            print(f"Upgrade compleate! Speed at {self.speed}")
            
class CarWash(WashStation):
    def __init__(self, speed, costSpeed, costQueue, QueueSlots, BoQ, FuelType):
        super().__init__(speed, costSpeed, costQueue, QueueSlots, BoQ)


#make the car wash first and make the game, then come back adn add the rest of the washes/vehicles




        
class Vehicles:
    def __init__(self, Pay, WashTime,SizeMult):
        self.pay = Pay
        self.WashTime = WashTime
        self.SizeMult = SizeMult
    def GetPay(self):
        return self.Pay
    def GetWashTime(self):
        return self.WashTime
    def GetSizeMult(self):
        return self.SizeMult

class Cars(Vehicles):
    def __init__(self,Pay,WashTime,SizeMult,FuelTank,FuelType):
        super().__init__(Pay,WashTime,SizeMult)
        self.FuelTank = FuelTank
        self.FuelType = FuelType
    def GetFuelTank(self):
        return self.FuelTank
    def GetFuelType(self):
        return self.FuelType
    def Refuel(self):
        if self.FuelTank > 80:
           print("Car doesn't need fuel")
        elif self.FuelTank > 50:
            #Different prices for different fuel, make the wash station first for the diff fuel types









price = 10

costW = 100
costP = 100



action = int(0)
carNum = 0
shopAct = 0

running = True
lock = threading.Lock()
