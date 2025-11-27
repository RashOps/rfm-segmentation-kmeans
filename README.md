# 📊 Pilote Marketing : Segmentation Clients (RFM & IA)

> **Projet Double Compétence : Business Intelligence & Data Science**

Ce dashboard interactif permet aux responsables marketing de transformer des données transactionnelles brutes en **stratégies d'activation client**. Il s'appuie sur une segmentation RFM (Récence, Fréquence, Montant) propulsée par un algorithme de Machine Learning (**K-Means**).

**Voir l'application déployer ici 👇**
[![Hugging Face Spaces](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-blue)](https://huggingface.co/spaces/RashOps/rfm-segmentation-kmeans)

---

## 🎯 Objectifs du Projet

Dans un contexte e-commerce, traiter tous les clients de la même manière est inefficace et coûteux. Ce projet vise à :
1.  **Segmenter** la base client de manière objective grâce à l'IA.
2.  **Visualiser** la répartition du chiffre d'affaires et des comportements.
3.  **Prescrire** des actions concrètes (Retention, Up-sell, Réactivation) via un moteur de recommandation intégré.

---

## 🛠 Stack Technique

| Domaine | Technologies |
| :--- | :--- |
| **Data Processing** | [![Pandas](https://img.shields.io/badge/Pandas-Analyses-150458?logo=pandas)](https://pandas.pydata.org/) |
| **Machine Learning** | [![Scikit-Learn](https://img.shields.io/badge/Scikit_Learn-K_Means-F7931E?logo=scikit-learn)](https://scikit-learn.org/) |
| **Visualisation** | [![Plotly](https://img.shields.io/badge/Plotly-Interactif-3F4F75?logo=plotly)](https://plotly.com/) |
| **Web App** | [![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-FF4B4B?logo=streamlit)](https://streamlit.io/) |

---

## 🚀 Fonctionnalités Clés

Contrairement aux dashboards classiques, cette application intègre une couche d'intelligence décisionnelle :

* **📊 KPIs Dynamiques :** Suivi du Chiffre d'Affaires, Panier Moyen et Récence en temps réel selon les filtres.
* **🤖 Segmentation IA :** Visualisation des clusters générés par l'algorithme K-Means (Visualisation 2D Récence vs Montant).
* **💡 Moteur de Recommandation :** Le dashboard analyse le segment sélectionné et affiche une stratégie marketing adaptée (ex: *"Segment À Risque" → "Envoyer promo -20% urgence"*).
* **👥 Explorateur de Données :** Accès aux listes de clients filtrées pour export et campagne d'emailing.

---

## 📂 Structure du Projet

```text
Projet_RFM/
│
├── data/
│   ├── online_retail.csv       # Dataset brut (Source)
│   └── rfm_segmented.csv       # Données traitées avec Clusters (Output du Notebook)
│
├── notebooks/
│   └── analysis.ipynb          # Le Labo : Nettoyage, Feature Engineering (RFM) & K-Means
│
├── app.py                      # L'Application : Dashboard Streamlit
├── requirements.txt            # Dépendances pour le déploiement
└── README.md                   # Documentation
