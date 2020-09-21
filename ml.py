import pandas as pd
import numpy as np
import sklearn

from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.pipeline import make_pipeline

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer

from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

from sklearn.base import TransformerMixin
    
from joblib import dump

df = pd.read_csv('FA-KES-Dataset.csv',encoding='latin1')
df.drop_duplicates(keep=False, inplace=True)
df['text'] = df['article_title'] + ' ' + df['article_content']

X = df["text"].values
y = df["labels"].values

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=345)


nb = make_pipeline(
    CountVectorizer(binary=True),
    MultinomialNB()
    
)

nb.fit(X_train, y_train)
y_pred = nb.predict(X_test)

print(classification_report(y_test, y_pred))
nb.fit(X, y)

dump(nb, "clf.joblib")
