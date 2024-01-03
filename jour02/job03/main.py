class Livre: 
    def __init__(self, titre, auteur, nombre_pages):
        self.titre = titre 
        self.auteur = auteur 
        self.nombre_pages = nombre_pages
        self.__disponible = True
        
    def getTitre(self):
        return self.titre
    
    def getAuteur(self):
        return self.auteur
    
    def getNombrePages(self):
        return self.nombre_pages
    
    def setTitre(self, titre):
        self.__titre = titre 
        
    def setAuteur(self, auteur):
        self.__auteur = auteur
        
    def setNombrePages(self, nombre_pages):
        if isinstance(nombre_pages, int) and nombre_pages > 0:
            self.__nombre_pages = nombre_pages 
        else : 
            print("Erreur : Le nombre de pages doit être un nombre entier positif.")
    def verification(self):
        return self.__disponible
    
    def emprunter(self):
        if self.verification():
            self.__disponible = False
        else: 
            print("Le livre n'est pas disponible")
    def rendre(self):
        if not self.verification():
            self.__disponible = True 
        else : 
            print("Le livre n'a pas été emprunter ")
        
livre = Livre("Harry Potter", "J.K. Rowling", 223)


livre.setTitre("Le Prince de Mars")
livre.setAuteur("Mary Dbr",)
livre.setNombrePages(345)


print("Titre:", livre.getTitre())
print("Auteur:", livre.getAuteur())
print("Nombre de pages:", livre.getNombrePages())            
        