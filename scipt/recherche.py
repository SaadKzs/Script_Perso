import pandas as pd

# Charger le fichier consolidé
consolidated_file = "consolidated_inventory.csv"

try:
    df = pd.read_csv(consolidated_file, encoding="utf-8-sig", sep=";")
except FileNotFoundError:
    print("Le fichier consolidé n'a pas été trouvé. Assurez-vous qu'il existe.")
    exit()

# Menu pour l'utilisateur
def afficher_menu():
    print("\nQue voulez-vous faire ?")
    print("1. Rechercher par nom de produit")
    print("2. Rechercher par catégorie")
    print("3. Rechercher par plage de prix")
    print("4. Exporter les résultats")
    print("5. Quitter")

# Fonctionnalités
def recherche_nom_produit():
    produit = input("Entrez le nom du produit : ").strip()
    resultats = df[df['Nom du produit'].str.contains(produit, case=False, na=False)]
    print(resultats if not resultats.empty else "Aucun produit trouvé.")

def recherche_categorie():
    categorie = input("Entrez la catégorie : ").strip()
    resultats = df[df['Catégorie'].str.contains(categorie, case=False, na=False)]
    print(resultats if not resultats.empty else "Aucune catégorie trouvée.")

def recherche_prix():
    try:
        min_prix = float(input("Entrez le prix minimum : "))
        max_prix = float(input("Entrez le prix maximum : "))
        resultats = df[(df['Prix unitaire'] >= min_prix) & (df['Prix unitaire'] <= max_prix)]
        print(resultats if not resultats.empty else "Aucun produit trouvé dans cette plage de prix.")
    except ValueError:
        print("Veuillez entrer des nombres valides.")

def exporter_resultats():
    resultats = input("Entrez les critères pour exporter (par exemple : 'Papier' ou 'Mobilier') : ").strip()
    data = df[df['Nom du produit'].str.contains(resultats, case=False, na=False)]
    if not data.empty:
        data.to_csv("search_results.csv", index=False, encoding="utf-8-sig", sep=";")
        print("Les résultats ont été exportés dans 'search_results.csv'.")
    else:
        print("Aucun résultat à exporter.")

# Boucle principale
while True:
    afficher_menu()
    choix = input("Votre choix : ").strip()
    if choix == "1":
        recherche_nom_produit()
    elif choix == "2":
        recherche_categorie()
    elif choix == "3":
        recherche_prix()
    elif choix == "4":
        exporter_resultats()
    elif choix == "5":
        print("Au revoir !")
        break
    else:
        print("Choix invalide. Veuillez réessayer.")
