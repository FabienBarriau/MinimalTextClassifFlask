from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from .utils import pred_sentiment_text
import os

app = Flask(__name__)

# Config options - Make sure you created a 'config.py' file.
app.config.from_object('config')
# To get one variable, tape app.config['MY_VARIABLE']

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form["text"]
        sentiment_pred = pred_sentiment_text(app.config["MODEL"], text)
        score = app.config["SCORE"]
        return render_template('index.html', text=text, sentiment_pred=sentiment_pred, score=score)
    elif request.method == 'GET':
        return render_template('index.html')

if __name__ == "__main__":
    app.run()