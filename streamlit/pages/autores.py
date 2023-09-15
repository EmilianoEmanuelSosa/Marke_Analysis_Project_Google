import streamlit as st

def mostrar_informacion_autores():
    st.title("Información de los Autores")
    
    # Info ricardo
    st.subheader("Ricardo Sanchez")
    st.image("ricardo.jpeg", use_column_width=True)
    st.markdown("[Enlace al GitHub](https://github.com/Rickhersd)")
    st.markdown("Rol: Anlista funcional")
    
    # Infor matias
    st.subheader("Matias Ponce")
    st.image("matias.jpeg", use_column_width=True)
    st.markdown("[Enlace al GitHub](https://github.com/PrismaPsy)")
    st.markdown("Rol: Analista de datos")

    # infor gabo 
    st.subheader("Gabriel Urbina")
    st.image("gabo.jpeg", use_column_width=True)
    st.markdown("[Enlace al GitHub](https://github.com/Gabo10DV)")
    st.markdown("Rol: Analista de datos")

    # infor franco
    st.subheader("Franco Aguilera")
    st.image("franco.jpeg", use_column_width=True)
    st.markdown("[Enlace al GitHub]()")
    st.markdown("Rol: Ingeniero de datos")

    # infor emilio
    st.subheader("Emiliano Sosa")
    st.image("emiliano.jpeg", use_column_width=True)
    st.markdown("[Enlace al GitHub](https://github.com/EmilianoEmanuelSosa)")
    st.markdown("Rol: Ingeniero de datos")
# Llama a la función para mostrar la información de los autores en la página correspondiente
mostrar_informacion_autores()
