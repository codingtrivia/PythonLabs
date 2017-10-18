#Q1: # What do I need to put at line 15 that says: "<your code here.>" in order to print 1 followed by 3 followed by 2

def func_one():
    print("1")

def func_two():
    func_three()
    print("2")

def func_three():
    func_one()
    print("3")

def calling_func():
    # <your code here.>

calling_func()





#Q2: # What will be output of below program and why ?

def yet_another_function():
    print("yet another function")


def another_function():
    yet_another_function()
    print("another function")


def my_func():
    another_function()
    print("my function")

my_func()


#Q3: # What will happen if we add a return (as in line 48 below) ? And why does that happen ?
def yet_another_function():
    print("yet another function")


def another_function():
    yet_another_function()
	return 2
    print("another function")


def my_func():
    another_function()
    print("my function")

my_func()


