class Vehicle:
    capacity = 0
    power = 0
    fueltype = ""
    engineType = ""
    numOfTires = 0
    
    def __init__(self, capacity = 0, power = 0, fuelType = "Gasoline", engineType = "small block 454", numOfTires = 1):
        self.capacity = capacity
        self.power = power
        self.fuelType = fuelType
        print("Vehicle Created")

    def operate(self):
        print("Vroom Vroom")

    def crash(self):
        print("Oh no!")

    def getFuelType(self):
        return self.fuelType
    
    def setFuelType(self, fuel):
        self.fuelType = fuel


class Car(Vehicle):
    cargo = None
    numOfDoors = None
    modifications = []
    
    def __init__(self, capacity, engineType, numOfTires, cargo = None, numOfDoors = 2):
        Vehicle.__init__(self, capacity = capacity, engineType = engineType, numOfTires = numOfTires)
        self.cargo = cargo
        self.numOfDoors = numOfDoors
        print("Car Created!")

    def modify(self,mods):
        self.modifications.append(mods)
        

