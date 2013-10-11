import numpy as np
import matplotlib.pyplot as plt


###reading the file in and deleting duplicates
def find_duplicates(duplicates_from):
    names=[]
    duplicate_output=[]
    for isolate_names in duplicates_from:
        names.append(isolate_names[0])

    for index, name in enumerate(names):
        if names.count(name) > 1:
            duplicate_output.append((index,name))
    return duplicate_output
    
    
def delete_lines(tupleofindex, delete_from):
    i=0
    for x in tupleofindex:
        delete_from = np.delete(delete_from, x[0]+i, axis=0)
        i = i-1
    return delete_from
#The path of the file has to start from 'current' directory
def file_import(file_path_string, output_name):
# dtype=None t2hendab, et v6etakse ka mitte numbrilised v22rtused
    columns = ['isolaadid','1','2','3','4','5','6','7']   
    output_name = np.genfromtxt(file_path_string, skip_header=1, dtype=None, delimiter=',', names=columns)
    #print output_name.shape

#    print find_duplicates(output_name)
#    print doble
#delete duplicates in imported files
    output = delete_lines(find_duplicates(output_name),output_name)
#output_name2 = np.delete(output_name2, (277), axis=0)
    isolates=[]
    isolates = np.append(isolates,output['isolaadid'])
    output = np.column_stack((output[columns[1]],output[columns[2]], output[columns[3]], output[columns[4]],output[columns[5]],output[columns[6]],output[columns[7]]))
###Output is a duple that has two numpy arrays in it. One is the isolate names and the other is OD values.
# The only way that I managed to make 1D array into a 2D array. I think it is easier to work with a 2D array.   
    return output, isolates 

zb = file_import('/home/lubuntu/pythonkursus/data_analyzes/example/andmefailid/ZB_OD.csv', 'ZB')[0]
amp100 = file_import('/home/lubuntu/pythonkursus/data_analyzes/example/andmefailid/amp100.csv', 'amp100')[0]
isolates = file_import('/home/lubuntu/pythonkursus/data_analyzes/example/andmefailid/ZB_OD.csv', 'ZB')[1]

x = [1,2,3,4,5,6,7]

#for n in zb:
#    line, = plt.plot(x, n, linewidth=2)
#plt.show()

a = 4

index005 = zb <= 0.05


 


print 'enne jagamist', amp100[a]

#jagab AB OD v22rtuse kontrolli OD v22rtusega. Eelnevalt on kontrolli v22rtused,
#mis on <= 0.05 muudetud kymneks
for i in range(amp100.shape[0]):
    for j in range(amp100.shape[1]):
        amp100[i,j] = amp100[i,j] / zb[i,j]
print 'peale jagamist', amp100[a]


not_growing = []
j=0
for index, i in enumerate(index005):
    if True == i[-2]:
        not_growing.append((index, isolates[index]))
        line, = plt.plot(x, zb[index], linewidth=2)
        j= j+1

isolates = delete_lines(not_growing, isolates)
zb = delete_lines(not_growing, zb)
amp100 = delete_lines(not_growing, amp100)
print amp100.shape

def biggest_inhibition(seriespoint_array):
    onepoint_array = np.array([])
    for n in seriespoint_array:
        onepoint_array = np.append(onepoint_array, np.nanmin(n))
    return onepoint_array

print (biggest_inhibition(amp100))

#amp100new = np.array([])
#for n in amp100:
#    amp100new = np.append(amp100new, np.nanmin(n))
#print amp100new.shape    

#print zb.shape
