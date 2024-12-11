# Génération des fichiers CSV avec encodage utf-8-sig pour une meilleure compatibilité avec Excel

import os
import pandas as pd
import random

# Définir les catégories et données aléatoires
categories = ["Mobilier", "Électronique", "Bureautique", "Jardinage"]
noms_produits = {
    "Mobilier": ["Chaise", "Table", "Armoire", "Canapé", "Lit"],
    "Électronique": ["Téléphone", "Ordinateur", "Casque", "Télévision", "Caméra"],
    "Bureautique": ["Stylo", "Classeur", "Imprimante", "Papier", "Toner"],
    "Jardinage": ["Pelle", "Râteau", "Tondeuse", "Arrosoir", "Graines"]
}

# Dossier pour stocker les CSV
output_dir = "csv_files"
os.makedirs(output_dir, exist_ok=True)

# Génération des fichiers CSV
for categorie in categories:
    data = []
    for _ in range(random.randint(10, 20)):  # Entre 10 et 20 produits par fichier
        produit = random.choice(noms_produits[categorie])
        quantite = random.randint(1, 100)
        prix_unitaire = round(random.uniform(5.0, 500.0), 2)
        data.append({"Nom du produit": produit, "Quantité": quantite, "Prix unitaire": prix_unitaire, "Catégorie": categorie})

    # Sauvegarder dans un fichier CSV avec encodage utf-8-sig
    df = pd.DataFrame(data)
    csv_path = os.path.join(output_dir, f"{categorie.lower()}.csv")
    df.to_csv(csv_path, index=False, encoding="utf-8-sig", sep=";")
    print(f"Fichier corrigé généré avec utf-8-sig : {csv_path}")
