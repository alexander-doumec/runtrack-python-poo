import random

class Personnage:
    def __init__(self, nom, vie):
        self.nom = nom
        self.vie = vie

    def attaquer(self, adversaire):
        degats = random.randint(1, 10)
        adversaire.vie -= degats
        print(f"{self.nom} attaque {adversaire.nom} pour {degats} points de dégâts!")

    def verifierSante(self):
        if self.vie <= 0:
            print(f"{self.nom} est mort!")
            return False
        else:
            print(f"{self.nom} a encore {self.vie} points de vie.")
            return True

class Jeu:
    def __init__(self):
        self.niveau = 0

    def choisirNiveau(self):
        self.niveau = int(input("Choisissez le niveau de difficulté (1-3): "))

    def lancerJeu(self):
        joueur = Personnage("Joueur", 100 * self.niveau)
        ennemi = Personnage("Ennemi", 150 * self.niveau)

        while True:
            joueur.attaquer(ennemi)
            if not ennemi.verifierSante():
                print(f"{joueur.nom} a gagné!")
                break

            ennemi.attaquer(joueur)
            if not joueur.verifierSante():
                print(f"{ennemi.nom} a gagné!")
                break

jeu = Jeu()
jeu.choisirNiveau()
jeu.lancerJeu()