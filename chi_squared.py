from scipy import stats
import pandas as pd
import collections
import matplotlib.pyplot as plt

# Load data
loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')

# Removes Na values cleaning data
loansData.dropna(inplace=True)

freq = collections.Counter(loansData['Open.CREDIT.Lines'])

# chi-squared testing
chi, p = stats.chisquare(freq.values())
print "The chi-squared is:" + str(chi)
print "The p-value is:" + str(p)