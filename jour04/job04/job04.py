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
    
if __name__ == "__main__":
    rec = Rectangle(3, 10)
    print(f"Dimentsion du rectangle: Hauteur: {rec.get_hauteur()} Largeur: {rec.get_largeur()}")
    print(f"Aire du rectangle: {rec.aire()}")