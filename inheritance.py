class Vehicle():
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
    def start_engine(self):
        print(f"{self.model} is starting")

class Car(Vehicle):
    def __init__(self,make,model,year,num_doors,num_passengers):
        super().__init__(make,model,year)
        self.doors = num_doors
        self.num_passengers = num_passengers
    def drive(self):
        print(f"{self.model} is driving")
    def start_engine(self):
        print(f"The car`s engine is starting")
class Truck(Vehicle):
    def __init__(self,make,model,year,cargo_capacity,towing_capacity):
        super().__init__(make,model,year)
        self.cargo_capacity = cargo_capacity
        self.towing_capacity = towing_capacity
    def haul(self):
        print(f"{self.model} is hauling")
    def start_engine(self):
        print("The truck's engine is starting...")

class Motorcycle(Vehicle):
    def __init__(self,make,model,year,num_wheels,has_sidecar):
        super().__init__(make,model,year)
        self.num_wheels = num_wheels
        self.has_sidecar = has_sidecar
    def ride(self):
        print(f"{self.model} is riding")
    def start_engine(self):
        print("The motorcycle's engine is starting...")

