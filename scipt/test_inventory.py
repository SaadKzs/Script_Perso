import unittest
import pandas as pd
from io import StringIO

class TestInventory(unittest.TestCase):
    def setUp(self):
        # Exemple de données pour les tests
        data = """Nom du produit;Quantité;Prix unitaire;Catégorie
Chaise;10;50;Mobilier
Table;5;100;Mobilier
Stylo;20;2;Bureautique
Tondeuse;3;300;Jardinage
"""
        self.df = pd.read_csv(StringIO(data), sep=";")

    def test_recherche_nom_produit(self):
        result = self.df[self.df['Nom du produit'].str.contains("Chaise", case=False)]
        self.assertEqual(len(result), 1)

    def test_recherche_categorie(self):
        result = self.df[self.df['Catégorie'].str.contains("Mobilier", case=False)]
        self.assertEqual(len(result), 2)

    def test_recherche_prix(self):
        result = self.df[(self.df['Prix unitaire'] >= 50) & (self.df['Prix unitaire'] <= 100)]
        self.assertEqual(len(result), 2)

if __name__ == "__main__":
    unittest.main()
