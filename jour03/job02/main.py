class CompteBancaire : 
    def __init__(self, id_compte, prenom, nom, balance, decouvert):
        self.__id_compte = id_compte
        self.__prenom = prenom
        self.__nom = nom
        self.__balance = balance
        self.__decouvert = decouvert
        self.__taux_agios = 0.05
        
    def get_id(self):
        return self.__id_compte
    
    def get_balance(self):
        return self.__balance
    
    def afficher(self):
        print(f"Numéro de compte : {self.__id_compte}")
        print(f"Titulaire: {self.__prenom}: {self.__nom}")
        self.afficherSolde()
        
    def afficherSolde(self):
        print(f"Solde du compte n°{self.get_id()}: {self.__balance}€")
    
    def versement(self, paiement):
        self.__balance += paiement 
        
    def retrait(self, retirer):
        if type(retirer) == int: 
            if self.__balance >= retirer or self.__decouvert is True:
                self.__balance -= retirer 
                self.afficherSolde()
                return True
            
            else: 
                print(f"Solde insuffisant pour un retrait de {retirer}€ sur le compte n° sur le compte n°{self.get_id()}")
                self.afficherSolde()
                return False
        
    def agios(self):
        if self.__balance < 0:
            self.__balance -= self.__balance * self.__taux_agios
            
    def virement(self, compte, transfert_montant):
        if self.retrait(transfert_montant):
            compte.versement(transfert_montant)
                
                
if __name__ == "__main__":
    compte1 = CompteBancaire(1, "Doe", "John", 10000, False)
    compte2 = CompteBancaire(2, "Dilan", "Bob", 2000, True)

    compte1.afficher()
    compte2.afficher()

    compte1.versement(2000)
    compte1.retrait(20000)
    compte2.retrait(5000)

    compte1.afficher()
    compte2.afficher()
    compte1.virement(compte2, abs(compte2.get_balance()))
    compte1.afficher()
    compte2.afficher()
        
        