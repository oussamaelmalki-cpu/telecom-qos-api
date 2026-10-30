import numpy as np
import pandas as pd
from pathlib import Path

def generate_telecom_data(n_samples=5000, seed=42):
    np.random.seed(seed)
    
    # 1. Simulation des indicateurs de performance (KPIs) 5G
    sinr = np.random.normal(15, 5, n_samples) # Qualité du signal (dB)
    rssi = np.random.normal(-75, 10, n_samples) # Force du signal (dBm)
    packet_loss = np.random.exponential(1.5, n_samples) # Perte de paquets (%)
    bandwidth_usage = np.random.normal(60, 15, n_samples) # Charge du réseau (%)
    
    # 2. Création de la variable cible (Y) : Dégradation de la QoS (0 = Bon, 1 = Dégradé)
    # On considère qu'il y a dégradation si le SINR est bas et la perte de paquets est élevée
    qos_degradation = np.where((sinr < 10) & (packet_loss > 3), 1, 0)
    
    # 3. Création du tableau (DataFrame)
    df = pd.DataFrame({
        "SINR": sinr,
        "RSSI": rssi,
        "Packet_Loss": packet_loss,
        "Bandwidth_Usage": bandwidth_usage,
        "QoS_Degradation": qos_degradation
    })
    
    # 4. Sauvegarde dans le dossier data
    out = Path("data")
    out.mkdir(exist_ok=True)
    df.to_csv(out / "telecom_qos.csv", index=False)
    
    print("✅ Données générées et sauvegardées dans data/telecom_qos.csv")
    print("\nAperçu des données :")
    print(df.head())
    print(f"\nNombre total d'échantillons : {len(df)}")
    print(f"Nombre de cas de dégradation de la QoS : {df['QoS_Degradation'].sum()}")

if __name__ == "__main__":
    generate_telecom_data()