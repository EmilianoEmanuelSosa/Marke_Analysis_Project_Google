import streamlit as st

def fuente_dato():
    st.subheader("**Fuentes de datos**")
    st.write("""Para este trabajo se tomaron como fuente de datos Google y Yelp, que cuentan con información actualizada hasta el 7 de marzo de 2023, dentro de las cuales se encontraron los siguientes archivos. 
             Yelp: user.parquet , tip.json, reviews.json , chekink.json , business.pkl
             Google: reviews_estados (archivos json dispuestos por cada estado de USA), metadata_sitios.json
             En lo que respecta a la confiabilidad de las fuentes se puede decir estas son de alto valor al provenir de empresas grandes y de renombre como Google. Los datos son principalmente de tipo texto y numérico decimal, usados para describir información general de los locales, ubicación y valoración por los usuarios.
             """)
def grafico_google():
    st.write("""De forma general los datos proporcionados por Google
              incluyen distintos comercios dentro de los cuales los que están mas presentes son los restaurantes""")
    st.image("google.png", use_column_width=True)
def grafico_yelp():
    st.write("""Mientras que por parte de yelp los datos están enfocados 
             únicamente a restaurantes de los cuales se puede apreciar la siguiente distribución de categorías.""")
    st.image("yelp.png", use_column_width=True)

def grafico_años():
    st.write("""Por otro lado en lo que respecta a la actividad de los 
             usuarios se pudo encontrar que en principio esta tenia una tendencia a aumentar la misma parece haber sido
              mermada en el 2020 lo cual se le puede acreditar a la pandemia.""")
    st.image("años.png", use_column_width=True)

# Página principal
st.title("analisis preliminar")

# Mostrar los KPIs
fuente_dato()
grafico_google()
grafico_yelp()
grafico_años()

