

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

    def __init__(self,information,type,isContinous):
        self.information    = information
        self.type           = type
        self.isContinous    = isContinous

    def encode(self):
        pass

    def encondeLetter(self,letter):
        
        number = self.letter2number[letter.upper()]
        bits = []
        if number <= (len(self.letter2number)/2):
            bits.append(1)
        else:
            bits.append(0)

        print(bits)
        


# MAIN
signal1 = Signal("Emin","Bits",False)

signal1.encondeLetter("E")
        
        