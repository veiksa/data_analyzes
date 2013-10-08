import numpy as np


###reading the file in and deleting duplicates

#The path of the file has to start from 'current' directory
def file_import(file_path_string, output_name):
# dtype=None t2hendab, et v6etakse ka mitte numbrilised v22rtused
    columns = ['isolaadid','1','2','3','4','5','6','7']   
    output_name = np.genfromtxt(file_path_string, skip_header=1, dtype=None, delimiter=',', names=columns)
    #print output_name.shape

###find duplicates
    names=[]
    doble=[]
    for isolate_names in output_name:
        names.append(isolate_names[0])

    for index, name in enumerate(names):
        if names.count(name) > 1:
            doble.append((index,name))
    #print doble
#delete duplicates in imported files
    i=0
    for x in doble:
        output_name = np.delete(output_name, x[0]+i, axis=0)
        i = i-1
#output_name2 = np.delete(output_name2, (277), axis=0)
    isolates=[]
    isolates = np.append(isolates,output_name['isolaadid'])
    output_name = np.column_stack((output_name[columns[1]],output_name[columns[2]], output_name[columns[3]], output_name[columns[4]],output_name[columns[5]],output_name[columns[6]],output_name[columns[7]]))
###Output is a duple that has two numpy arrays in it. One is the isolate names and the other is OD values.
# The only way that I managed to make 1D array into a 2D array. I think it is easier to work with a 2D array.   
    return output_name, isolates 

zb = file_import('/home/lubuntu/pythonkursus/data_analyzes/example/andmefailid/ZB_OD.csv', 'ZB')[0]
amp100 = file_import('/home/lubuntu/pythonkursus/data_analyzes/example/andmefailid/amp100.csv', 'amp100')[0]
isolates = file_import('/home/lubuntu/pythonkursus/data_analyzes/example/andmefailid/ZB_OD.csv', 'ZB')[1]
print isolates

#isolates = []
#isolates = np.append(isolates,zb['isolaadid'])
#newzb = np.column_stack((zb['1'],zb['2'], zb['3'], zb['4'],zb['5'],zb['6'],zb['7']))
#print newzb[:10], newzb.shape, type(newzb)
#print isolates[:3],isolates.shape, type(isolates)
