from math import pi 

class Forme: 
    def __init__(self):
        pass
    
    def aire(self):
        return 0 

class Rectangle(): 
    def __init__(self, hauteur, largeur):
        super().__init__()
        self.__hauteur = hauteur
        self.__largeur = largeur
        
    def get_hauteur(self):
        return self.__hauteur
    
    def set_hauteur(self, hauteur):
        self.__hauteur = hauteur
        
    def get_largeur(self):
        return self.__largeur
    
    def set_largeur(self, largeur):
        self.__largeur = largeur
        
    def aire(self):
        return self.get_hauteur() * self.get_largeur() 
          
class Cercle:
    def __init__(self, radius ):
        super().__init__()
        self.__radius = radius
        
    def get_radius(self):
        return self.__radius
    
    def set_radius(self, radius):
        self.__radius = radius
        
    def aire(self):
        return pi * self.get_radius() ** 2
    
if __name__ == "__main__":
    rec = Rectangle(3, 10)
    cercle = Cercle(10)
    print(f"Dimension du rectangle: Longueur: {rec.get_length()}  Largeur: {rec.get_width()}")
    print(f"Aire du rectangle: {rec.aire()}")
    print(f"Rayon du cercle: {cercle.get_radius()}")
    print(f"Aire du cercle: {cercle.aire()}")