
class Car:

    # constructor
    def __init__(self,name,fuel,consumption,passengers,capacity):
        self.name = name
        self.fuel = fuel
        self.consumption = consumption
        self.km   = 0.0
        self.passengers = passengers
        self.capacity = capacity


    # Behavior
    def print_car(self):
        print(f'--- Car {self.name} ---\n| km: {self.km}\n| fuel: {self.fuel}\n| Passengers: {self.passengers}')

    def move(self,km):
        if( km <= (self.fuel / self.consumption)):
            ## move
            self.km += km
            self.fuel -= km / self.consumption
        else:
            # move as fas as car can
                # calculate max km
            maxKm = self.fuel / self.consumption
            self.km += maxKm
            self.fuel = 0
            print(f"Car {self.name} cannot move further. Please go to the nearest gas station!")

    def get_passenger(self,passanger):
        if (self.capacity > len(self.passengers)):
            # get passenger
            self.passengers.append(passanger)
        else:
            # cannot
            print(f"There is no space for Passenger {passanger}")

    def get_fuel(self,newFuel):
        self.fuel += newFuel

    def get_passengers(self,passengers):
        if len(passengers) < 2:
            # warn
            print("Please use approprate function")
        else:
            for passanger in passengers:
                self.get_passenger(passanger)

car1 = Car("Tesla Car",100,1.6,["Emin","Deniz"],4)
car2 = Car("Ferrari",120,5.6,["Durmus","Ezgi"],3)
car3 = Car("Mustang GT",220,11,["Umut"],2)

car1.print_car()
car2.print_car()
car3.print_car()

car1.move(10)
car1.get_passenger("Kagan")
car1.move(900)

##################
car2.move(22)
car2.get_fuel(26) 
car2.move(17)
car2.get_passengers(["Mehmet","Hatice","Muhammet"])

car1.print_car()
car2.print_car()



