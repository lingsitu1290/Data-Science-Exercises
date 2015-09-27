''' Load the Lending Club Statistics.

Use income (annual_inc) to model interest rates (int_rate).

Add home ownership (home_ownership) to the model.

Does that affect the significance of the 
coefficients in the original model? + Try to add the 
interaction of home ownership and incomes as a term. 
How does this impact the new model?
'''

import pandas as pd
import statsmodels.formula.api as smf
import numpy as np


loansData = pd.read_csv(('LoanStats3c.csv'), nrows = 1000, skiprows=1)


#Select specific columns into subdata
subdata = pd.DataFrame(columns=['Interest.Rate', 'Annual.Income', 'Home'])
subdata['Interest.Rate'] = loansData.int_rate
subdata['Annual.Income'] = loansData.annual_inc.astype(float)
subdata['Home'] = loansData.home_ownership

#Intercept set to 1.0
subdata['Intercept'] = float(1.0)

#Clean data but replacing na and removing % from interest.rate column
subdata.dropna(inplace=True)
subdata['Interest.Rate'] = map(lambda x: float(x.rstrip('%')), subdata['Interest.Rate'])


#1annual_inc to model int_rate and print the coefficients
est = smf.ols(formula='int_rate ~ 1 + annual_inc', data=loansData).fit()
print est.params[0]


#2. Add home ownership to annual_inc to model int_rate and print the coefficients
est2 = smf.ols(formula='int_rate ~ 1 + home_ownership + annual_inc', data=loansData).fit()
print est2.params[0]

