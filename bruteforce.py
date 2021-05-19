import csv
from itertools import combinations,chain


liste = []
with open('dataset.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile)
    next(csvfile)
    for row in spamreader:
        info = ''.join(row).split(';')
        sum = float(info[1])*(float(info[2])/100)
        dict = {'name': str(info[0]),'price': float(info[1]), 'profit': sum }
        liste.append(dict)


def subsets(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

li = subsets(liste)

total_final = 0
best_gain = 0
names = []
for i in li:
    total = 0
    gain = 0
    names.clear()
    for elem in i:
        if total + elem['price'] <= 500: 
           total += float(elem['price'])
           gain += float(elem['profit'])
           names.append(elem['name'])
 
    if gain > best_gain:
        total_final = total
        best_gain = gain
            
print(names)
print(str(best_gain))
print(str(total_final))