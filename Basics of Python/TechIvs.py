'''Lists and Mutability'''
'''Lists are mutable,tuples and strings are not'''

'''id(), which returns a unique integer identifier for an object, this function is used to test for
object equality'''
# . append()

Techs = ['MIT', 'Caltech']
Ivys = ['Harvard', 'Yale', 'Brown']

Univs = [Techs, Ivys]
Univs1 = [['MIT', 'Caltech'], ['Harvard', 'Yale', 'Brown']]

print 'Unvis ->', Univs
print 'Unvis1 ->', Univs1
print Univs1 == Univs

'''id's of the objects'''
print id(Univs)
print id(Univs1)

# .append() in Lists
Techs.append('RPI')
'''Does not create a new list, it mutates the current list'''

'''List concatenation'''

L1 = [1,2,3]
L2 = [4,5,6]
L3 = L1+L2
print L3
L1.extend(L2)
print L1
L1.append(L2)
print L1

'''CLONING'''

def removeDups (L1,L2):
    for x in L1:
        if x in L2:
            L1.remove(x)

L1 = [1,2,3,4]
L2 = [1,2,5,6]

removeDups(L1,L2)
print L1

L0 = [4,5,6,7,8]
L0.insert(1,100)
print L0

L1 = [1,2,3,4]
L2 = [1,2,5,6]
def removeDupsMod(L1,L2):
    for x in L1[:]:
        '''List slicing [:], creates a copy of the whole list'''
        if x in L2:
            L1.remove(x)


removeDupsMod(L1,L2)
print L1






