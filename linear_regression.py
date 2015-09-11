import numpy as np
import pandas as pd
import statsmodels.api as sm

loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')


# Clean Interest Rate column by removing %
loansData['Interest.Rate'] = loansData['Interest.Rate'].map(lambda x: float(x.rstrip('%')))

# Clean Loan Length by removing months
loansData['Loan.Length'] = loansData['Loan.Length'].map(lambda x: float(x.rstrip(' months')))

# Clean Fico Range and get lower number and set to new column FICO Score
loansData['FICO.Score'] = loansData['FICO.Range'].map(lambda x: float(x.split('-')[0]))

intrate = loansData['Interest.Rate']
loanamt = loansData['Amount.Requested']
fico = loansData['FICO.Score']

# Reshaping the Data
# The dependent variable
y = np.matrix(intrate).transpose()
# The independent variables shaped as columns
x1 = np.matrix(fico).transpose()
x2 = np.matrix(loanamt).transpose()

# Create input matrix
x = np.column_stack([x1,x2])

# Create linear model
X = sm.add_constant(x)
model = sm.OLS(y,X)
f = model.fit()

# Output the results summary 
print f.summary()

loansData.to_csv('loansData_clean.csv', header=True, index=False)
