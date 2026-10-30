import pandas as pd
import joblib
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

def train():
    print("Chargement des données...")
    df = pd.read_csv("data/telecom_qos.csv")
    
    X = df.drop(columns=["QoS_Degradation"])
    y = df["QoS_Degradation"]
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    print("Entraînement du modèle Random Forest...")
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    
    print(f"\n✅ Précision du modèle (Accuracy) : {accuracy:.4f}")
    print("\nRapport de classification :\n")
    print(classification_report(y_test, y_pred))
    
    out = Path("models")
    out.mkdir(exist_ok=True)
    joblib.dump(model, out / "qos_model.pkl")
    print("💾 Modèle sauvegardé avec succès dans models/qos_model.pkl !")

if __name__ == "__main__":
    train()