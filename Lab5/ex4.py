class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_info(self):
        return f"Name: {self.name}, Salary: {self.salary}"


class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def display_info(self):
        return f"Name: {self.name}, Salary: {self.salary}, Department: {self.department}"

    def assign_task(self, task):
        return f"{self.name} is assigning the task: {task}"


class Engineer(Employee):
    def __init__(self, name, salary, project):
        super().__init__(name, salary)
        self.project = project

    def display_info(self):
        return f"Name: {self.name}, Salary: {self.salary}, Project: {self.project}"

    def start_work(self):
        return f"{self.name} is starting work on {self.project}"


class Salesperson(Employee):
    def __init__(self, name, salary, quota):
        super().__init__(name, salary)
        self.quota = quota

    def display_info(self):
        return f"Name: {self.name}, Salary: {self.salary}, Quota: {self.quota}"

    def meet_quota(self, actual_sales):
        if actual_sales >= self.quota:
            return f"{self.name} has met the sales quota."
        else:
            return f"{self.name} has not met the sales quota yet."


manager = Manager("John Doe", 80000, "Human Resources")
print(manager.display_info())
print(manager.assign_task("Fire Steve!"))
print()

engineer = Engineer("James Bond", 70000, "Project X")
print(engineer.display_info())
print(engineer.start_work())
print()

salesperson = Salesperson("Minecraft Steve", 60000, 100000)
print(salesperson.display_info())
print(salesperson.meet_quota(120000))
