import pickle
from sklearn.pipeline import Pipeline
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
import numpy as np

def pred_sentiment_text(model, text):
    try:
        prediction = model.predict([text])
        print(prediction)
        if prediction == 0:
            return "negative"
        elif prediction == 2:
            return "neutral"
        elif prediction == 4:
            return "positive"
    except:
        return "error"

