class Personne : 
    def __init__(self, prenom, nom):
        self.nom = nom
        self.prenom = prenom

    def se_presenter(self):
        return f"Je suis {self.prenom} {self.nom}"
    
personne1 = Personne("Jhon", "Doe")
personne2 = Personne("Jean", "Dupont")

print(personne1.se_presenter())
print(personne2.se_presenter())