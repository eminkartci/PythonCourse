# Emin Kartcı Quick Python Course
# # This program prints several lines.


# Question 1
#################
# name = "Emin"
# content = f"""
#  /\\_/\\
# / oo  \\ 
# \\  ~  / 
# Hello “{name}”!
# """
#################

# print(content)

# Question 2
#################
# s0 = 12
# v0 = 3.5
# a = 9.8
# t = 10

# s0,v0,a,t = 12,3.5,9.8,10

# S = s0 + v0 * t + 1/2 * a * (t**2)

# print(f"The value of s is {S}")
#################

## Question 3

#################

place = ["Taşdelen","Çekmeköy","Üsküdar","Kadıköy"]
rent  = [1300,1500,1800,2000]
monthlyContRate = 0.10
friendCount = 3
monthlyCont = []
unitCost = []

## Calculate aidat
for r in rent:
    x = r*monthlyContRate
    monthlyCont.append(x) # %10 of rent is monthly contribution

for i in range(len(place)):
    cost = (rent[i]+monthlyCont[i])/friendCount
    unitCost.append(cost)

for i in range(len(place)):
    content = f"{place[i]}: {unitCost[i]}"
    print(content)

#################


