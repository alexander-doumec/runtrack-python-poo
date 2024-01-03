class Personnage:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def gauche(self):
        self.x -= 1

    def droite(self):
        self.x += 1

    def bas(self):
        self.y -= 1

    def haut(self):
        self.y += 1

    def position(self):
        return (self.x, self.y)

# Instanciation d'un personnage
personnage1 = Personnage(0, 0)

# Utilisation des méthodes pour vérifier tout fonctionne correctement
print(personnage1.position())

personnage1.droite()
print(personnage1.position())

personnage1.bas()
print(personnage1.position())

personnage1.gauche()
print(personnage1.position())

personnage1.haut()
print(personnage1.position())