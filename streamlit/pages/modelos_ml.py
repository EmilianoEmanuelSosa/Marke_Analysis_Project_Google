import streamlit as st
import pickle
import sklearn
import nltk
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
import re


# Cargar el modelo desde el archivo .pkl
with open('modelo_scoring.pkl', 'rb') as file:
    modelo = pickle.load(file)

def modelo():
    st.subheader("**Modelo de clasificación**")
    st.write("""Se utiliza un modelo de procesamiento de lenguaje natural , en este caso (random forest classifier) , en el que 
             recibira un parametro (la reseña de un usuario) y la clacificara en 3 categorias (mala, neutral, buena). Lo interesante 
             de toda la etapa del proceso , es, como se preproceso las reseñas para que el modelo pueda interpretarlas y en base a las 
             palabras normalizadas y vectorizadas  , tomar una decision""")

def preparacion():
    st.subheader("**Preparación del modelo**")    
    st.markdown("""Se comenzó con un preprocesamiento de los datos que manejaría el modelo, el cual consistió de los siguientes pasos:
             """)
    st.image("flujo_trabajo.png", use_column_width=True)
    st.markdown("**1 Signos de puntuación:** Se eliminaron los distintos signos de puntuación")
    st.markdown("**2 Números:** Eliminación de los números y su transformación a texto")
    st.markdown("**3 Minúsculas:** Convertir todas las letras a minúsculas")
    st.markdown("**4 Stop Words:** Eliminación de palabras innecesarias")
    st.markdown("**5 Tokenizacion:** Transformar una cadena de textos en una lista de palabras")
    st.markdown("**6 Lemmatización:** Simplificar las palabras a su raiz")
    st.image("lemmatizacion.png", use_column_width=True)


    
def randon_forest():
    st.write("""Para el entrenamiento de modelo nos basamos en un sistema de random forest, al ser el que mejor dio mejor performance.
             Tal como se puede puede apreciar en la matriz de confucion se optuvieron los siguientes resultado al momento de clasificar
             las reseñas como buena, mala o intermedia""")
    st.image("matriz.jpeg", use_column_width=True)

def nube():
    st.write("""Tomando en consideración las palabras clave que uso el modelo para tomar y clasificar las reseñas se genero la siguiente 
             nube de palabras""")
    st.image("nube.jpeg", use_column_width=True)


# Definir la función get_wordnet_pos()
def get_wordnet_pos(word):
    """Map POS tag to first character lemmatize() accepts"""
    tag = nltk.pos_tag([word])[0][1][0].upper()
    tag_dict = {"J": wordnet.ADJ,
                "N": wordnet.NOUN,
                "V": wordnet.VERB,
                "R": wordnet.ADV}

    return tag_dict.get(tag, wordnet.NOUN)

# Definir la función preprocesar_texto()
def preprocesar_texto(texto):
    # Estos son cambios necesarios en el texto ingresado para que el modelo haga la mejor predicción
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

def interfaz():
    st.title('Clasificador de Comentarios')
    
    # Campo de entrada para el comentario
    comentario = st.text_input('Escribe tu comentario')
    
    # Botón para realizar la clasificación
    if st.button('Clasificar'):
        # Verificar si se ingresó un comentario
        if comentario:
            # Realizar la predicción utilizando el modelo cargado
            prediction = modelo.predict(preprocesar_texto(comentario))

            # Imprimir el resultado en el formato deseado
            if prediction == 0:
                st.write("La reseña es mala")
            elif prediction == 1:
                st.write("La reseña es neutra")
            else:
                st.write("La reseña es buena")
        else:
            st.write('Por favor, ingresa un comentario antes de realizar la clasificación')

modelo()
preparacion()
randon_forest()
nube()
interfaz()