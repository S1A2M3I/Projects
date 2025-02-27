from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def analyze_sentiment(text):
    analyzer = SentimentIntensityAnalyzer()
    scores = analyzer.polarity_scores(text)
    if scores['compound'] > 0:
        return "Positive"
    elif scores['compound'] < 0:
        return "Negative"
    else:
        return "Neutral"

# Example usage
print(analyze_sentiment("The sales team is underperforming and failing to meet targets consistently. This is unacceptable."))
