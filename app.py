import streamlit as st
import pandas as pd
import plotly.express as px

# Leer CSV generado
df = pd.read_csv("ofertas.csv")

st.title("Radar mercado prepago España")

# Selector (futuro multi-país)
paises = ["España"]
pais_seleccionado = st.selectbox("Selecciona un país", paises)

# Mostrar tabla
st.subheader("Tabla de operadores y planes")
st.dataframe(df)

# Gráfico de €/GB
fig = px.bar(df, x="Operador", y="€/GB", color="Operador", title="Precio por GB (€/GB)")
st.plotly_chart(fig)

# Generar texto LinkedIn
def generar_post_linkedin(df):
    lider = df[df["€/GB"] == df["€/GB"].min()]
    operador_top = lider["Operador"].values[0]
    precio_top = lider["€/GB"].values[0]

    texto = f"""El mercado prepago en España sigue moviéndose.

Hoy revisé las principales ofertas y destaca {operador_top}, con un precio por GB de apenas {precio_top:.2f} €/GB.

¿Estamos ante una guerra de precios en el segmento prepago? ¿O veremos movimientos en servicios de valor añadido como Spotify o Netflix?

Me interesa saber cómo lo veis 👇
"""
    return texto

post = generar_post_linkedin(df)

st.subheader("Propuesta de post para LinkedIn (solo para admin)")
st.text_area("Texto generado", post, height=250)
