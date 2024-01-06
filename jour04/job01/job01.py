class Personne:
    def __init__(self, age=14):
        self._age = age

    def afficherAge(self):
        print(f"Age: {self._age} ans")

    def modifierAge(self, age):
        self._age = age

    def bonjour(self):
        print("Hello")


class Eleve(Personne):
    def __init__(self):
        super().__init__()

    def afficherAge(self):
        print(f"J'ai {self._age} ans")

    def allerEnCours(self):
        print("Je vais en cours")


class Professeur(Personne):
    def __init__(self, subject="Informatique"):
        super().__init__()
        self.__matiereEnseignee = subject

    def enseigner(self):
        print(f"Le cours \"{self.__matiereEnseignee}\" va commencer")


if __name__ == "__main__":
    people = Personne()
    student = Eleve()
    student.afficherAge()