

# Car Object
class Car:

    def __init__(self, numberOfPassengersIn, gasolineCapacityIn, consumptionRateIn,averageSpeedIn, distanceTravelledIn):
        self.numberOfPassengers = numberOfPassengersIn
        self.gasolineCapacity = gasolineCapacityIn
        self.consumptionRate = consumptionRateIn
        self.averageSpeed = averageSpeedIn
        self.distanceTravelled = distanceTravelledIn

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
        print("Distance Travelled: " + distanceTravelled)
        print("Remaining Gasoline: " + gasolineCapacity)