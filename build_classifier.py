import pickle
from sklearn.pipeline import Pipeline
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
import numpy as np

print("## TRAIN")
df = pd.read_csv("train.csv", header=None, encoding='latin1')
X_train = df.values[:, 5]
y_train = df.values[:, 0]
y_train = y_train.astype('int')

text_clf = Pipeline([('vect', CountVectorizer()),('tfidf', TfidfTransformer()),('clf', MultinomialNB()),])
text_clf.fit(X_train, y_train)

with open("App/static/pickle/model.pickle", 'wb') as handle:
    pickle.dump(text_clf, handle, protocol=pickle.HIGHEST_PROTOCOL)

print("## TEST")
df = pd.read_csv("test.csv", header=None, encoding='latin1')
X_test = df.values[:, 5]
y_test = df.values[:, 0]
y_test= y_test.astype('int')

predicted = text_clf.predict(X_test)
score = np.mean(predicted == y_test)

print(score)

with open("App/static/pickle/score.pickle", 'wb') as handle:
    pickle.dump(score, handle, protocol=pickle.HIGHEST_PROTOCOL)