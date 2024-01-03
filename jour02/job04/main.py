class Student: 
    def __init__(self,nom, prenom, student_id):
        self.__nom = nom 
        self.__prenom = prenom
        self.__student_id = student_id 
        self.__credits = 0
        
    def add_credits(self, credits):
        if credits > 0:
            self.__credits += credits 
            
    def studentEval(self):
        if self.__credits > 90:
            return "Excellent"
        elif self.__credits >= 80:
            return "Très bien"
        elif self.__credits >= 70:
            return "Bien"
        elif self.__credits >= 60:
            return "Passable"
        else:
            return "Insuffisant"
        
    def studentInfo(self):
        print(f"Nom: {self.__nom}")
        print(f"Prénom: {self.__prenom}")
        print(f"Identifiant étudiant: {self.__student_id}")
        print(f"Niveau: {self.studentEval()}")


john_doe = Student("Doe", "John", 145)


john_doe.add_credits(30)
john_doe.add_credits(20)
john_doe.add_credits(40)


john_doe.studentInfo()