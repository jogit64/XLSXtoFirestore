import firebase_admin
from firebase_admin import credentials, firestore
import json
import sys

if len(sys.argv) < 2:
    print("Usage: python upload_to_firestore.py [jeu]")
    sys.exit(1)

jeu = sys.argv[1].lower()

collections = {
    'loto': 'lotoStats',
    'euromillions': 'euromillionsStats',
    'eurodreams': 'eurodreamsStats'
}

if jeu not in collections:
    print(f"Jeu non reconnu: {jeu}")
    sys.exit(2)

collection_name = collections[jeu]
json_file_path = f"{jeu}_Stat.json"

cred = credentials.Certificate('./love4num-app-firebase-admin.json')
firebase_admin.initialize_app(cred)
db = firestore.client()

with open(json_file_path, 'r', encoding='utf-8') as f:
    stats = json.load(f)

for stat in stats:
    # Utilisez 'numero' pour la clé
    doc_id = f"{stat['numero']}_{stat['type']}"
    doc_ref = db.collection(collection_name).document(doc_id)
    doc_ref.set(stat)

print(f"Les données de {jeu} ont été envoyées à Firestore dans la collection '{collection_name}'.")
