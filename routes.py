from flask import Flask

app = Flask(__name__)

@app.route('/')
def homepage():
    return 'welcome to the Arrow API\n>------|>'

@app.route('/analyze/<text>')
def analyze(text):
    print(text)
    import random
    mood = random.choice(['happy', 'sad', 'angry', 'upset'])
    sentence = random.choice([
        "Wow! You're really {} today!",
        "Huh... You seem pretty {}.",
        "Geez! No need to be so {}!",
        "You're totally {}. Why? You should write about it using Arrow!"
    ])
    return sentence.format(mood)

if __name__ == '__main__':
    app.run(debug=True)