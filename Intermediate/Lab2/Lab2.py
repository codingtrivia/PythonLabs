# Q1: Below function prints numbers in increasing order (till the number passed into the function). What do we need to change
# in this function so that it prints downwards in decreasing order.
# If you can write down call stack and value of number on every call, that would help.
def print_up_down(number):
    if(number == 0):
        return 0
    print_up_down(number-1)
    print(number)

print_up_down(2)


#Q2 Below code adds first n numbers.
def add_n_numbers_rec(n):
    if(n == 0):
        return 0
    return n + add_n_numbers_rec(n-1)

# Factorial is similar, except it just multiplies first n numbers. Please write function for calculating factorial.
def factorial(n):
    # Your code goes here.
