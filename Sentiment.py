from textblob import TextBlob
def AI(text):
    blob=TextBlob(text)
    polarity=blob.sentiment.polarity
    if polarity>0:
        sentiment='positive'
    elif polarity<0:
        sentiment='negative'
    else:
        sentiment='neutral'

    print(sentiment,polarity)   

text=input('enter your text!')
AI(text)





