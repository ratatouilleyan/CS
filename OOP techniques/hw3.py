'''
Class
+name: str
+topic:str
+name_of_teacher: str
+number_of_participants: int

+__init__(name:str, topic:str, name_of_teacher:str, number_of_participants:int)
+__str__():str

'''

class Course:
    def __init__(self, name, topic, name_of_teacher, num_of_participants):
        self.name = name
        self.topic = topic
        self.name_of_teacher = name_of_teacher
        self.num_of_participants = num_of_participants
    def __str__(self):
        return f'{self.name} ({self.topic}) by {self.name_of_teacher} with {self.num_of_participants} participants'

c = Course('Computer Science', 'OOP', 'Jarmo Hurri', 20)
print(c)

