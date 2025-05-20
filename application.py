import streamlit as st
import pandas as pd
import folium
from folium.plugins import MarkerCluster
from streamlit_folium import st_folium
import matplotlib.pyplot as plt

st.set_page_config(page_title="Coworking à Paris", layout="wide")

st.title("📍 Espaces de Coworking à Paris")
st.markdown("Visualisation interactive des espaces de coworking listés sur [leportagesalarial.com](https://www.leportagesalarial.com/coworking/).")

@st.cache_data
def load_data():
    return pd.read_csv("coworking_data.csv")

df = load_data()

st.write("Aperçu des données géocodées :")
st.dataframe(df[["nom", "latitude", "longitude"]].dropna())

# BARRE DE RECHERCHE
search_term = st.text_input("Rechercher un coworking (par nom ou adresse)").lower()

# Filtrage dynamique du DataFrame
if search_term:
    df = df[
        df["nom"].str.lower().str.contains(search_term) |
        df["adresse"].str.lower().str.contains(search_term)
    ]

# Carte Folium
m = folium.Map(location=[48.8566, 2.3522], zoom_start=12)
marker_cluster = MarkerCluster().add_to(m)

for _, row in df.iterrows():
    if pd.notnull(row["latitude"]) and pd.notnull(row["longitude"]):
        popup_content = f"<b>{row['nom']}</b><br>{row['adresse']}<br><a href='{row['Site']}' target='_blank'>Voir site</a>"
        folium.Marker(
            location=[row["latitude"], row["longitude"]],
            popup=popup_content,
            icon=folium.Icon(color="blue", icon="briefcase", prefix="fa")
        ).add_to(marker_cluster)

st.subheader("🗺️ Carte des espaces de coworking")
st_folium(m, width=700, height=500)

# Visualisation supplémentaire : Répartition par arrondissement
st.subheader("📊 Répartition par arrondissement")
df["arrondissement"] = df["adresse"].str.extract(r"75(\d{2})")
arr_counts = df["arrondissement"].value_counts().sort_index()

fig, ax = plt.subplots()
arr_counts.plot(kind="bar", ax=ax)
ax.set_xlabel("Arrondissement")
ax.set_ylabel("Nombre d'espaces")
ax.set_title("Nombre d'espaces de coworking par arrondissement")
st.pyplot(fig)
