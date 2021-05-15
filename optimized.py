import csv
from operator import itemgetter


liste = []
with open('dataset.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile)
    next(csvfile)
    for row in spamreader:
        info = ''.join(row).split(';')
        if float(info[1]) > 0 and float(info[2]) > 0:
            sum = float(info[1])*float(info[2])/100
            ratio = (float(info[1]))/sum
            dict = {'name': str(info[0]), 'price': float(info[1]), 'profit': sum, 'ratio': ratio }
            liste.append(dict)
        
        
ordered_list = sorted(liste, key=itemgetter('ratio'), reverse=False)

total = 0
list_buy = [] 
gain = 0
for action in ordered_list:
    if action["name"] not in list_buy:   
        if  total + float(action["price"]) <= 500:
            total += float(action["price"])
            gain += float(action["profit"])
            list_buy.append(action["name"])
        
print("Vous devez acheter des actions chez " + ' ,'.join(list_buy) +'.' )
print("Avec un investissement de " + str(total) + " euros" +',vous gagnerez ' + str(round(gain, 2)) + " euros")
