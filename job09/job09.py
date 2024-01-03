class Produit:
    def __init__(self, nom, prixHT, TVA):
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA

    def calculerPrixTTC(self):
        return self.prixHT * (1 + self.TVA)

    def afficher(self):
        print(f"Nom : {self.nom}")
        print(f"Prix HT : {self.prixHT}")
        print(f"TVA : {self.TVA}")
        print(f"Prix TTC : {self.calculerPrixTTC()}")

    def modifierNom(self, nouveau_nom):
        self.nom = nouveau_nom

    def modifierPrix(self, nouveau_prix):
        self.prixHT = nouveau_prix

    def getNom(self):
        return self.nom

    def getPrixHT(self):
        return self.prixHT

    def getTVA(self):
        return self.TVA
    
produit1 = Produit("Produit A", 10, 0.2)
produit2 = Produit("Produit B", 15, 0.15)

for i, produit in enumerate([produit1, produit2], start=1):
    print(f"\nProduit {i} :")
    produit.afficher()
    
produit1.modifierNom("Nouveau Produit A")
produit1.modifierPrix(12)

produit2.modifierNom("Nouveau Produit B")
produit2.modifierPrix(17)

for i, produit in enumerate([produit1, produit2], start=1):
    print(f"\nProduit {i} :")
    produit.afficher()