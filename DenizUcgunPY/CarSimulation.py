
from Car import Car

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



