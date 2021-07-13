class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        return self.name + " " + self.surname

    def get_total_income(self):
        return self._income["wage"]+self._income["bonus"]


A1 = Position("Иван", "Иваныч", "прораб", 10000, 1000)
print(A1.name)
print(A1.get_full_name())
print(A1.position)
print(A1.get_total_income())
