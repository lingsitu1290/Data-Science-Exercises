import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats

#reads the load data and load into pandas Dataframe
loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')

#Cleaning the data - removing rows with null values
loansData.dropna(inplace=True)

#generate boxplot
loansData.boxplot(column='Amount.Requested')
plt.show()

#generate histogram
loansData.hist(column='Amount.Requested')
plt.show()

#generate QQplot
plt.figure()
graph = stats.probplot(loansData['Amount.Requested'], dist="norm", plot=plt)
plt.show()