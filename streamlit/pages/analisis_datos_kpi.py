import streamlit as st

def mostrar_kpi1():
    st.subheader("**KPI N°1**: Aumento de la Cantidad de Reseñas de Clientes a lo Largo de un Año")
    st.write("**Definición**: Este KPI mide el incremento en la cantidad total de reseñas dejadas por los clientes en los diferentes locales de restaurantes durante el transcurso de un año.")
    st.write("**Fórmula**: ((Cantidad de Reseñas Actuales - Cantidad de Reseñas Inicial) / Cantidad de Reseñas Inicial) x 100.")
    st.write("**Interpretación**: Un aumento positivo en este KPI indica que las estrategias de marketing y las interacciones con los clientes están motivando a más personas a dejar reseñas sobre su experiencia en los restaurantes.")
    st.write("**Detalle**: Los datos para este KPI se obtendrán a partir del número total de reseñas que contiene cada local.")

def mostrar_kpi2():
    st.subheader("**KPI N°2**: Sentimiento de Reseñas en Comparación con Locales con Mejores Reseñas")
    st.write("**Definición**: Este KPI mide el sentimiento general de las reseñas para cada local de restaurante en comparación con los locales que tienen las mejores reseñas.")
    st.write("**Fórmula**: (Porcentaje de Reseñas Positivas del Local - Porcentaje de Reseñas Positivas de los Locales de Referencia) + (Porcentaje de Reseñas Neutras del Local - Porcentaje de Reseñas Neutras de los Locales de Referencia) + (Porcentaje de Reseñas Negativas del Local - Porcentaje de Reseñas Negativas de los Locales de Referencia).")
    st.write("**Interpretación**: Un resultado positivo indica que las reseñas del local tienen un sentimiento más positivo en comparación con los locales de referencia. Un resultado negativo sugiere un sentimiento más negativo. Un valor cercano a cero podría indicar que el sentimiento es similar al de los locales de referencia.")

def mostrar_kpi3():
    st.subheader('**KPI N°3**: Retención de Clientes.')
    st.write('**Definición**: Esta métrica evalúa la capacidad de la empresa para mantener a sus clientes existentes durante un período de tiempo determinado.')
    st.write('**Fórmula**: ((Clientes al final del período - Nuevos clientes durante el período) / Clientes al inicio del período) x 100.')
    st.write('**Interpretación**: Una alta retención de clientes indica la satisfacción y el valor continuo que los clientes encuentran en los servicios de la empresa. Una baja retención podría indicar problemas en la calidad del servicio o la necesidad de mejorar el soporte al cliente')
    st.write('**Detalle**: Esta métrica en cuanto a la cantidad de clientes, se toma a partir de la cantidad de Reviews que se tienen. Y')

def mostrar_kpi4():
    st.subheader('**KPI N°4**: Análisis de Conveniencia de Ubicación Basado en Turismo y Cantidad de Reseñas.')
    st.write('**Definición**: Este KPI evalúa la conveniencia de establecer un nuevo negocio en un área geográfica en función de la cantidad de reseñas de locales existentes y la actividad turística en esos lugares')
    st.write('**Formula**:Índice de Conveniencia = (Cantidad de Reseñas Positivas + Actividad Turística) / (Cantidad Total de Reseñas + Actividad Turística).')
    st.write('**Interpretación**: Un valor más alto del índice de conveniencia sugiere que la ubicación tiene un buen equilibrio entre reseñas positivas y actividad turística. Esto podría indicar que es una ubicación atractiva para establecer un nuevo negocio.')
# Página principal
st.title("Desarrollo de KPIs")

# Mostrar los KPIs
mostrar_kpi1()
mostrar_kpi2()
mostrar_kpi3()
mostrar_kpi4()