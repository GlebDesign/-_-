from Vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, make, model, fuel_type):
        super().__init__(make, model)
        self.fuel_type = fuel_type

    def get_info(self):
        return self.make, self.model, self.fuel_type

car = Car('audi', 'q7', '95')
print(car.get_info())