import re
import pickle
from nltk.corpus import wordnet
from sklearn.feature_extraction.text import CountVectorizer

import nltk

nltk.download('wordnet')
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')

# Importamos el lemmatizar de NLTK, y creamos el objeto
from nltk.stem import WordNetLemmatizer
wordnet_lemmatizer = WordNetLemmatizer()

# Creamos el objeto stopwords
stopwords = nltk.corpus.stopwords.words('english')

def get_wordnet_pos(word):
  tag = nltk.pos_tag([word])[0][1][0].upper()
  tag_dict = {
    "J": wordnet.ADJ,
    "N": wordnet.NOUN,
    "V": wordnet.VERB,
    "R": wordnet.ADV
  }

  return tag_dict.get(tag, wordnet.NOUN)

def preprocesar_texto(texto):
  # Estos son cambios necesarios en el texto ingresado para que el modelo haga la mejor prediccion
  with open('/home/rickhersd2002/projects/Marke_Analysis_Project_Google/server/ML_models/cou_vec_entrenado.pkl', 'rb') as f:
    cou_vec = pickle.load(f)

  texto = re.sub("[^a-zA-Z]"," ",str(texto))
  texto = texto.lower()
  texto = nltk.word_tokenize(texto)
  texto = [word for word in texto if len(word)>3]
  texto = [word for word in texto if not word in stopwords]
  texto = [wordnet_lemmatizer.lemmatize(w, get_wordnet_pos(w)) for w in texto]
  texto = " ".join(texto)
  texto = [texto]
  matriz_texto = cou_vec.transform(texto)

  return matriz_texto

def predecir_texto (texto):
  # Obtener la predicción del modelo

  # Cargar el vector guardado
  with open('/home/rickhersd2002/projects/Marke_Analysis_Project_Google/server/ML_models/modelo_scoring.pkl', 'rb') as f:
    modelo = pickle.load(f)

  prediction = modelo.predict(preprocesar_texto(texto))

  # Imprimir el resultado en el formato deseado
  if prediction == 0:
    return "La reseña es mala"
  else:
    return "La reseña es buena"

