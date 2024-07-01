import re
import nltk
import pickle
import tensorflow as tf
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
from tensorflow.keras.preprocessing.sequence import pad_sequences

stop_words = stopwords.words('english')
stemmer = SnowballStemmer('english')
text_cleaning_re = r"@\S+|https?:\S+|http?:\S|[^A-Za-z0-9]+"
MAX_SEQUENCE_LENGTH = 30

def preprocess(text, stem=False):
  text = re.sub(text_cleaning_re, ' ', str(text).lower()).strip()
  tokens = []
  for token in text.split():
    if token not in stop_words:
      if stem:
        tokens.append(stemmer.stem(token))
      else:
        tokens.append(token)
  return " ".join(tokens)

tt_test = "il est toujours @@@ nul !!!"
print('\n',"========================")
print(tt_test) 
print(preprocess(tt_test))
print("========================", '\n')
# Charger le modèle et le tokenizer
loaded_model = tf.keras.models.load_model('/content/drive/MyDrive/tmp/model.keras')

with open('/content/drive/MyDrive/tmp/tokenizer.pickle', 'rb') as handle:
  loaded_tokenizer = pickle.load(handl)


# ********** Fonction de prédiction

def decode_sentiment(score):
    return "Positive" if score>0.5 else "Negative"

def predict_sentiment(json_data, imodel=loaded_model,itokenizer=loaded_tokenizer):
    # Extraire le texte du tweet
    tweet = json_data["text"]

    # Prétraiter le tweet
    processed_tweet = preprocess(tweet)

    # Tokeniser et padding le tweet
    sequence = itokenizer.texts_to_sequences([processed_tweet])
    padded_sequence = pad_sequences(sequence, maxlen=MAX_SEQUENCE_LENGTH)

    # Faire la prédiction
    score = imodel.predict(padded_sequence, verbose=0)[0][0]

    # Décoder le sentiment
    sentiment = decode_sentiment(score)

    # Retourner le résultat
    return {"sentiment": sentiment, "score": score}

# Tweet à prédire
print('\n',"========================")
tt = "it's a beautiful @@day!!!!!"
print(tt)
print(predict_sentiment({"text":tt}))
print("========================", '\n')







