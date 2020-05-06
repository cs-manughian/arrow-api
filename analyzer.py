from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

def get_sentiment_scores(sentence):
    score = analyzer.polarity_scores(sentence)
    result = "{:-<40} {}".format(sentence, str(score))
    print(result)
    return(score)