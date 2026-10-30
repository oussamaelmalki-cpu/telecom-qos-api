# On utilise une image Python légère
FROM python:3.11-slim

# On définit le dossier de travail dans le conteneur
WORKDIR /app

# On copie les requirements et on installe les dépendances
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# On copie tout le reste du projet (app.py, models, etc.)
COPY . .

# On expose le port 8000
EXPOSE 8000

# La commande pour lancer l'API
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]