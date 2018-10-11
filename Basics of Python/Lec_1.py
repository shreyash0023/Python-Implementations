import pylab as py
principle = 1000
rate = 0.05
years = 20
values = []
year = []

for i in range(years+1):
    year.append(i)


for i in range(years+1):
    values.append(principle)
    principle += principle*rate

py.title('5% Growth, Compounded Annually')
py.xlabel('Years of Compounding')
py.ylabel('Value of Principle ($)')

py.plot(year, values, 'ob', linewidth = 1)
py.show()

print values

# The plot is showing the growth of an initial investment of 10k, at an annual compounding of 5 cent

