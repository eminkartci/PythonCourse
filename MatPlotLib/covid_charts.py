
import matplotlib.pyplot as plt
import numpy as np

## read csv file
def readCSV(path):

    covidFile = open(path, encoding="utf-8", mode="r")

    covidFileList = covidFile.readlines()

    return covidFileList
    

def getDose1(covidList):

    dose1 = []
    for row in covidList[1::]:
        infoList = row.split(",")
        dose1.append(float(infoList[5]))

    return dose1

def getCities(covidList):

    cities = []
    for row in covidList[1::]:
        infoList = row.split(",")
        cities.append(infoList[3])

    return cities

def plot_dose1(cities,dose1):
    print("CTIES: ",cities)
    print("DOSE 1: ",dose1)
    plt.plot(cities,dose1)
    plt.show()
    


covidRows = readCSV("MatPlotLib/covid19Vaccination.csv")

dose1 = getDose1(covidRows)

cityList = getCities(covidRows)

plot_dose1(cityList,dose1)