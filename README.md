# Gestionnaire d'Inventaire
## Installation
### Prérequis
* Python 3.9 ou plus récent.
* Les bibliothèques Python suivantes :
   * ` pandas `
     
### Étapes d'installation
1. Clone ou télécharge ce dépôt.

2. Installe les dépendances nécessaires en exécutant la commande suivante dans ton terminal :
```
pip install pandas

```
## Utilisation
### Étape 1 : Consolidation des fichiers CSV
1. Place les fichiers CSV que tu souhaites consolider dans le dossier csv_files.
2. Exécute le script de consolidation avec la commande suivante :

```
python consolidate_csv.py

```
3. Résultat :

* Un fichier nommé `consolidated_inventory.csv` est généré.
* Un rapport s'affiche dans la console indiquant :
  * Le nombre total de produits consolidés.
  * Les catégories présentes.
### Étape 2 : Recherche dans l'inventaire
1. Exécute le script de recherche avec cette commande :
```
python search_inventory.py

```
2. Suis les instructions dans le menu interactif pour :
    * Rechercher un produit par son nom.
    * Rechercher des produits par catégorie.
    * Rechercher des produits dans une plage de prix.
    * Exporter les résultats dans un fichier CSV nommé `search_results.csv`.
### Étape 3 : Tests unitaires
1. Exécute les tests unitaires pour vérifier les fonctionnalités avec cette commande :
```
python -m unittest test_inventory.py

```
