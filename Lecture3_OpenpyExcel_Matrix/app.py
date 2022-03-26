

col = 10
row = 12

values = []

# iterate rows
for i in range(row):
    # iterate cols
    newRow = []
    for j in range(col):
        newRow.append(0)

    values.append(newRow)


print("Values :",values)
