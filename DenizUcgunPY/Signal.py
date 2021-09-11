import math
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
import numpy as np

class Signal:

    letter2number = {
        "A" : 1,
        "B" : 2,
        "C" : 3,
        "D" : 4,
        "E" : 5,
        "F" : 6,
        "G" : 7,
        "H" : 8,
        "I" : 9,
        "J" : 10,
        "K" : 11,
        "L" : 12,
        "M" : 13,
        "N" : 14,
        "O" : 15,
        "P" : 16,
        "R" : 17,
        "S" : 18,
        "T" : 19,
        "U" : 20,
        "V" : 21,
        "X" : 22,
        "Y" : 23,
        "Z" : 24,
    }

    additionList = [12,6,3,1,1]

    def __init__(self,information,type,isContinous):
        self.information    = information
        self.type           = type
        self.isContinous    = isContinous
        self.signal = self.encode()

    def encode(self):
        signal = []
        for letter in self.information:
            signal += self.encondeLetter(letter)

        # print("Signal: ",signal)
        return signal

        

    def encondeLetter(self,letter): # Z

        number = self.letter2number[letter.upper()]  # 24
        # print(f"Number: {number}")
        bits = []  # 0 0 0 0 0
        addition = 0  # 21

        for i in range(5): # 4

            if i > 0:
                if bits[i-1] == 0:
                    addition += self.additionList[i-1]
                else:
                    addition += 0

            # print(f"i: {i} \ addition: {addition}")

            if number <= (addition + self.additionList[i]):  #  24 <= 21 + 2
                bits.append(1)
            else:
                bits.append(0)

        # print(bits)
        return bits

    def printSignal(self):
        print(f"Signal: {self.signal}")

    def showSignal(self):
        x = range(len(self.signal))
        y = self.signal

        plt.plot(x, y, 'o', color='black')
        plt.show()
        


# MAIN
signal1 = Signal("Emin","Bits",False)

signal1.printSignal()
signal1.showSignal()
        