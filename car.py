from vehicle import Vehicle

class Car(Vehicle):

    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    def turn(self, direction):
        print(f"Odbočím do {direction}")

    def __str__(self):
        return f"name: {self.name}, color: {self.color}"


