class Vehicle:
    def __init__(self, Make, Model, Color, Fueltype, Options):
        self.Make = Make
        self.Model = Model
        self.Color = Color
        self.Fueltype = Fueltype
        self.Options = Options


    def getMake(self):
        return self.Make


    def getModel(self):
        return self.Model


    def getColor(self):
        return self.Color


    def getFueltype(self):
        return self.Fueltype


    def getOptions(self):
        return self.Options


class Car(Vehicle):
    def __init__(self, Make, Model, Color, Fueltype, Options, engineSize, numDoors):
        super().__init__(Make, Model, Color, Fueltype, Options)
        self.engineSize = engineSize
        self.numDoors = numDoors


    def getEngineSize(self):
        return self.engineSize


    def getNumDoors(self):
        return self.numDoors


    def __str__(self):
        return '''
        Make: {}
        Model: {}
        Color: {}
        Fueltype: {}
        Options: {}
        engineSize: {}
        numDoors: {}
        '''.format(
            self.Make, self.Model, self.Color, self.Fueltype, self.Options, self.engineSize, self.numDoors
        )


class Pickup(Vehicle):
    def __init__(self, Make, Model, Color, Fueltype, Options, cabStyle, bedLength):
        super().__init__(Make, Model, Color, Fueltype, Options)
        self.cabStyle = cabStyle
        self.bedLength = bedLength


    def getCabStyle(self):
        return self.cabStyle


    def getBedLength(self):
        return self.bedLength


    def __str__(self):
        return '''
        Make: {}
        Model: {}
        Color: {}
        Fueltype: {}
        Options: {}
        cabStyle: {}
        bedLength: {}
        '''.format(
            self.Make, self.Model, self.Color, self.Fueltype, self.Options, self.cabStyle, self.bedLength
        )


def garage():
    menu = '''
    1. Add new car
    2. Add new pick up
    3. Show all cars
    4. Show all pick ups
    5. Exit
    Your option: '''
    cars = []
    pick_ups = []
    while True:
        option = int(input(menu))
        if(option == 1):
            add_car(cars)
        elif(option == 2):
            add_pickup(pick_ups)
        elif(option == 3):
            show_cars(cars)
        elif(option == 4):
            show_pickups(pick_ups)
        elif(option == 5):
            break


def add_car(cars):
    menu = '''
    The attributes for a car are Make, Model, Color, Fueltype, Options, engineSize, numDoors
    Enter the values with a comma separating them: '''
    values = input(menu)
    # separate the values
    values = values.split(",")
    # remove extra spaces
    values = [i.strip() for i in values]
    new_car = Car(*values)
    cars.append(new_car)


def add_pickup(pick_ups):
    menu = '''
    The attributes for a pickup are Make, Model, Color, Fueltype, Options, cabStyle, bedLength
    Enter the values with a comma separating them: '''
    values = input(menu)
    # separate the values
    values = values.split(",")
    # remove extra spaces
    values = [i.strip() for i in values]
    new_pickup = Pickup(*values)
    pick_ups.append(new_pickup)


def show_cars(cars):
    print("Your cars:")
    for car in cars:
        print(car)
        print("*"*40)


def show_pickups(pick_ups):
    print("Your pick ups:")
    for pickup in pick_ups:
        print(pickup)
        print("*"*40)


if __name__ == "__main__":
    garage()