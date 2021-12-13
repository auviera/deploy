from sklearn import datasets
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import numpy as np

def year_prediction(tahun):

    df_malay = pd.read_csv('malaysia.csv')
    df_malay.rename(columns={'Category':'Year'}, inplace=True)
    df_malay.dropna(inplace=True)

    #hapus data outlier dari kolom Annual Mean
    df_malay = df_malay.replace((df_malay[df_malay['Annual Mean']>26.1]).values, df_malay['Annual Mean'].mean())

    X = df_malay.iloc[:,0]
    y = df_malay.iloc[:,2]

    X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3)
    X_test = np.array(tahun)

    regressor = LinearRegression()
    regressor.fit(X_train.values.reshape(-1, 1), y_train)

    return regressor.predict(X_test.reshape(-1, 1))



