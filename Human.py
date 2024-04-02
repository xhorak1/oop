class Human:

    def __init__(self, name, date, number, city, country, address):
        self.__name = name
        self.date = date
        self.number = number
        self.city = city
        self.country = country
        self.address = address

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        if len(new_name) < 3:
            return False
        self.__name = new_name
        return True



Human1 = Human("Kuba", "20.5.1987", "628822432", "Stašov", "Czechia", "Neřeknu")
Human2 = Human("Pavel", "02.04.1990", "187538715", "Brno", "Czechia", "neznámá")


print(Human2.date)
print(Human1.get_name())