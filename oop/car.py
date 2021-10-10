class Car:
    def __init__(self, model, company, year, color):
        self.model = model
        self.company = company
        self.year = year
        self.color = color

    def description(self):
        # print(f"{self.model} {self.company} {self.year}")
        return f"{self.model} {self.company} {self.year}"



my_car = Car('x4','BMW','2019','black')

mc = my_car.description()

print(mc.title())