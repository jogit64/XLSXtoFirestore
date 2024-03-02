# Outils de Préparation de Données pour Love4Num

Ce projet comprend une série de scripts Python conçus pour automatiser la préparation, le formatage, et l'envoi de statistiques des jeux de la Française des Jeux (FDJ) - Loto, Euromillions, et Eurodreams - sur Firestore. Ces outils sont une composante essentielle de l'application Love4Num, qui transforme des mots et phrases en numéros de loterie basés sur ces statistiques.

## Objectif

L'objectif de ces scripts est de faciliter la mise à jour des données statistiques utilisées par Love4Num pour générer des numéros de loterie personnalisés. Ils automatisent le processus de :

- Téléchargement des statistiques des jeux de la FDJ.
- Conversion de ces statistiques au format JSON.
- Envoi des données formatées dans une base de données Firestore.

## Fonctionnement

### Scripts Inclus

- `convert.py` : Script pour convertir les statistiques téléchargées en format JSON.
- `upload_to_firestore.py` : Script pour envoyer les données JSON sur Firestore.

### Prérequis

- Python 3.x
- firebase-admin (Bibliothèque Python)
- Un projet Firebase configuré avec Firestore.

### Configuration de Firebase

Pour utiliser ces scripts, vous devez configurer votre propre projet Firebase et Firestore. Voici les étapes à suivre :

1. **Créer un projet Firebase** : Rendez-vous sur [Firebase Console](https://console.firebase.google.com/) et créez un nouveau projet.
2. **Configurer Firestore** : Dans la console Firebase, activez Firestore pour votre projet.
3. **Générer un fichier de configuration Admin SDK** : Allez dans les paramètres de votre projet Firebase > Comptes de service, puis générez un nouveau fichier de configuration privé pour votre Admin SDK. Téléchargez ce fichier JSON.

### Installation

1. Clonez ce dépôt sur votre machine.
2. Installez firebase-admin via pip :
   pip install firebase-admin

3. Configurez votre fichier de configuration Firebase Admin SDK : Placez le fichier JSON que vous avez téléchargé à l'étape 3 de la configuration de Firebase dans votre répertoire de travail. Pour des raisons de sécurité, assurez-vous que ce fichier est inclus dans votre `.gitignore` pour éviter son téléchargement accidentel sur des dépôts publics.

### Utilisation

**Conversion des Statistiques** : Après avoir téléchargé les statistiques de la FDJ, utilisez `convert.py` pour les convertir en format JSON.

python convert.py loto
python convert.py euromillions
python convert.py eurodreams

**Envoi sur Firestore** : Utilisez `upload_to_firestore.py` pour envoyer les fichiers JSON convertis sur Firestore.

python upload_to_firestore.py loto
python upload_to_firestore.py euromillions
python upload_to_firestore.py eurodreams

### Contribution

Bien que ces scripts soient spécifiquement conçus pour un usage personnel dans le cadre du projet Love4Num, toute suggestion d'amélioration ou de généralisation est la bienvenue.

# Contact

Pour toute question, suggestion, ou proposition de collaboration, n'hésitez pas à me contacter :

Site Web : johannr.fr
Email : contact@johannr.fr
