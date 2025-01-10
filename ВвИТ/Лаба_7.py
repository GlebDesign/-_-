from ftplib import error_temp
from keyword import kwlist


class Employee:
    def __init__(self, name, id):
        self.name=name
        self.id=id

    def get_info(self):
        return f'Имя:{self.name}, ID:{self.id}'

class Manager(Employee):
    def __init__(self,name, id, department, **kwargs):
        super().__init__(name, id, **kwargs)
        self.department=department

    def manage_project(self):
        return f'Работник {self.name}, учавствует в проекте {self.department} отдела'

    def get_info(self):
        return f"{Employee.get_info(self)}, Отдел: {self.department}"

class Technician(Employee):
    def __init__(self, name, id, specialization, **kwargs):
        super().__init__(name, id, **kwargs)
        self.specialization=specialization

    def perform_maintenance(self):
        return f'Работник{self.name} ,осуществляет техобслуживание в сфере {self.specialization} '

    def get_info(self):
        return f'{Employee.get_info(self)}, Спеуциализация:{self.specialization}'

class TechManager(Manager, Technician):
    def __init__(self, name, id, department, specialization, **kwargs):
        super().__init__(name, id, department=department, specialization=specialization, **kwargs)
        self.team=[]

    def add_employee(self, employye):
        self.team.append(employye)

    def get_team_info(self):
        if not self.team:
            return f"Техменеджер {self.name} не имеет команды"
        info = [f"Команда Техменеджера {self.name}:"]
        for person in self.team:
            info.append(person.get_info())
        return "\n".join(info)

class TechManager2(TechManager):
    def __init__(self, name, id, experience, department, specialization, **kwargs):
        super().__init__(name, id, department, specialization, expirience=experience, **kwargs)

    def get_expirience(self):
        return f'Стаж работника {self.name}, равен {self.expirience}'

person1 = Employee("Миша", 1)
person2 = Technician("Алиса", 2, "Программисти")
person3 = Manager("Вова", 3, "АйТи")

# Создание объект TechManager и добавление сотрудников в его команду
tech_manager = TechManager("Алёна", 4, "Инженерия", "Автоматизация")
tech_manager.add_employee(person1)
tech_manager.add_employee(person2)
tech_manager.add_employee(person3)
tech_manager2=TechManager2('Антон', 5,"3 года", 'Айти',  'программист')

# Вывод информации о команде
print(tech_manager.get_info())
print(tech_manager.get_team_info())

print(tech_manager2.get_expirience())