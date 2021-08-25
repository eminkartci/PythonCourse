
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

## Move 10 km with Tesla
carkm += 10
carfuel -= 10 * 1.6
## Get a new passanger named "Kagan" there -> Tesla
passengers.append("Kagan")
## Move further 900 km
carkm += 900
carfuel -= 900 * 1.6

##################

## Move 22 km with
carkm2 += 22
carfuel2 -= 22 * 5.6
## Get 26 lt fuel
carfuel += 26
## Move 17 km 
carkm2 += 17
carfuel2 -= 17 * 5.6
## Take 3 passangers -> "Mehmet" "Hatice" "Muhammet"
passengers2.append("Mehmet")
passengers2.append("Hatice")
passengers2.append("Muhammet")

