

# Car Object
class Car:
    numberOfPassengers  = 0
    gasolineCapacity    = 0
    consumptionRate     = 0
    averageSpeed        = 0
    distanceTravelled   = 0

    def __init__(self, numberOfPassengersIn, gasolineCapacityIn, consumptionRateIn,averageSpeedIn, distanceTravelledIn):
        self.numberOfPassengers = numberOfPassengersIn
        self.gasolineCapacityIn = gasolineCapacityIn
        self.consumptionRateIn = consumptionRateIn
        self.averageSpeedIn = averageSpeedIn
        self.distanceTravelledIn = distanceTravelledIn

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
        