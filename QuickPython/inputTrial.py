import sys

print('Bu Program calisiyor!')

# for index in range(len(sys.argv)):

#     if index == 0:
#         continue

#     print(f"Index: {index}")
#     print(f"Value: {sys.argv[index]}")

# print("Emin","Basak","Deniz","Muart","Nihan",sep="\n")

isimler = ["Emin","Basak","Deniz"]

for isim in isimler:
    print(isim)

for i in range(len(isimler)):
    print(isimler[i])


