class Vehicule : 
    def __init__(self, marque, modele, annee, prix):
        self.__marque = marque
        self.__modele = modele 
        self.__annee = annee 
        self.__prix = prix 
        
    def get_marque(self):
        return self.__marque
    
    def set_marque(self, marque):
        self.__marque = marque
        
    def get_modele(self): 
        return self.__modele 
    
    def set_modele(self, modele):
        self.__modele = modele
        
    def get_annee(self):
        return self.__annee
    
    def set_annee(self, annee):
        self.__annee = annee
        
    def get_prix(self):
        return self.__prix
    
    def set_prix(self, prix):
        self.__prix = prix  
        
class Voiture(Vehicule):
    def __init__(self, marque, modele, annee, prix, portes=4):
        super().__init__(marque=marque, modele=modele, annee=annee, prix=prix)
        self.__portes = portes 
        
    def get_portes(self):
        return self.__portes
    
    def set_portes(self, portes):
        self.__portes = portes
        
    def informationsVehicule(self):
        print(f"Marque: {self.get_marque}")
        print(f"Model : {self.get_modele}")
        print(f"Prix : {self.get_prix}")
        print(f"Nombre de porte : {self.get_portes}")
        
    def demarrer(self):
        print(f"Je roule avec {self.get_portes()} portes")
        
class Moto(Vehicule):
    def __init__(self, marque, modele, annee, prix, roues=2):
        super().__init__(marque=marque, modele=modele, annee=annee, prix=prix)
        self.__roues = roues