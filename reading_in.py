#import pandas as pd
import numpy as np


###reading the file in and deleting duplicates

#The path of the file has to start from 'current' directory
def file_import(file_path_string, output_name):
# dtype=None t2hendab, et v6etakse ka mitte numbrilised v22rtused
    output_name = np.genfromtxt(file_path_string, dtype=None, delimiter=',', names=True)

###find duplicates
    names=[]
    doble=[]
    for isolate_names in output_name:
        names.append(isolate_names[0])

    for index, name in enumerate(names):
        if names.count(name) > 1:
            doble.append((index,name))

#delete duplicates in imported files
    i=0
    for x in doble:
        output_name = np.delete(output_name, x[0]+i, axis=0)
        i = i-1
#output_name2 = np.delete(output_name2, (277), axis=0)
    return output_name

zb = file_import('/home/lubuntu/pythonkursus/data_analyzes/example/andmefailid/ZB_OD.csv', 'ZB')

#nimed2=[]
#doble2=[]
#for andmed in output_name2:
#    nimed2.append(andmed[0])
#
#for index, nimi in enumerate(nimed2):
#    if nimed2.count(nimi) > 1:
#        doble2.append((index,nimi))
#print 'Topelt kirjed arrays output_name2', doble2
#print len(output_name2), len(output_name)