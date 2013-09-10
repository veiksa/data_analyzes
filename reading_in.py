import pandas as pd
import numpy as np


###reading the file in
# faili teekond peab algama kaustast, kus sa praegu asud, muidu python ei suuda seda leida; turvalisuse t6ttu.

np.genfromtxt
# dtype=None t2hendab, et v6etakse ka mitte numbrilised v22rtused
isolaadid = np.genfromtxt('/home/lubuntu/pythonkursus/data_analyzes/example/andmefailid/ZB_OD.csv', dtype=None, delimiter=',', names=True)

isolaadid2 = np.genfromtxt('/home/lubuntu/pythonkursus/data_analyzes/example/andmefailid/ZB_OD.csv', dtype=None, delimiter=',', names=True)

#print isolaadid
###get rid of duplicates
nimed=[]
doble=[]
for andmed in isolaadid:
    nimed.append(andmed[0])

for index, nimi in enumerate(nimed):
    if nimed.count(nimi) > 1:
        doble.append((index,nimi))
print 'Topelt kirjed arrays isolaadid', doble


i=0
for x in doble:
    isolaadid2 = np.delete(isolaadid2, x[0]+i, axis=0)
    i = i-1
#isolaadid2 = np.delete(isolaadid2, (277), axis=0)
print isolaadid2[277]


nimed2=[]
doble2=[]
for andmed in isolaadid2:
    nimed2.append(andmed[0])

for index, nimi in enumerate(nimed2):
    if nimed2.count(nimi) > 1:
        doble2.append((index,nimi))
print 'Topelt kirjed arrays isolaadid2', doble2
print len(isolaadid2), len(isolaadid)