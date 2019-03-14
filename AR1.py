import pandas as pd
from statsmodels.tsa.api import VAR
from statsmodels.tsa.api import AR
import numpy as np



def data():
    df = pd.read_excel(r'C:\Users\justi\Documents\DataMatrixDiss.xlsx',sheet_name='matrix', header=0)
    df = pd.DataFrame(df)
   # df['date'] = pd.to_datetime(df.Date_Time, format='%d/%m/%Y %H.%M.%S')
   # df = df.drop(['date'], axis=1)
   # df = df.Date_Time
    return(df)

def difference(X):
    X = X.diff(periods=1,axis=0)
    return X

def get_data(X):
    for i in range(1,20):
        columns = X.iloc[:,:i]
    return (columns)


def common_shocks(X):

        mod = AR(X)
        res = mod.fit(1)
        res= res.params
        return (res)


#def VAR(X):

#    model = VAR(X)
#    results = model.fit(4)
#    results = results.params
#    return results



#this finds the optimal lag for the VAR series

X = data()
X = X[['CS_BHY_3MO','3MO_TY']]
N = 10
BIC = np.zeros((N, 1))

for i in range(N):
    model = VAR(X)
    model = model.fit(i + 1)
    BIC[i] = model.bic
    results = model.summary()


BIC_min = np.min(BIC)
model_min = np.argmin(BIC)

print('Relative Likelihoods')
print(np.exp((BIC_min - BIC) / 2))
print('Number of parameters in minimum BIC model %s' % (model_min + 1))
print(results)



