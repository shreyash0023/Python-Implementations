import pylab as py

def fixedRatePayment (intR,periods,loan):
    payment =  loan * (intR / (1 - (1+intR)**-periods))
    return payment

def findPayments (loan,r,m) :
    '''returns the monthly payment for a mortgage of size loan at a monthly rate of r for m months'''
    return loan*((r*(1+r)**m)/((1+r)**m - 1))

class Mortgage(object):
    def __init__(self,loan,annRate,months):
        '''Create a new mortgage'''
        self.loan = loan
        self.rate = annRate / 12.0
        self.months = months
        self.paid = [0.0]
        self.owed = [loan]
        self.payment = findPayments(loan,self.rate,months)
        self.legend = None


    def makePayments(self):
        '''Make Payments'''
        self.paid.append(self.payment)
        reduction = self.payment - self.owed[-1] * self.rate
        self.owed.append(self.owed[-1] - reduction)

    def getTotalPaid(self):
        '''Return the total amound paid so far'''
        return sum(self.paid)

    def __str__(self):
        return self.legend

    def plotPayments(self,style):
        py.plot(self.paid[1:], style, label = self.legend)
        py.show()

    def plotBalance(self,style):
        py.plot(self.owed, style, label = self.legend)
        py.show()

    def plotTotPd(self,style):
        totPd = [self.paid[0]]
        for i in range(1,len(self.paid)):
            totPd.append(totPd[-1] + self.paid[i])
        py.plot(totPd,style, label = self.legend)
        py.show()


class Fixed(Mortgage):
    def __init__(self,loan,r,months):
        Mortgage.__init__(self,loan,r,months)
        self.legend = 'Fixed, ' + str(r*100) + '%'
        Mortgage.plotBalance(self,'ob')


class FixedWithPts(Mortgage):
    def __init__(self,loan,r,months,pts):
        Mortgage.__init__(self,loan,r,months)
        self.pts = pts
        self.paid = [loan*(pts/100.0)]
        self.legend = 'Fixed, ' + str(r*100) + '% ,' + str(pts) + ' points'


fx = Fixed(100,4,14)





