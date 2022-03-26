

# Car Class
class Car:

    ## Constructor
    def __init__(self, numberOfPassengersIn, gasolineCapacityIn, consumptionRateIn,averageSpeedIn, distanceTravelledIn):
        ## Attributes
        self.numberOfPassengers = numberOfPassengersIn
        self.gasolineCapacity = gasolineCapacityIn
        self.consumptionRate = consumptionRateIn
        self.averageSpeed = averageSpeedIn
        self.distanceTravelled = distanceTravelledIn

    ## Behaviors
    def move(self,hours):
        maxTravel = self.gasolineCapacity / self.consumptionRate
        distanceToTravel = hours * self.averageSpeed

        if(maxTravel >= distanceToTravel):
            spentGasoline = distanceToTravel * self.consumptionRate
            self.gasolineCapacity -= spentGasoline
            self.distanceTravelled += distanceToTravel
        else:
            self.distanceTravelled += maxTravel
            self.gasolineCapacity = 0
        
    def report(self):
        print(f"Distance Travelled: {self.distanceTravelled}")
        print(f"Remaining Gasoline: {self.gasolineCapacity}")

carObj = Car(2,100,0.4,60,100)
carObj2 = Car(1,200,5,100,30)

carObj.move(2)
carObj.report()

carObj2.move(2)
carObj2.report()