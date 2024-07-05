# Tweet Sentiment API

## Objectif de l'API

L'objectif de cette API est de prédire le sentiment (positif ou négatif) d'un tweet donné. Cette API utilise un modèle de machine learning pour analyser le texte du tweet et fournir une prédiction.

## Fonctionnement Global de l'API

L'API est construite avec FastAPI, un framework web rapide pour la construction d'API basées sur Python. Voici comment elle fonctionne :

1. **Prétraitement du texte** : Le texte du tweet est prétraité pour être dans un format approprié pour le modèle.
2. **Chargement du modèle** : Le modèle de machine learning est chargé pour effectuer la prédiction.
3. **Prédiction du sentiment** : Le modèle analyse le texte du tweet et retourne le sentiment (positif ou négatif).

## Architecture de l'API

### Structure des Dossiers

```
tweetsentimentapi/
├── src/
│ ├── init.py
│ ├── app.py
│ ├── model_loader.py
│ ├── text_preprocessing.py
│ ├── tests/
│ ├── init.py
│ ├── test_app.py
│ ├── test_model_loader.py
├── model_files/
│ ├── model.keras
│ ├── tokenizer.pickle
├── Dockerfile
├── requirements.txt
├── README.md
├── setup.py
└── TweetsSentimentTests_localhost_postman_collection.json
```

## Utilisation de l'API
- Démarrage de l'API (via FastAPI) avec main.py comme exemple
  - Assurez-vous de l'utilisation de la version Python 3.10.12
  - Assurez-vous que toutes les dépendances sont installées. Vous pouvez utiliser le fichier requirements.txt pour installer les dépendances nécessaires :
    ```
    pip install -r requirements.txt
    ```
  - Exécutez main.py pour démarrer l'API :
    ```
    python main.py
    ```
- L'API sera disponible sur http://localhost:8000.

- Obtenir le Sentiment d'un Tweet avec get_tweetsentiment.py
    Le fichier get_tweetsentiment.py est un script qui permet de tester l'API en envoyant un tweet et en récupérant le sentiment prédicté.
    ```
    python get_tweetsentiment.py  "mon tweet bla bla"
    ```

## Conteneurisation Docker

Pour exécuter l'API dans un conteneur Docker, utilisez la commande suivante :

```
docker run -p 8000:8000 -v C:\zz_dev_folder\test_for_maif\fastAPI_App_Tweets\tmp2\dockerpackage\_local_model_files:/app/_local_model_files ghcr.io/lamjoun/tweetsentimentapi
```

## Utilisation du Package

```
Le dossier /dist contient les fichiers packagés (tweetsentimentpkg-0.1.tar.gz et tweetsentimentpkg-0.1-py3-none-any.whl). Pour installer le package, utilisez les commandes suivantes :
```
- Port Mapping (8000:8000) : Mappe le port 8000 du conteneur au port 8000 de la machine hôte.
- Volume Mapping : Mappe le dossier local contenant le modèle (_local_model_files) au répertoire /app/_local_model_files dans le conteneur. Cela permet de s'assurer que le modèle est accessible par l'application.
- Assurez-vous de télécharger le modèle depuis le lien suivant et de le placer dans le répertoire approprié :
- Lien de téléchargement du modèle : [lien_du_modele]

Tests avec GitHub Actions
Le fichier test_api.yml dans .github/workflows décrit le workflow pour tester l'API. Voici les étapes :

1. Checkout du code : Récupère le code source depuis le dépôt GitHub.
2. Configuration de l'environnement Python : Installe Python 3.10.12.
3. Installation des dépendances : Installe les dépendances nécessaires.
4. Configuration des identifiants AWS : Configure les identifiants AWS pour télécharger le modèle.
5. Téléchargement du modèle : Télécharge le modèle depuis S3.
6. Exécution des tests Pytest : Exécute les tests unitaires avec Pytest.
7. Démarrage de FastAPI : Lance le serveur FastAPI.
8. Vérification du statut du serveur : Vérifie que le serveur est démarré correctement.
9. Tests de l'API : Exécute les tests de l'API avec un script Python.
10. Configuration de Node.js : Installe Node.js pour exécuter Newman.
11. Installation de Newman : Installe Newman pour exécuter les tests Postman.
12. Exécution des tests Postman : Exécute les tests Postman avec Newman.

## Validation et Documentation
- Typing : Utilise typing pour les annotations de type (voir PEP 484).
- Pydantic : Valide les entrées utilisateur avec Pydantic (voir Pydantic Documentation).
- Docstrings : Documentation du code avec des docstrings suivant PEP 287.
- Tests Unitaires : Tests unitaires avec unittest ou pytest (voir pytest Documentation).
- Tests End-to-End : Tests end-to-end avec Postman et Newman (voir Postman Documentation).
