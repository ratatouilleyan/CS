#Project (integer identifier) contains tasks: agglomeration
#task completed by workers: composition
#employee and hired contractor are subclasses of worker: inheritance

class Worker:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return self.name

class employee(Worker):
    def __init__(self, name):
        super().__init__(name)
    def __str__(self):
        return self.name + '(employee)'

class hired_contractor(Worker):
    def __init__(self, name):
        super().__init__(name)
    def __str__(self):
        return self.name + '(hired_contractor)'

class Project:
    def __init__(self, identifier):
        self.identifier = identifier
        self.tasks = []
    def add_task(self, task):
        self.tasks.append(task)
    def __str__(self):
        return 'Project ' + str(self.identifier) + ':\n' + '\n'.join([str(t) for t in self.tasks])

class Task:
    def __init__(self, identifier):
        self.identifier = identifier
        self.workers = []
    def add_worker(self, worker):
        self.workers.append(worker)
    def __str__(self):
        return 'Task ' + str(self.identifier) + ' completed by: ' + ', '.join([str(w) for w in self.workers])

task1 = Task(1)
task2 = Task(2)

alex = employee('alex')
bob = hired_contractor('bob')

task1.add_worker(alex)
task1.add_worker(bob)
task2.add_worker(alex)

project = Project(101)
project.add_task(task1)
project.add_task(task2)
print(project)
