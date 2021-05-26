import csv, time
import os
from operator import itemgetter


# Choix du fichier
file = input("Entrez le nom du fichier csv: ")

while not os.path.exists("data/"+ file + ".csv"):
    
    print("Fichier introuvable ou mauvais type de fichier")
    file = input("Entrez le nom du fichier csv: ")
    

# Démarrer chrono
start_time = time.time()

# Lecture du fichier excel
liste = []
with open("data/"+ file + ".csv", newline='') as csvfile:
    spamreader = csv.reader(csvfile)
    next(csvfile)
    for row in spamreader:
        info = ''.join(row).split(';')
        name, price, profit = str(info[0]), float(info[1]), float(info[2])
        if price > 0 and profit > 0:
            sum = price*profit/100
            ratio = price/sum
            dict = {'name': name, 'price': price, 'profit': sum, 'ratio': ratio}
            liste.append(dict)

# Trier le élémenents par ratio
ordered_list = sorted(liste, key=itemgetter('ratio'), reverse=False)

# Calcul du meilleur investissment
total = 0
list_buy = []
gain = 0
for action in ordered_list:
        name, price, profit = str((action["name"])), float(action["price"]), float(action["profit"])
        if total + price <= 500:
            total += price
            gain += profit
            list_buy.append(name)


print("Vous devez acheter des actions chez " + ', '.join(list_buy) + '.')
print("Avec un investissement de " + str(round(total, 2)) + " euros" + ',vous gagnerez ' + str(round(gain, 2)) + " euros")
print("--- %s seconds ---" % (time.time() - start_time))

