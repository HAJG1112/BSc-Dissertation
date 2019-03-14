from DataExtraction import data
from statsmodels.tsa.base.datetools import dates_from_str
import numpy as np
import pandas as pd
import statsmodels.api as sm
from statsmodels.tsa.api import VAR, DynamicVAR
import matplotlib.pyplot as plt
from statsmodels.tsa.vector_ar.vecm import coint_johansen
from sklearn import linear_model


def data():
    df = pd.read_excel(r'C:\Users\justi\Documents\DataMatrixDiss.xlsx',sheet_name='matrix', header=0)
    df = pd.DataFrame(df)
    return(df)


def residuals(X,Y):
    regr = linear_model.LinearRegression()
    Y_hat = regr.fit(X, Y)
    residuals = Y_hat - Y
    return(residuals)


df = data()
X = df['INF','RMRF', 'UER_change','IPI_change','PDI_change', 'PCE_change']
Y1 = df['CS_AAA_3MO']
Y2 = df['CS_AAA_5Y']
Y3 = df['CS_AAA_10Y']
Y4 = df['CS_AA_3MO']
Y5 = df['CS_AA_5Y']
Y6 = df['CS_AA_10Y']

r1 = (residuals(X,Y1))
r2 = (residuals(X,Y2))
print(r1,r2)



#regress columns 1-18 as they are dependent variable against macro variables in last 6 columns
#take the residuals of these regressions
#store them to be used for the covaraince matrix




