import pandas as pd
import statsmodels.api as sm
import math

#load the data
loansData = pd.read_csv('loansData_clean.csv')

#Create a column called IR_TF to determine whether value is <12%
loansData['IR_TF'] = loansData['Interest.Rate'].map(lambda x: 0 if x < 12 else 1)

#Add constant intercept number of 1.0
loansData['Intercept'] = 1.0

#create list of column names including the intercept
ind_vars = ['Intercept','FICO.Score', 'Amount.Requested']

#define the logistic regression model
logit = sm.Logit(loansData['IR_TF'], loansData[ind_vars])

#fit the model
result = logit.fit()

#print the fitted coefficients
coeff = result.params
print coeff

#writing a function called logistic_function that returns p
def logistic_function(FICOScore, LoanAmount):
	#Fico coefficient, LoanAmt cooefficent, and intercept coefficient extracted from coeff
    FICO_coeff = coeff[0]
    LoanAmt_coeff = coeff[1]
    intercept = coeff[2]
    #print logistic function 
    p = 1/(1 + math.exp(-1*(intercept + FICO_coeff*FICOScore + LoanAmt_coeff*LoanAmount))
    print p

logistic_function(300, 10000)

    

