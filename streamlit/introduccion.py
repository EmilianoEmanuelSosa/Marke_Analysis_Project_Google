import streamlit as st
import pandas as pd

def introduccion():
    st.subheader("**Conocenos**")
    st.write("""Somos una consultoría de análisis de datos que está desarrollando un nuevo paquete de servicios enfocado en mejorar el rendimiento de locales del sector gastronómico. Este paquete está diseñado para ayudar a los restaurantes a aumentar su popularidad, mejorar su servicio al cliente y aumentar sus ventas.

Dicho paquete está siendo evaluada para ser implementada en una cadena de restaurantes en el estado de Nevada. Y para la evaluación del produlto, estos servicios están siendo evaluados poniéndolos en ejecución en 10 restuarantes selectos de forma aletoria en el estado de Nevada y estados fronterizos: Óregon, Idaho, California, utah y Arizona.

""")
    st.image("zona.png", use_column_width=True)
    st.write("""EL criterio para la selección de restaurantes fue su popularidad o rendimiento en sitios webs de Reseñas y críticas, para así comparar lo que nuestro paquete de servicios puede lograr en dichos restaurantes de bajo rendimeinto enfréntandolos contra aquellos que si tienen buen rendimiento.""")

def paquete():
    st.subheader("**Soluciones del paquete:**")
    st.markdown("**Servicio API REST:** Servicio para la obtención de competidores y usuarios: Esta API proporcionará a los restaurantes datos sobre sus competidores y sus clientes. Los datos de los competidores se utilizarán para identificar oportunidades de crecimiento y diferenciación. Los datos de los clientes se utilizarán para personalizar las campañas de marketing y mejorar el servicio al cliente.")
    st.markdown("**Modelo de machine learning:** El modelo de lenguaje natural analizará las reseñas de los clientes para proporcionar información sobre la satisfacción de los clientes y las áreas de mejora del restaurante.")
    st.markdown("**Análisis y dashboard interactivo:** Este análisis proporcionará a los restaurantes una visión general de su rendimiento y les ayudará a identificar áreas de mejora. El dashboard interactivo será fácil de usar y proporcionará información visual atractiva.")
    st.image("logo_bueno.png", use_column_width=True)

introduccion()
paquete()