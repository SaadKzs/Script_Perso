import os
import pandas as pd

# Dossier contenant les fichiers CSV
input_dir = "csv_files"
output_file = "consolidated_inventory.csv"

# Lister les fichiers CSV dans le dossier
csv_files = [f for f in os.listdir(input_dir) if f.endswith('.csv')]

# Liste pour stocker les DataFrames
dataframes = []

# Charger et combiner les fichiers
for file in csv_files:
    file_path = os.path.join(input_dir, file)
    print(f"Chargement du fichier : {file_path}")
    try:
        df = pd.read_csv(file_path, encoding="utf-8-sig", sep=";")
        dataframes.append(df)
    except Exception as e:
        print(f"Erreur lors du chargement du fichier {file_path}: {e}")

# Combiner tous les DataFrames
if dataframes:
    consolidated_df = pd.concat(dataframes, ignore_index=True)

    # Supprimer les doublons
    consolidated_df.drop_duplicates(inplace=True)

    # Enregistrer dans un fichier CSV consolidé
    consolidated_df.to_csv(output_file, index=False, encoding="utf-8-sig", sep=";")
    print(f"Fichier consolidé généré : {output_file}")
else:
    print("Aucun fichier CSV trouvé pour la consolidation.")
