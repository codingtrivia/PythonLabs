# Below is class specification of a Car. Some data attributes of class are: name,color,model. __init__ function is always called
# by python when we create an object of this class. We have defined some methods (or functions) of this class e.g. whoareyou
# is one method. Please add another method by the name: "all_in_one_string()" that prints below string by using self
# I am Honda and my color is: White and my model is: LX
# I am Honda and my color is: Black and my model is: EX

class Car:
    number_of_cars = 0

    def __init__(self, name, color, model):
        self.name = name
        self.color = color
        self.model = model
        Car.number_of_cars += 1

    def who_are_you(self):
        print("I am " + self.name)
        print("I have {}".format(self.color) + " color")
        print("My model is: {}".format(self.model))

    @classmethod
    def how_many_cars(cls):
        print("We have "+ str(cls.number_of_cars) + " cars now\n")


    def remove_a_car(self):
        print("{} is being removed!".format((self.name)))

        Car.number_of_cars -= 1

        if Car.number_of_cars == 0:
            print("{} was the last one".format(self.name))
        else:
            print("There are still {:d} cars".format(Car.number_of_cars))


class Honda(Car):
    pass

class Toyota(Car):
    pass


white_car = Car("Honda", "White", "LX")
black_car = Car("Honda", "Black", "EX")

white_car.all_in_one_string()
black_car.all_in_one_string()
