import pandas as pd

df = pd.read_csv("input.txt", sep="   ", header=None)

dfv = df.iloc[:, 0]
dfh = df.iloc[:, 1]

sum = 0
count = 0
for a, x in dfv.items():
    for b, y in dfh.items():
        if x == y:
            count += 1
    sum += count * x
    count = 0

print(sum)