
class Boss:
    def notice(self):
        print("I'm Your Boss & have access of Everything (:p)\n")

class Employee(Boss):
    def __init__(self,name,percentage):
        self.name=name
        self.percentage=percentage
        self.status=self.grade

    @property
    def grade(self):
        if self.percentage >= 85:
            return "A+"
        elif self.percentage>=75:
            return "A"
        else:
            return "B"

    @grade.setter            
    def grade(self):
        if self.percentage >= 85:
            return "A+"
        elif self.percentage>=75:
            return "A"
        else:
            return "B"

                
    
    def Info(self):
        print(f"Your Name: {self.name}\nPercentage: {self.percentage}\nMerit: {self.status}")






staff1=Employee("Aryakumar_Jaiswal",83)
staff1.status='A++'
staff1.Info()
staff1.notice()
