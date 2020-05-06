from flask import Flask
import importlib
import json

preprocessor = importlib.import_module('preprocessor')
analyzer = importlib.import_module('analyzer')

app = Flask(__name__)

@app.route('/')
def homepage():
    return 'welcome to the Arrow API! >------|>'

@app.route('/sentiment/<text>')
def get_sentiment(text):
    return json.dumps(analyzer.get_sentiment_scores(text))

@app.route('/process/<text>')
def process(text):
    return json.dumps(list(preprocessor.preprocess_input(text)))


if __name__ == '__main__':
    app.run(debug=True)