L1 = ['Hello\tWorld','My\tName\tis\tKhan']
L2 = ['Hello World','My Name is Khan']


for x in L1:
    x.split('\t')

L3 = []
'''List Comprehension for spliting with delimiter'''
L2 = [x.split(' ') for x in L2]
L1 = [x.split('\t') for x in L1]

L1_new = []

print L1
for x in range(len(L1)):
    new_str =""
    for y in range(len(L1[x])):
        new_str += L1[x][y]
        new_str += " "
    L1_new.append(new_str)


#print L2
#print L1
print L1_new


'''''
for x in range(len(L2)):
    L3.append(L2[x].split(' '))


print L1
print L2
print L3
'''''

list = ['element1\t0238.94', 'element2\t2.3904', 'element3\t0139847']
newList=[]
for i in list:
    newList.append(i.split('\t')[0])

#print newList