
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




carName = "Tesla Car"
carkm = 0.0   # km
carfuel = 100 # kWh
consumption = 1.6 # kWh/km
passengers = ["Emin","Deniz"] # Max 4



carName2 = "Ferrari"
carkm2 = 0.0   # km
carfuel2 = 120  # lt
consumption2 = 5.6 # lt/km
passengers2 = ["Durmus","Ezgi"] # Max 3

car1 = Car("Tesla Car",100,1.6,["Emin","Deniz"],4)
car2 = Car("Ferrari",120,5.6,["Durmus","Ezgi"],3)
car3 = Car("Mustang GT",220,11,["Umut"],2)

car1.print_car()
car2.print_car()
car3.print_car()


print(f'--- Car {carName} ---\n| km: {carkm}\n| fuel: {carfuel}\n| Passengers: {passengers}')
print(f'--- Car {carName2} ---\n| km: {carkm2}\n| fuel: {carfuel2}\n| Passengers: {passengers2}')

## Move 10 km with Tesla
car1.move(10)
# if (10 * consumption <= carfuel):
#     carkm += 10
#     carfuel -= 10 * consumption
# else:
#     maxKm = carfuel / consumption
#     carkm += maxKm
#     carfuel = 0
#     print("There isn't enough fuel! Go to the nearest gas station!")
    
## Get a new passanger named "Kagan" there -> Tesla
car1.get_passenger("Kagan")
# if len(passengers) < 3:    
#     passengers.append("Kagan")
# else:
#     print("There is no space !!")

## Move further 900 km
car1.move(900)
# if (900 * consumption <= carfuel):
#     carkm += 900
#     carfuel -= 900 * consumption
# else:
#     maxKm = carfuel / consumption
#     print("Maxkm: ",maxKm)
#     carkm += maxKm
#     carfuel = 0
#     print("There isn't enough fuel! Go to the nearest gas station!")

##################

## Move 22 km with
car2.move(22)
# if (22 * consumption2 <= carfuel2):
#     carkm2 += 22
#     carfuel2 -= 22 * consumption2
# else:
#     maxKm = carfuel2 / consumption2
#     print("maxkm: ",maxKm)
#     carkm2 += maxKm
#     carfuel2 = 0
#     print("There isn't enough fuel! Go to the nearest gas station!")
## Get 26 lt fuel
car2.get_fuel(26)
# carfuel2 += 26
## Move 17 km 
car2.move(17)
# if (22 * consumption2 <= carfuel2):
#     carkm2 += 17
#     carfuel2 -= 17 * consumption2
# else:
#     maxKm = carfuel2 / consumption2
#     carkm2 += maxKm
#     print("maxkm: ",maxKm)
#     carfuel2 = 0
#     print("There isn't enough fuel! Go to the nearest gas station!")
## Take 3 passangers -> "Mehmet" "Hatice" "Muhammet"
car2.get_passengers(["Mehmet","Hatice","Muhammet"])
# if len(passengers2) < 3:
#     passengers2.append("Mehmet")
# else:
#     print("There is no space !!")
# if len(passengers2) < 3:
#     passengers2.append("Hatice")
# else:
#     print("There is no space !!")
# if len(passengers2) < 3:    
#     passengers2.append("Muhammet")
# else:
#     print("There is no space !!")

car1.print_car()
car2.print_car()
# print(f'--- Car {carName} ---\n| km: {carkm}\n| fuel: {carfuel}\n| Passengers: {passengers}')
# print(f'--- Car {carName2} ---\n| km: {carkm2}\n| fuel: {carfuel2}\n| Passengers: {passengers2}')



