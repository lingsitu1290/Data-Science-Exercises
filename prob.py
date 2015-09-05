import matplotlib.pyplot as plt
import collections
import numpy as np 
import scipy.stats as stats

#data list
testlist = [1, 4, 5, 6, 9, 9, 9]

c = collections.Counter(testlist)

print c

# output the frequencies 
count_sum = sum(c.values())

for k,v in c.iteritems():
  print "The frequency of number " + str(k) + " is " + str(float(v) / count_sum)


#create boxplot
''' plt.boxplot(testlist)
plt.savefig("boxplot.png")
'''

#create histogram
''' plt.hist(testlist, histtype='bar')
plt.savefig("histogram.png")
plt.show()
'''

#create qq plot
plt.figure()
test_data2 = np.random.uniform(size=1000)   
graph2 = stats.probplot(testlist, dist="norm", plot=plt)
plt.savefig("qqplot.png") 
plt.show()