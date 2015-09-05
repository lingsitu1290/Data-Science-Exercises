
import collections
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

#data
x = [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 4, 4, 4, 4, 5, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 9, 9]

c = collections.Counter(x)
print c

# calculate the number of instances
count_sum = sum(c.values())

for k,v in c.iteritems():
  print "The frequency of number " + str(k) + " is " + str(float(v) / count_sum)

#save boxplot
p1 = plt.figure(1)
plt.boxplot(x)
p1.savefig('prob-boxplot.png')

#save histogram
p2 = plt.figure(2)
plt.hist(x)
p2.savefig('prob-hist.png')

#save qqplot
p3 = plt.figure(3)
stats.probplot(x, dist="norm", plot=plt)
p3.savefig('prob-qq.png')

plt.show()