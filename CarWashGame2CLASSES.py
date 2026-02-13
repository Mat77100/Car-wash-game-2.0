#last modified 05/02/2026
import time
import random
import threading
class player:
    def __init__(self, money, fame, costF):
        self.money = money
        self.fame = fame
        self.costF = costF
        self.lock = threading.Lock()
    def GetBalance(self):
        with self.lock:
            return self.money
    def EditBalance(self,Amount):
        with self.lock:
            self.money += Amount
    def GetFame(self):
        return self.fame
    def GetCostF(self):
        return self.costF
    def UpgradeFame(self):
        if self.fame ==10:
            print("Max fame reached")
        elif self.money >= self.costF:
            self.money -= self.costF
            self.costF += (self.costF * 0.6)
            self.fame += 1
            print(f"Upgrade compleate! Fame at {self.fame}")
        else:
            print("\033[31m**Upgrade Failed** ---> Balance too low\033[0m")
    def GetMoneyPerSecond(self):
        T1 = self.money
        time.sleep(1)
        T2 = self.money
        return T2-T1



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
    def GetQueueSlots(self):
        return self.QueueSlots
    def GetSpeed(self):
        return self.speed
    def GetCostQueue(self):
        return self.costQueue
    def GetCostSpeed(self):
        return self.costSpeed
    def AddToQ(self):
        if not(self.BoQ >= len(self.Q)):
            self.Q[self.BoQ] = "Create a vehicle object here"
            self.BoQ +=1
    def WashFoQ(self,p1):
        if self.Q[0] != "Empty":
            Selected = self.Q[0]
            dirt = 15*Selected.GetSizeMult()
            while dirt > 0:
                dirt -= 1
                time.sleep(self.speed)
            print(f"Vehicle cleaned! it paid £{Selected.GetPay()}")
            p1.EditBalance(Selected.GetPay())
            for i in range(0, self.QueueSlots-1):
                self.Q[i] = self.Q[i+1]
            self.BoQ -= 1
    def UpgradeQ(self,p1):
        if p1.GetBalance()<= self.costQueue:
            print("\033[31m**Upgrade Failed** ---> Balance too low\033[0m")
        else:
            self.QueueSlots +=1
            self.Q = ["Empty"]*self.QueueSlots
            p1.EditBalance(-self.costQueue)
            self.costQueue = self.costQueue * 2
            print(f"Upgrade compleate! New queue has {self.QueueSlots} queue slots")
    def UpgradeSpeed(self,p1):
        if p1.GetBalance() >= self.costSpeed:
            self.speed = round(self.speed * 0.75,3)
            p1.EditBalance(-self.costSpeed)
            self.costSpeed = self.costSpeed + (self.costSpeed * 0.5)
            print(f"Upgrade compleate! Speed at {self.speed}")
        else:
            print("\033[31m**Upgrade Failed** ---> Balance too low\033[0m")
class CarWash(WashStation):
    def __init__(self, speed, costSpeed, costQueue, QueueSlots, BoQ):
        super().__init__(speed, costSpeed, costQueue, QueueSlots, BoQ)
        self.FuelTypesUnlocked = 1
    def UnlockNewFuel(self,p1):
        if self.FuelTypesUnlocked != 3 and p1.GetBalance >=100:
            p1.EditBalance(-100)
            self.FuelTypesUnlocked += 1
            print("New fuel unlocked")
        else:
            print("\033[31m**Upgrade Failed** ---> Balance too low\033[0m") 
    def AddToQ(self):
        if not(self.BoQ >= len(self.Q)-1):
            self.Q[self.BoQ] = Cars(20,round(random.uniform(1,1.5),2),random.randint(10,100))
            self.BoQ +=1
    def Refuel(self,p1):
        Selected = self.Q[0]
        if Selected.Refuel():
            Amount = 100 - Selected.GetFuelTank
            if (Selected.GetFuelType() == "Petrol") and (self.FuelTypesUnlocked >= 1):
                print("Filled with petrol")
                p1.EditBalance(1*Amount)
            if (Selected.GetFuelType() == "Diesel") and (self.FuelTypesUnlocked >= 2):
                print("Filled with Diesel")
                p1.EditBalance(1.5*Amount)
            if (Selected.GetFuelType() == "Super") and (self.FuelTypesUnlocked >= 3):
                print("Filled with Super")
                p1.EditBalance(2*Amount)
        else:
            print("the car didnt refuel")

        
class Vehicles:
    def __init__(self, Pay,SizeMult):
        self.pay = Pay
        self.SizeMult = SizeMult
    def GetPay(self):
        return self.pay
    def GetSizeMult(self):
        return self.SizeMult

class Cars(Vehicles):
    def __init__(self,Pay,SizeMult,FuelTank):
        super().__init__(Pay,SizeMult)
        self.FuelTank = FuelTank
        A = random.randint(1,3)
        if A == 1:
            self.FuelType = "Petrol"
        elif A == 2:
            self.FuelType = "Diesel"
        elif A == 3:
            self.FuelType = "Super"
    def GetFuelTank(self):
        return self.FuelTank
    def GetFuelType(self):
        return self.FuelType
    def Refuel(self):
        if self.FuelTank > 80:
            return False
        elif self.FuelTank > 50:
            if random.randint(1,3) == 3:
                return True
        elif self.FuelTank > 20:
            if random.randint(1,2) == 2:
                return True
        else:
            return True


