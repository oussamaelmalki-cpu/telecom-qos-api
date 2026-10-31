# 📡 Telecom QoS API - MLOps Cloud Deployment

![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)

> **API de prédiction de la dégradation de la QoS (5G) déployée sur le Cloud avec Docker et FastAPI.**

Ce projet a été développé dans le cadre de mon Master en Ingénierie des Systèmes de Télécommunication. Il illustre la mise en place d'un pipeline **MLOps** complet pour anticiper les baisses de performance réseau (chute du SINR, augmentation de la latence) avant qu'elles n'impactent les utilisateurs finaux.

## 🚀 Testez l'API en direct
L'API est déployée sur le Cloud et accessible publiquement via Swagger UI :
👉 **[Cliquez ici pour tester l'API](https://telecom-qos-api-4d914.containers.snapdeploy.app/docs)**
*(⚠️ Bdel had l'lien b l'lien dyalek dyal SnapDeploy ila kan mokhtalef)*

## ✨ Fonctionnalités
- **Machine Learning :** Modèle Random Forest entraîné pour classifier la QoS (Normal vs Dégradé) à partir de KPIs télécoms.
- **Backend API :** FastAPI pour une exposition rapide des prédictions en temps réel via des endpoints REST.
- **Conteneurisation :** Docker (Image Python 3.11-slim) garantissant la portabilité de l'application.
- **Cloud & MLOps :** Déploiement continu (CI/CD) synchronisé avec GitHub.

## 🗂️ Structure du Projet
```text
├── data/                   # Données simulées (CSV)
├── models/                 # Modèle de ML sauvegardé (.pkl)
├── src/                    # Scripts de génération et d'entraînement
│   ├── generate_data.py
│   └── train_model.py
├── app.py                  # Serveur FastAPI
├── Dockerfile              # Configuration de l'image Docker
├── requirements.txt        # Dépendances Python
└── README.md               # Documentation
