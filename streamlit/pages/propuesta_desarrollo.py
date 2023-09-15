import streamlit as st
import pandas as pd
_, center, _ = st.columns([1,3,1])

body = """
Mejorar y expandir la aplicación de estrategias gastronómicas, brindando un servicio más completo y específico para locales gastronómicos. 
Esto incluye la creación de estrategias adaptadas a las necesidades 
individuales de cada negocio y la ampliación de la cobertura geográfica para abarcar todos los estados del país.


**Desarrollo de API**
Se plantea la creacion que contenga la informacion de los restaurantes adyacentes, con informacion tal como 

**Alcance del Proyecto**:
### 

- **Desarrollo de Estrategias Específicas:**
    - Identificación y análisis de las problemáticas únicas de cada local gastronómico.
    - Ejecución de análisis de ubicación, precios, tipos de plato y comparativa de marketing específicos para cada negocio.
    - Creación de estrategias personalizadas para mejorar la clientela y la competitividad de los locales.
- **Expansión Geográfica:**
    - Ampliación de la cobertura de la aplicación para incluir todos los estados del país.
    - Consideración de las particularidades locales y regionales en la creación de estrategias.
- **Mejoras en la Aplicación:**
    - Implementación de un ChatBot para facilitar la comunicación entre los clientes y nuestra empresa.
    - Desarrollo de una interfaz de usuario intuitiva que permita a los clientes ingresar información sobre un nuevo restaurante no registrado en la base de datos de la aplicación
"""
with center:
    st.markdown(body)