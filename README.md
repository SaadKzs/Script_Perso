Gestionnaire d'Inventaire
Installation
Prérequis
Python 3.9 ou plus récent.
Les bibliothèques Python suivantes :
pandas
Étapes d'installation
Clone ou télécharge ce dépôt.
Installe les dépendances nécessaires en exécutant la commande suivante dans ton terminal :
bash
Copier le code
pip install pandas
Utilisation
Étape 1 : Consolidation des fichiers CSV
Place les fichiers CSV que tu souhaites consolider dans le dossier csv_files.
Exécute le script de consolidation avec la commande suivante :
bash
Copier le code
python consolidate_csv.py
Résultat :
Un fichier nommé consolidated_inventory.csv est généré.
Un rapport s'affiche dans la console indiquant :
Le nombre total de produits consolidés.
Les catégories présentes.
Étape 2 : Recherche dans l'inventaire
Exécute le script de recherche avec cette commande :
bash
Copier le code
python search_inventory.py
Suis les instructions dans le menu interactif pour :
Rechercher un produit par son nom.
Rechercher des produits par catégorie.
Rechercher des produits dans une plage de prix.
Exporter les résultats dans un fichier CSV nommé search_results.csv.
Étape 3 : Tests unitaires
Exécute les tests unitaires pour vérifier les fonctionnalités avec cette commande :
bash
Copier le code
python -m unittest test_inventory.py
