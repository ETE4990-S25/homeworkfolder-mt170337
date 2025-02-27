import json
save_file_name = "savefile.json"
save_file_list = []

#person and child class student
class Person(object):
    def __init__(self,name,age,email):
        self.name = name
        self.age = age
        self.email = email


class Student(Person):
    def __init__(self, name, age, email, student_id):
        super().__init__(name, age, email)
        self.student_id = student_id

# saver and loader code
def saver(obj):
    if isinstance(obj,Person):
        save_file_list.append(obj.__dict__)

        with open(save_file_name, 'w') as file:
            json.dump(save_file_list, file)

def loader():
    with open(save_file_name) as file:
        save_file_list = json.load(file)
    print(json.dumps(save_file_list, indent=2))

