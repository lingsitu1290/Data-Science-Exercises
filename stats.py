# import pandas and scipy(for mode)
import pandas as pd
from scipy import stats


data = '''Region, Alcohol, Tobacco
North, 6.47, 4.03
Yorkshire, 6.13, 3.76
Northeast, 6.19, 3.77
East Midlands, 4.89, 3.34
West Midlands, 5.63, 3.47
East Anglia, 4.52, 2.92
Southeast, 5.89, 3.20
Southwest, 4.79, 2.71
Wales, 5.27, 3.53
Scotland, 6.08, 4.51
Northern Ireland, 4.02, 4.56'''

#split the string
data = data.splitlines()  # data.split('\n') why can i use? 

#split each item at the comma
data = [i.split(', ') for i in data]

#create panda dataframe
column_names = data[0] 
data_rows = data[1::] 
df = pd.DataFrame(data_rows, columns=column_names)

#convert the columns to float
df['Alcohol'] = df['Alcohol'].astype(float)
df['Tobacco'] = df['Tobacco'].astype(float)

#print the statements
print "Mean: ", df['Alcohol'].mean(), df['Tobacco'].mean()
print "Median: ", df['Alcohol'].median(), df['Tobacco'].median()
print "Mode: ", stats.mode(df['Alcohol']), stats.mode(df['Tobacco']) #why isn't the mode printing out?
#ModeResult(mode=array([ 4.02]), count=array([1])) ModeResult(mode=array([ 2.71]), count=array([1]))
print "Range: ", max(df['Alcohol']) - min(df['Alcohol']), max(df['Tobacco']) - min(df['Tobacco'])
print "Variance: ", df['Alcohol'].var(), df['Tobacco'].var()
print "Standard deviation: ", df['Alcohol'].std(), df['Tobacco'].std()