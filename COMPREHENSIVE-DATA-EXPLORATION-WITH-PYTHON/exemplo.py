import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy.stats import norm
from sklearn.preprocessing import StandardScaler
from scipy import stats
import warnings
warnings.filterwarnings('ignore')
#%matplotlib inline

df_train = pd.read_csv('../TEST_FILES/train.csv')

df_train.columns

print(df_train['NU_NOTA_MT'].describe())

sns.distplot(df_train['NU_NOTA_MT'])

print("Skewness: %f" % df_train['NU_NOTA_MT'].skew())
print("Kurtosis: %f " % df_train['NU_NOTA_MT'].kurt())

plt.show()