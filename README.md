# 📊 Segmentation Client RFM (Recency, Frequency, Monetary)

Ce projet est une application interactive de **Data Science** permettant de segmenter une base de données clients selon la méthode RFM. L'objectif est d'identifier les profils consommateurs pour optimiser les campagnes marketing.

L'application permet de charger des données, de calculer les scores RFM, d'appliquer un clustering (K-Means) et de visualiser les résultats via un dashboard interactif.

---

## 🛠 Tech Stack

| Catégorie | Technologies |
| :--- | :--- |
| **Data Prep & ML** | [![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=flat&logo=pandas&logoColor=white)](https://pandas.pydata.org/) [![Scikit-Learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=flat&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/stable/) |
| **Visualisation** | [![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=flat&logo=Matplotlib&logoColor=black)](https://matplotlib.org/) [![Seaborn](https://img.shields.io/badge/Seaborn-blue?logo=seaborn&logoColor=white)](https://seaborn.pydata.org/) [![Plotly](https://img.shields.io/badge/Plotly-%233F4F75.svg?style=flat&logo=plotly&logoColor=white)](https://plotly.com/python/) |
| **Application** | [![Streamlit](https://img.shields.io/badge/Streamlit-%23FF4B4B.svg?style=flat&logo=streamlit&logoColor=white)](https://streamlit.io/) |

---

## 📸 Démo / Aperçu

![Dashboard bientôt disponible](https://via.placeholder.com/800x400?text=Capture+d%27%C3%A9cran+de+votre+Dashboard+Streamlit)

---

## 🧐 Qu'est-ce que l'analyse RFM ?

L'analyse RFM est une technique marketing basée sur trois critères clés :

* **Récence (Recency) :** Date du dernier achat (plus c'est récent, mieux c'est).
* **Fréquence (Frequency) :** À quelle fréquence le client achète-t-il ?
* **Montant (Monetary) :** Combien le client dépense-t-il au total ?

Ce projet utilise **Scikit-Learn** pour automatiser cette segmentation via un algorithme de clustering (ex: K-Means) afin de regrouper les clients en catégories homogènes (ex: *Champions, Clients fidèles, À risque*).

---

## 🚀 Fonctionnalités

* 📥 **Upload de données :** Chargement de fichiers CSV/Excel transactionnels.
* 🧹 **Nettoyage automatique :** Gestion des valeurs manquantes et formatage des dates.
* 🧮 **Calcul des scores :** Création automatique des variables R, F et M.
* 🤖 **Clustering ML :** Segmentation non-supervisée (K-Means).
* 📊 **Visualisation 3D & 2D :** Scatter plots interactifs avec Plotly pour explorer les clusters.
* 📑 **Export :** Téléchargement des données segmentées au format CSV.

---

## 📂 Structure du Projet

```bash
├── data/                # Dataset 
├── images/              # Les images du projets
├── notebooks/           # Notebooks Jupyter pour l'analyse exploratoire
├── src/                 # Scripts de traitement (preprocessing.py, clustering.py)
├── app.py               # Point d'entrée de l'application Streamlit
├── requirements.txt     # Liste des dépendances
└── README.md            # Documentation du proje
