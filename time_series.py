import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import statsmodels.api as sm
%matplotlib inline

df = pd.read_csv('LoanStats3c.csv', header=1, low_memory=False)

# converts string to datetime object in pandas:
df['issue_d_format'] = pd.to_datetime(df['issue_d']) 
dfts = df.set_index('issue_d_format') 
year_month_summary = dfts.groupby(lambda x : x.year * 100 + x.month).count()
loan_count_summary = year_month_summary['issue_d']


# plot loan_count_summary 
plt.plot(loan_count_summary)

#This is not a stationary time series because the data changes with time 

#How do we go about making it stationary?? Smoothing out the data? 

#ACF 
acf = sm.graphics.tsa.plot_acf(loan_count_summary)

#PACF
sm.graphics.tsa.plot_pacf(loan_count_summary_diff)