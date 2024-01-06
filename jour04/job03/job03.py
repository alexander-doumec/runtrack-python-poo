class Rectangle:
    def __init__(self, largeur, longueur):
        self.__largeur = largeur
        self.__longueur = longueur

    def get_largeur(self):
        return self.__largeur

    def set_largeur(self, largeur):
        self.__largeur = largeur

    def get_longueur(self):
        return self.__longueur

    def set_longueur(self, longueur):
        self.__longueur = longueur

    def perimetre(self):
        return 2 * (self.get_longueur() + self.get_largeur())

    def surface(self):
        return self.get_largeur() * self.get_longueur()


class Parallelepipede(Rectangle):
    def __init__(self, largeur, longueur, hauteur):
        super().__init__(largeur=largeur, longueur=longueur)
        self.__hauteur = hauteur

    def get_hauteur(self):
        return self.__hauteur

    def set_hauteur(self, hauteur):
        self.__hauteur = hauteur

    def volume(self):
        return self.surface() * self.__hauteur


if __name__ == "__main__":
    rec = Rectangle(3, 10)
    print(f"Dimensions du rectangle: Longueur: {rec.get_longueur()}   Largeur: {rec.get_largeur()}")
    print(f"Périmère: {rec.perimetre()}  Aire: {rec.surface()}")

    para= Parallelepipede(3, 10, 7)
    print(f"Dimensions du parallélépipède: Longueur: {para.get_longueur()}  Largeur: {para.get_largeur()}  Hauteur: {para.get_hauteur()}")
    print(f"Volume: {para.volume()}")