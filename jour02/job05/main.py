class Voiture:
    def __init__(self, marque, modele, annee, kilometrage, en_marche=False, reservoir=50):
        self._marque = marque
        self._modele = modele
        self._annee = annee
        self._kilometrage = kilometrage
        self._en_marche = en_marche
        self._reservoir = reservoir

    # Mutateurs
    def setMarque(self, nouvelle_marque):
        self._marque = nouvelle_marque

    def setModele(self, nouveau_modele):
        self._modele = nouveau_modele

    def setAnnee(self, nouvelle_annee):
        self._annee = nouvelle_annee

    def setKilometrage(self, nouveau_kilometrage):
        self._kilometrage = nouveau_kilometrage

    def setEnMarche(self, en_marche):
        self._en_marche = en_marche

    def setReservoir(self, nouveau_reservoir):
        self._reservoir = nouveau_reservoir

    # Assesseurs
    def getMarque(self):
        return self._marque

    def getModele(self):
        return self._modele

    def getAnnee(self):
        return self._annee

    def getKilometrage(self):
        return self._kilometrage

    def getEnMarche(self):
        return self._en_marche

    def getReservoir(self):
        return self._reservoir

    # Méthode privée pour vérifier le niveau du réservoir
    def _verifier_plein(self):
        return self._reservoir

    # Méthode pour démarrer la voiture
    def demarrer(self):
        niveau_reservoir = self._verifier_plein()
        if niveau_reservoir > 5:
            self._en_marche = True
            print("La voiture a démarré.")
        else:
            print("La voiture ne peut pas démarrer, le réservoir est trop bas.")

    # Méthode pour arrêter la voiture
    def arreter(self):
        self._en_marche = False
        print("La voiture s'est arrêtée.")

# Création d'une instance de la classe Voiture
ma_voiture = Voiture(marque="Toyota", modele="Corolla", annee=2020, kilometrage=15000)

# Affichage des informations initiales
print(f"Marque: {ma_voiture.getMarque()}")
print(f"Modèle: {ma_voiture.getModele()}")
print(f"Année: {ma_voiture.getAnnee()}")
print(f"Kilométrage: {ma_voiture.getKilometrage()}")
print(f"En marche: {ma_voiture.getEnMarche()}")
print(f"Reservoir: {ma_voiture.getReservoir()}")

# Démarrage de la voiture
ma_voiture.demarrer()

# Arrêt de la voiture
ma_voiture.arreter()
