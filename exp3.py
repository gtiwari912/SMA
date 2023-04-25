# first scrape data from twitter
#the perform this ops on csv file
#View dimensions of dataset
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline
import warnings
warnings.filterwarnings('ignore')
data = 'filename.csv'
df = pd.read_csv(data)


df.shape


df.head()


#Summary of Dataset
df.info()


df.isnull().sum()


df.describe()


#Summary statistics of character columns
df.describe(include=['object'])


#Summary statistics of all the columns
df.describe(include='all')
