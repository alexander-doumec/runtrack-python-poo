class Point: 
    def __init__(self, x, y):
        self.x = x
        self.y = y 

    def afficherLesPoints(self):
        return f"Les coordonnées du point sont: ({self.x}, {self.y})"
    
    def afficher_x(self):
        return f"La coordonnées x du point est: {self.x}"
    
    def afficher_y(self):
        return f"La coordonnées y du point est: {self.y}"
    
    def changer_x(self, nouvelle_valeur_x):
        self.x = nouvelle_valeur_x
        return f"La nouvelle valeur de x du point est: {self.x}"
    
    def changer_y(self, nouvelle_valeur_y):
        self.y = nouvelle_valeur_y 
        return f"La nouvelle valeur de y du point est: {self.y}"   
    

point1 = Point(2,3)

print(point1.afficherLesPoints())
print(point1.afficher_x())
print(point1.afficher_y())

point1.changer_x(4)
point1.changer_y(10)

print(point1.afficherLesPoints())
print(point1.afficher_x())
print(point1.afficher_y)