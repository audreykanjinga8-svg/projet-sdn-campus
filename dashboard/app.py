from flask import Flask, render_template, jsonify
import os
from alerts import send_alert
import threading
import time

app = Flask(__name__)

LOG_FILE = "../logs/network.log"

# Stockage des dernières alertes envoyées pour éviter les doublons
sent_alerts = set()

def monitor_logs():
    """Surveille le fichier log en arrière-plan et envoie les alertes Telegram"""
    while True:
        if os.path.exists(LOG_FILE):
            with open(LOG_FILE, "r") as f:
                lines = f.readlines()

            for line in lines[-10:]:  # vérifier les 10 dernières lignes
                if line.startswith("ERREUR") and line not in sent_alerts:
                    send_alert(f"⚠️ Nouvelle erreur détectée : {line.strip()}")
                    sent_alerts.add(line)

        time.sleep(5)  # vérifie toutes les 5 secondes

# Lancer le monitoring dans un thread séparé
threading.Thread(target=monitor_logs, daemon=True).start()

@app.route("/")
def home():
    logs = []
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as f:
            logs = f.readlines()[-10:]  # dernières 10 lignes
    return render_template("dashboard.html", logs=logs, data=[len(logs)], labels=list(range(1,len(logs)+1)))

@app.route("/metrics")
def metrics():
    logs = []
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as f:
            logs = f.readlines()[-10:]

    chart_data = [len(line) for line in logs]  # longueur des lignes comme métrique
    chart_labels = list(range(1, len(logs)+1))

    return jsonify({
        "last_metrics": logs,
        "chart_data": chart_data,
        "chart_labels": chart_labels
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

