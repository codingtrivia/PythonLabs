# Please list out following details.
# what are instance methods in class Car ?
# What are instance methods that Honda can call (or has access to ?)
# Which methods were overridden in class Honda ?
# What will happen if I remove @staticmethod decorator from tell_me_how_car_works ? And why ?
# What is purpose of __str__ function defined in class Car (You may refer to this URL: https://docs.python.org/3/reference/datamodel.html#object.__str__) and a hint: this is a function that is redefined by a class and is called by python framework(just like __init__)
# How many object (or instance) attributes will Honda have if we uncomment __init__ function (currently commented in Honda).
# Define a new class (that inherits from Honda and name that class as: "Element". Re-define __init__ method and add a new attribute: wheels (of type string)
# what will the output of "print(honda.__dict__)" Followup questions: what is __dict__
# Call __init__ method of Car in Honda by using super. We will cover this in next session, but if you have sometime, please use this link to read a bit about super here: https://docs.python.org/3/library/functions.html#super. Please feel free to google (super in Python)
# What are: isinstance() and issubclass() methods. Where are they defined ?

class Car:
    number_of_cars = 0
    def __init__(self, name, color, model):
        self.name = name
        self.color = color
        self.model = model
        Car.number_of_cars = Car.number_of_cars + 1

    def who_are_you(self):
        print("I am " + self.name)
        print("I have {}".format(self.color) + " color")
        print("My model is: {}".format(self.model))

    @classmethod
    def how_many_cars(cls):
        print("We have "+ str(cls.number_of_cars) + " cars now\n")

    @staticmethod
    def tell_me_how_car_works():
         print("Car is a machine");

    def remove_a_car(self):
        print("{} is being removed!".format((self.name)))

        Car.number_of_cars -= 1

        if Car.number_of_cars == 0:
            print("{} was the last one".format(self.name))
        else:
            print("There are still {:d} cars".format(Car.number_of_cars))

    def __del__(self):
        #print("Deleting {}".format(self.color))
        pass

    def __str__(self):
        return "I am " + self.name + " I have {}".format(self.color) + " color" + " My model is: {}".format(self.model)

class Honda(Car):
    number_of_cars = 0
    # def __init__(self, color):
    #     self.color = color
    def who_are_you(self):
        print("My color is: " + self.color)
    def exlusive_honda_func(self):
        print("This is my exclusive function, btw I am: " + self.name)

class Toyota(Car):
    pass


white_car = Car("whiteCar", "White", "LX")
black_car = Car("blackCar", "Black", "EX")

honda = Honda("hondaWhiteCar", "White", "LX")

Car.how_many_cars()
Honda.how_many_cars()

