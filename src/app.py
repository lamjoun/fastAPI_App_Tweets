import os
import re
import nltk
import pickle
import tensorflow as tf
tf.get_logger().setLevel('ERROR')

# Désactiver les avertissements généraux
import warnings
warnings.filterwarnings("ignore")

# Désactiver les avertissements de TensorFlow
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # Cela masque les logs d'erreur moins importants de TensorFlow
tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.ERROR)

# Désactiver les optimisations OneDNN
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

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

# Charger le modèle et le tokenizer
#model_file='model_files/model6.keras'  # ===> OK
#model_file='model_files/model7.keras'
#model_file='model7.keras'
model_file='model_files/model.keras'
tokenizer_file='model_files/tokenizer.pickle'

# Fonction pour charger le tokenizer
def load_tokenizer(file_path):
    with open(file_path, 'rb') as handle:
        try:
            tokenizer = pickle.load(handle)
        except ModuleNotFoundError as e:
            if 'keras.src.preprocessing' in str(e):
                import keras
                keras.utils.get_custom_objects()
                with open(file_path, 'rb') as handle:
                    tokenizer = pickle.load(handle)
            else:
                raise e
    return tokenizer

loaded_tokenizer = load_tokenizer(tokenizer_file)
#print('\n',"=======End loading tokenizer.pickle =================","\n")
loaded_model = tf.keras.models.load_model(model_file)

# Fonction de prédiction
def decode_sentiment(score):
    return "Positive" if score > 0.5 else "Negative"

def predict_sentiment(ijson_data, imodel, itokenizer):
    # Extraire le texte du tweet
    l_tweet = ijson_data["text"]

    # Prétraiter le tweet
    l_processed_tweet = preprocess(l_tweet)

    # Tokeniser et padding le tweet
    l_sequence = itokenizer.texts_to_sequences([l_processed_tweet])
    l_padded_sequence = pad_sequences(l_sequence, maxlen=MAX_SEQUENCE_LENGTH)

    # Faire la prédiction
    score = imodel.predict(l_padded_sequence, verbose=0)[0][0]

    # Décoder le sentiment
    sentiment = decode_sentiment(score)

    # Retourner le résultat
    return {"sentiment": sentiment, "score": score}

tweets = ["spring break plain city snowing",
	"yeeeees freaking handsome wait till new moon night museum 2",
	"Positive,working holla",
	"nooo danny kicked adam totally going win"
	]
    
tweets = []
# Tweet à prédire
for txt in tweets:
  print('\n', "========================")
  print(txt) 
  print(predict_sentiment({"text": txt}, loaded_model, loaded_tokenizer))
  print("========================", '\n')

#================================= ===============#
#======================= FastAPI ========== ===============#
#================================= ===============#
# Importer les bibliothèques nécessaires
#
import json
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
#

app = FastAPI()

# Définir un modèle Pydantic pour le corps de la requête
class Tweet(BaseModel):
    text: str

@app.get("/")
def read_root():
    return {"Hello": "World.....!!!!"}


@app.post("/predict")
async def prediction(input_parameters: Tweet):
    input_data = input_parameters.json()
    input_dictionary = json.loads(input_data)
    print(input_dictionary) 
    #
    #l_tweet_text = input_dictionary['text']

    #predict_sentiment = 1
    l_predict = predict_sentiment(input_dictionary,loaded_model, loaded_tokenizer)
    print(l_predict)
    #
    return {"sentiment": l_predict['sentiment']}



# Démarrer le serveur
if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=int(os.environ.get('PORT', 8000)))
