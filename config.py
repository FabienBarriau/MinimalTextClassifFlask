import pickle
import string
from flask import url_for
import random

SECRET_KEY = "".join([random.choice(string.printable) for _ in range(24)])

with open('App/static/pickle/model.pickle', 'rb') as handle:
    MODEL = pickle.load(handle)

with open('App/static/pickle/score.pickle', 'rb') as handle:
    SCORE = pickle.load(handle)

