class Livre: 
    def __init__(self, titre, auteur, nombre_pages):
        self.titre = titre 
        self.auteur = auteur 
        self.nombre_pages = nombre_pages
        
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
       
livre = Livre("Harry Potter", "J.K. Rowling", 223)


livre.setTitre("Le Prince de Mars")
livre.setAuteur("Mary Dbr",)
livre.setNombrePages(345)


print("Titre:", livre.getTitre())
print("Auteur:", livre.getAuteur())
print("Nombre de pages:", livre.getNombrePages())            
        