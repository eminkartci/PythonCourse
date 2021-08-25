
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


print(f'--- Car {carName} ---\n| km: {carkm}\n| fuel: {carfuel}\n| Passengers: {passengers}')
print(f'--- Car {carName2} ---\n| km: {carkm2}\n| fuel: {carfuel2}\n| Passengers: {passengers2}')

## Move 10 km with Tesla
if (10 * 1.6 <= carfuel):
    carkm += 10
    carfuel -= 10 * 1.6
else:
    maxKm = carfuel / 1.6
    carkm += maxKm
    carfuel = 0
    print("There isn't enough fuel! Go to the nearest gas station!")
## Get a new passanger named "Kagan" there -> Tesla
passengers.append("Kagan")
## Move further 900 km
if (900 * 1.6 <= carfuel):
    carkm += 900
    carfuel -= 900 * 1.6
else:
    maxKm = carfuel / 1.6
    print("Maxkm: ",maxKm)
    carkm += maxKm
    carfuel = 0
    print("There isn't enough fuel! Go to the nearest gas station!")

##################

## Move 22 km with
carkm2 += 22
carfuel2 -= 22 * 5.6
## Get 26 lt fuel
carfuel2 += 26
## Move 17 km 
carkm2 += 17
carfuel2 -= 17 * 5.6
## Take 3 passangers -> "Mehmet" "Hatice" "Muhammet"
passengers2.append("Mehmet")
passengers2.append("Hatice")
passengers2.append("Muhammet")

print(f'--- Car {carName} ---\n| km: {carkm}\n| fuel: {carfuel}\n| Passengers: {passengers}')
print(f'--- Car {carName2} ---\n| km: {carkm2}\n| fuel: {carfuel2}\n| Passengers: {passengers2}')