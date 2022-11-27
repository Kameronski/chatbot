from newspaper import Article
from textblob import TextBlob
import nltk

def open_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as infile:
        return infile.read()


#openai.api_key = open_file('openaiapikey.txt')

url = "https://www.newyorker.com/magazine/2022/10/24/how-a-tycoon-linked-to-chinese-intelligence-became-a-darling-of-trump-republicans"
article = Article(url)
article.download()
article.parse()
article.nlp()
print(article.text)
print("\nAuthor\n")
print(article.authors)
summary = article.summary
print(summary)
print("\n\nSummary:\n")
blob = TextBlob(summary)
sentiment = blob.sentiment.polarity # -1 to 1
print(sentiment)
