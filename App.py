import pandas as pd
import streamlit as st

# Chargement du fichier Excel
@st.cache_data
def load_data():
    df = pd.read_excel("membres.xlsx")
    return df

df = load_data()

st.set_page_config(page_title="Vérification des membres", page_icon="✅", layout="centered")

st.title("🔍 Vérification de présence dans la liste des membres")

st.write("Entrez votre nom pour vérifier si vous êtes inscrit dans la base.")

# Champ de recherche
nom_recherche = st.text_input("Votre nom :")

if st.button("Rechercher"):
    if nom_recherche.strip() == "":
        st.warning("Veuillez entrer un nom.")
    else:
        # Normalisation (majuscules, espaces)
        noms = df["First Name"].astype(str).str.lower().str.strip()
        if nom_recherche.lower().strip() in noms.values:
            st.success(f"✅ {nom_recherche} est bien présent(e) dans la liste !")
        else:
            st.error(f"❌ {nom_recherche} n’a pas été trouvé(e).")

