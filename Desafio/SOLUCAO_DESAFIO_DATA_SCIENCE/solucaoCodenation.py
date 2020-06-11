import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import GridSearchCV
import matplotlib.pyplot as plt
import seaborn as sns

#Leitura dos datasets de treino e teste e criação do df de resposta
df_train = pd.read_csv('../TEST_FILES/train.csv')
df_test = pd.read_csv('../TEST_FILES/test.csv')
df_resposta = pd.DataFrame()

#verificar se os dados de teste estão nos dados de treinamento
print(set(df_test.columns).issubset(set(df_train.columns)))

# Correlação das tabelas
# Quanto mais próximo de 1, maior a correlação
df_train.corr()['NU_NOTA_MT'].dropna().sort_values(ascending=False)