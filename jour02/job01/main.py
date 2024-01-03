class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    def getLongueur(self):
        return self.__longueur

    def getLargeur(self):
        return self.__largeur

    def setLongueur(self, longueur):
        if longueur >= 0:
            self.__longueur = longueur
        else:
            print("Erreur: la longueur doit être supérieure ou égale à 0.")

    def setLargeur(self, largeur):
        if largeur >= 0:
            self.__largeur = largeur
        else:
            print("Erreur: la largeur doit être supérieure ou égale à 0.")


rectangle = Rectangle(10, 5)


rectangle.setLongueur(12)
rectangle.setLargeur(6)


print("Longueur:", rectangle.getLongueur())
print("Largeur:", rectangle.getLargeur())