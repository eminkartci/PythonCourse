import sys

print('Bu Program calisiyor!')

for index in range(len(sys.argv)):

    if index == 0:
        continue

    print(f"Index: {index}")
    print(f"Value: {sys.argv[index]}")



