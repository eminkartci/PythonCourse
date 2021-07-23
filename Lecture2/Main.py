from Car import Car

car_1 = Car(5, 120, 0.01, 100, 0)
car_2 = Car(2, 120, 0.1, 100, 0)

for i in range(1,5):
    car_1.move(1)
    car_1.report()
    car_2.move(i)
    car_2.report()
