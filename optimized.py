import csv
import time
import os
import math

# A Dynamic Programming based Python

# Choix du fichier
file = input("Entrez le nom du fichier csv: ")

while not os.path.exists("data/" + file + ".csv"):
    print("Fichier introuvable ou mauvais type de fichier")
    file = input("Entrez le nom du fichier csv: ")

# Variable
names = []
prices = []
profits = []

# Démarrer chrono
start_time = time.time()

# Lecture du fichier excel
with open("data/" + file + ".csv", newline='') as csvfile:
    spamreader = csv.reader(csvfile)
    next(csvfile)
    for row in spamreader:
        info = ''.join(row).split(';')
        name, price, price_wr, profit = str(info[0]), math.floor(float(info[1])), float(info[1]), float(info[2])
        if price > 0 and profit > 0:
            names.append(name)
            prices.append(price)
            profits.append(math.floor(price_wr * profit/100))


# Fonction  pour calculer le meilleur gain
def knapSack(W, prices, profits, n):
    # Création du tableau K[][]
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]

    for i in range(n + 1):
        for w in range(W + 1):

            if i == 0 or w == 0:
                K[i][w] = 0

            elif prices[i-1] <= w:
                K[i][w] = max(profits[i-1] + K[i-1][w-prices[i-1]], K[i-1][w])
            else:
                K[i][w] = K[i-1][w]
    return K, K[n][W]


W = 500
n = len(names)

# Obtenir le meilleur gain
K, gain = knapSack(W, prices, profits, n)
print("Gain: " + str(gain) + " euros")

w = W
total = 0
buy = []

# Récuper la somme investie et le nom des actions
for i in range(n, 0, -1):
    if gain <= 0:
        break

    if gain == K[i - 1][w]:
        continue
    else:
        total += prices[i - 1]
        buy.append(names[i - 1])
        gain = gain - profits[i - 1]
        w = w - prices[i - 1]

print("Somme investie : " + str(total) + " euros")
print("Action(s) : " + ", ".join(buy))
print("--- %s seconds ---" % (time.time() - start_time))
