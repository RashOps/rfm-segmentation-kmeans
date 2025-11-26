import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

# Configuration de la page 
st.set_page_config(
    page_title="Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded")

# Mise en cache et chargment du dataset
@st.cache_data
def load_data() :
    path = "./data/rfm_segmented.csv"
    try : 
        df = pd.read_csv(path)
        return df
    except FileNotFoundError :
        st.error(f"Fichier {path} non trouvé, vérifié le dossier data")
        return None
    except Exception as e:
        st.error(f"Une erreur est survenue : {e}")
        return None

# Titre et Introduction ==============================
st.title("📊 Pilote Marketing : Segmentation Clients")
st.markdown("""
Bienvenue sur le dashboard de pilotage. 
Cette application permet d'analyser la segmentation client issue de notre algorithme **K-Means**.
""")

# Chargement et gestion des erreurs ================
rfm = load_data()
if rfm is None :
    st.stop()

# Les KPIs =========================================
# Créarion des colonnes
st.divider()
st.subheader("Les KPIs")
kpi_col = st.columns(4)

# Création des KPIs et des selecteurs
# Choix des segments
st.sidebar.header("Filtres")
segment_selection = st.sidebar.multiselect(
    "Choisir un segment à afficher",
    options=rfm["Segment"].unique(),
    default=rfm["Segment"].unique()
)

# Filtrage du dataset
df_filtred = rfm[rfm["Segment"].isin(segment_selection)]

# Les KPIs variables
# Nombre de client
nb_clients = df_filtred["Customer ID"].count()

# Le chiffres d'affaires
CA = df_filtred["Monetary"].sum()

# Panier moyen
average_buying = 0
if nb_clients > 0 :
    average_buying = CA / nb_clients

# Recence moyenne
average_recence = 0
average_recence = df_filtred["Recency"].mean()

# Affichage des KPIs
if not segment_selection :
    st.warning("Selectionnez au moins un segment pour afficher les KPIs", icon="🚨")
else :
    # KPI clients
    with kpi_col[0] :
        st.metric(label="Nombre de Clients", value=f"{nb_clients:,.0f}".replace(",", " "))

    # KPI chiffre d'affaires
    with kpi_col[1] :
        st.metric(label="Chiffre d'affaires", value=f"{CA:,.2f} €")

    # KPI panier moyen
    with kpi_col[2] :
        st.metric(label="Panier moyen", value=f"{average_buying:,.2f} €")
        
    # KPI recence moyenne
    with kpi_col[3] :
        st.metric(label="Recence moyenne", value=f"{average_recence:,.0f} Jours")

# Affichage du dataset =====================
st.divider()
st.subheader("Afficher la liste des clients")

with st.expander(label="Liste des clients du segments", icon="👥") :
    if not segment_selection : 
        st.dataframe(rfm, use_container_width=True)
    else : 
        st.dataframe(df_filtred[['Customer ID', 'Segment', 'Recency', 'Frequency', 'Monetary']], use_container_width=True)

# Graphes et analyses =====================
st.divider()
st.subheader("Les graphiques")

viz_col = st.columns(2)

# Le diagrammes en bar
with viz_col[0]:
    st.markdown("### Répartition des clients")
    fig_bar = px.bar(
        data_frame=rfm["Segment"].value_counts().reset_index(),
        x="Segment",
        y="count",
        color="Segment",
        text="Segment",
        title="Nombre de clients par segment"
    )
    st.plotly_chart(fig_bar, use_container_width=True)

# Nuage des points
with viz_col[1]:
    st.markdown("### Analyse Récence vs Montant")
    fig_scatter = px.scatter(
        data_frame=df_filtred,
        x="Recency",
        y="Monetary",
        color="Segment",
        size="Frequency",
        hover_data=["Customer ID"],
        title="Carte des clusters"
    )
    st.plotly_chart(fig_scatter, use_container_width=True)