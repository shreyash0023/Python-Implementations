def applyToEach(L,f):
    '''Assume L is a list, f is a function'''
    '''Mutates L by replacing each element, e, of L by f(e)'''
    for x in range(len(L)):
        L[x] = f(L[x])

L = [1,-2,3.3]
applyToEach(L,abs)
print L


L = [-11,-2,3.3]

map(abs,L)
print L

