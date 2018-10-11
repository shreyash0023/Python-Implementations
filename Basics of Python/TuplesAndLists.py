# Tuples
#
t1 = (3.35,)
t2 = (1,'two',3)
t3 = (t1,'hellow')
print t1
print t2
print (t3 + t2)[3]

def findDivisors (n1,n2):
    '''Assume n1 and n2 are positive ints'''
    divisors = ()
    for x in range(1,min(n1,n2)+1):
        if n1%x == 0 and n2%x == 0:
            divisors = divisors + (x,)
    return divisors

divisors = findDivisors(20,100)

print divisors

total = 0
print divisors[0]
'''for x in range(0,len(divisors)):
    total += divisors[x]
'''


for x in divisors:
    total += x
    print total
'''Sequences and Multiple Assignments'''

def findExtremeDivisors(n1,n2):
    '''Assume that n1 and n2 are positive ints
    Returns a tuple containing the smallest common divisor > 1
    and the largest common divisor of n1 and n2'''
    divisor = ()
    minValue,maxValue = None, None
    for x in range(2,min(n1,n2)+1):
        if n1%x == 0 and n2%x == 0:
            if minValue == None or x < minValue:
                minValue = x
            if maxValue == None or x > maxValue:
                maxValue = x

    return (minValue,maxValue)

minDivisor, maxDivisor = findExtremeDivisors(100,200)

print minDivisor, maxDivisor


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






# Aliasing
'''Two distinct path to the same object'''
























