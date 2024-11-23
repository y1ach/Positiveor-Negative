from textblob import TextBlob

sentence = input("Prompt: ")

blob = TextBlob(sentence)
sentiment = blob.sentiment.polarity

if sentiment < 0:
    print("Negative sentence")
    print("I am sorry about that, how can I help you?")
else:
    print("Positive sentence")
