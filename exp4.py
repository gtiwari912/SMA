# To Perform data cleaning on the social media data (Dataset will be provided)
# Dataset1: facebook.csv
import pandas as pd
#find null values
df=pd.read_csv("/content/facebook - facebook.csv")


df.head(10)


df.isnull().sum()


# show in heatmap
import seaborn as sns
sns.heatmap(df.isnull(), cbar=False)


#Fill null values by 0
import pandas as pd
df=pd.read_csv('/content/facebook - facebook.csv')
df.fillna(0)


#Fill null values by particular values
newdf = df.fillna(100)
print(newdf)


#Fill null values by forward fill method
print(df.fillna(method="ffill"))


#Fill null values by backward fill method
print(df.fillna(method="bfill"))
df.interpolate()


dfresult = df.dropna()
print(dfresult)


#Drop Duplicate values
df.drop_duplicates()
#drop if entire row is null
df = df.dropna(axis = 0, how = 'all')
print(df)








# Now for youtube dataset

import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
# Read the CSV file containing YouTube comments
df = pd.read_csv('YouTube_Comments_Sentiment.csv')
# Extract the 'Comments' column from the DataFrame
df_text = df[['Comments']]
# Convert all text to lowercase
df_text['Comments'] = df_text['Comments'].str.lower()
# Download the required NLTK resources
nltk.download('punkt')
nltk.download('stopwords')
# Define the list of English stopwords
en_stopwords = stopwords.words('english')
# Function to remove stopwords from text
def remove_stopwords(text):
  result = []
  for token in text:
    if token not in en_stopwords:
      result.append(token)
  return result
# Apply the remove_stopwords function to the 'Comments' column
df_text['Comments'] = df_text['Comments'].apply(nltk.word_tokenize)
df_text['Comments'] = df_text['Comments'].apply(remove_stopwords)
# Function to remove punctuation from text
def remove_punct(text):
  tokenizer = RegexpTokenizer(r"\w+")
  lst = tokenizer.tokenize(' '.join(text))
  return lst
# Apply the remove_punct function to the 'Comments' column
df_text['Comments'] = df_text['Comments'].apply(remove_punct)
