
import pandas as pd
import numpy as np
from statsmodels.tsa.arima_model import ARIMA


def data():
    df = pd.read_excel(r'C:\Users\justi\Documents\DataMatrixDiss.xlsx',sheet_name='matrix', header=0)\

    df = pd.DataFrame(df)
    return(df)

def AR1(X):

    columns = list(X)

    for column in columns:
        model = ARIMA(X[column].values, order=(1,0,0))
        model_fit = model.fit(disp=0)
    return model_fit.summary()




def dat1(X):
        mean = X.mean(axis=0)
        sigma = np.std(X,axis=0)
        min = (X.min(axis=0))
        max = (X.max(axis=0))
        #AR1 = AR1()
        X = pd.concat([mean, sigma, min, max], axis=1)
        return (X)

X = data()
X = X.drop(X.columns[0],axis=1) # to drop datetime string as not important

print(AR1(X))
# this doesnt return an ARIMA model result summary for each column, why?
