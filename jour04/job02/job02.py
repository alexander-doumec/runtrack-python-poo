from job01 import Eleve, Professeur

if __name__ == "__main__":
    student = Eleve()
    student.bonjour()
    student.modifierAge(15)
    student.afficherAge()
    master = Professeur()
    master.modifierAge(40)
    master.afficherAge()
    master.enseigner()