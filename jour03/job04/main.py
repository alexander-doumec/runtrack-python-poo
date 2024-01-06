
class Joueur:
    def __init__(self, name, surname, number, position, nb_goal=0, nb_pass=0, yellow=0, red=0):
        self.__name = name
        self.__surname = surname
        self.__number = number
        self.__position = position
        self.__goals = nb_goal
        self.__pass = nb_pass
        self.__yellow = yellow
        self.__red = red

    def get_name(self):
        return self.__name

    def get_surname(self):
        return self.__surname

    def get_number(self):
        return self.__number

    def set_number(self, number):
        self.__number = number

    def get_position(self):
        return self.__position

    def set_position(self, position):
        self.__position = position

    def marquerUnBut(self):
        self.__goals += 1

    def effectuerUnePasseDecisive(self):
        self.__pass += 1

    def recevoirUnCartonJaune(self):
        self.__yellow += 1

    def recevoirUnCartonRouge(self):
        self.__red += 1

    def afficherStatistiques(self):
        return (self.__number, self.__position, self.__name, self.__surname, self.__goals, self.__pass, self.__yellow, self.__red)


class Equipe:
    def __init__(self, name):
        self.__name = name
        self.__team = []

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def ajouterJoueur(self, player):
        self.__team.append(player)

    def mettreAJourStatistiquesJoueur(self, player_id, goal, passe, yellow, red):
        for k in self.__team:
            if k.get_number() == player_id:
                if goal != 0:
                    for _ in range(goal):
                        k.marquerUnBut()
                if passe != 0:
                    for _ in range(passe):
                        k.effectuerUnePasseDecisive()
                if yellow != 0:
                    if yellow == 1:
                        k.recevoirUnCartonJaune()
                    if yellow == 2:
                        k.recevoirUnCartonJaune()
                        k.recevoirUnCartonRouge()
                        break
                if red == 1:
                    k.recevoirUnCartonRouge()

    def AfficherStatistiquesJoueurs(self):
        print(f"{'*' * 120}")
        print(f"{self.get_name():^120}")
        print(f"{'*' * 120}")
        nb, position, nom, prenom, but, passe, jaune, rouge = "Numéro", "Position", "Nom", "Prénom", "buts", "Passes déc.", "C. Jaune", "C. Rouge"
        header = f"{nb:^10}|{position:^30}|{nom:^15}|{prenom:^15}|{but:^4}|{passe:^20}|{jaune:^10}|{rouge:^10}"
        print(header)
        print(f"{'-' * 120}")
        for k in self.__team:
            nb, position, nom, prenom, but, passe, jaune, rouge = k.afficherStatistiques()
            body = f"{nb:^10}|{position:^30}|{nom:^15}|{prenom:^15}|{but:^4}|{passe:^20}|{jaune:^10}|{rouge:^10}"
            print(body)
            

if __name__ == "__main__":
    from random import randint

    postes = {'1': "Gardien",
              '2': "Arrière latéral gauche",
              '3': "Arrière latéral droit",
              '4': "Stoppeur",
              '5': "Libéro",
              '6': "Milieu défensif",
              '7': "Milieu défensif",
              '8': "Milieu offensif",
              '9': "Avant-centre",
              '10': "Milieu offensif",
              '11': "Le 2e attaquant"}

    def match_aleatoire(equip1, equip2):
        for k in range(1, 12):
            equip1.mettreAJourStatistiquesJoueur(k, randint(0, 2), randint(0, 10), randint(0, 10), randint(0, 10))
            equip2.mettreAJourStatistiquesJoueur(k, randint(0, 2), randint(0, 10), randint(0, 10), randint(0, 10))


    equipe1 = Equipe("Equipe 1")
    equipe2 = Equipe("Equipe 2")

    for k in range(1, 12):
        equipe1.ajouterJoueur(Joueur(f"Name{k}", f"Surname{k}", int(f"{k}"), postes[str(k)]))
        equipe2.ajouterJoueur(Joueur(f"Name{k}", f"Surname{k}", int(f"{k}"), postes[str(k)]))

    equipe1.AfficherStatistiquesJoueurs()
    print()
    equipe2.AfficherStatistiquesJoueurs()
    
    print(f"{'*' * 120}")
    print(f"{'*' * 120}")
    match_aleatoire(equipe1, equipe2)
    print()
    equipe1.AfficherStatistiquesJoueurs()
    print()
    equipe2.AfficherStatistiquesJoueurs()
