import tweepy
import os

from google.cloud import language

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"KEY_PATH"

# This is the example provided in the natural language API documentation:
client = language.LanguageServiceClient()
text = ""
document = language.Document(content = text, type_= language.Document.Type.PLAIN_TEXT)

sentiment = client.analyze_sentiment(request={'document' : document}).document_sentiment

print("Text: {}".format(text))
print("Sentiment: {}, {}".format(sentiment.score, sentiment.magnitude))

# This is the next step to explore the npl api.



client = language.LanguageServiceClient()
text = """The Mona Lisa is a magnificent piece of work! It was created by Leonardo Da Vinci, an artist from Italy."""
document = language.Document(content = text, type_= language.Document.Type.PLAIN_TEXT)

entity_examples = client.analyze_entities(document=document, encoding_type='UTF32')
print("Notable figure: {0}".format(entity_examples))

client = language.LanguageServiceClient()
text = """What would a pie be classified as in this API? In addition, would it detect the number of pie is repeated, such as pie, pie, pie,
or would it return nothing in this field? Google Cloud Storage was something I wanted to use but could not get to work within
this program. Here is a test to see if it can detect the word 'Rome'. Interesting to note how the word 'program' trends on the negative
sentiment scale rating. """
document = language.Document(content = text, type_= language.Document.Type.PLAIN_TEXT)

entity_sentiment = client.analyze_entity_sentiment(document=document, encoding_type="UTF32")
print("Combining the two: {0}".format(entity_sentiment))


