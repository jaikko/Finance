import csv
import time
from itertools import combinations, chain

# Démarrer le chrono
start_time = time.time()

liste = []

# Lecture du fichier csv
with open('data/dataset.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile)
    next(csvfile)
    for row in spamreader:
        info = ''.join(row).split(';')
        sum = float(info[1])*(float(info[2])/100)
        dict = {'name': str(info[0]), 'price': float(info[1]), 'profit': sum}
        liste.append(dict)


# Fonction pour générer toutes les combinaisons
def subsets(liste):
    return chain.from_iterable(combinations(liste, r) for r in range(len(liste)+1))


# Générer les combinaisons à partir d'une liste
combi = subsets(liste)

total_final = 0
best_gain = 0
names = []
buy = []

#  Obtenir le meilleur investissement
for i in combi:
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
        buy = names

print("Vous devez acheter des actions chez " + ', '.join(buy) + '.')
print("Avec un investissement de " + str(round(total_final, 2)) + " euros" + ',vous gagnerez ' + str(round(best_gain, 2)) + " euros")
print("--- %s seconds ---" % (time.time() - start_time))
