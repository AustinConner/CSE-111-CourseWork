class task_blueprint:
    def __init__(self, task_id, name, priority, time_to_complete):
        self.id = task_id
        self.name = name
        self.priority = priority
        self.complete_by = time_to_complete
    
    def __str__(self):
        return f"Task(ID: {self.id}, Name: '{self.name}', Priority: {self.priority}, Complete By: {self.complete_by})"
    # Add this method
    def __repr__(self):
        return self.__str__()

task = [task_blueprint("34434", "my awesome task", "p4", "12/2/34"), task_blueprint("344", "my awesome task443", "p4", "12/5/34")]

print(task)