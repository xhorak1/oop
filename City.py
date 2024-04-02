class City:

    def __init__(self, name, country, citizens):
        self.name = name
        self.country = country
        self.citizens = citizens

    def __str__(self):
        return f"""Name: {self.name}
Country: {self.country}, Citizens: {self.citizens}"""

c1 = City("Praha", "Czechia", "10 000 000")
c2 = City("Berlin", "Germany", "10 000 000")
print(c1)





