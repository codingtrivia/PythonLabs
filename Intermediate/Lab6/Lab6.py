# Define a class named: "Files" and define a staticmethod (@staticmethod) method that takes two arguments:
# first argument: filename (e.g.: my_first_file.txt)
# second argument: a string that would be written to the file.
# The static method will create 10 files (use a for loop to implement this). The files would be created in the directory: c:\\PythonFiles.
# 10 files should be named something like: my_first_file_1.txt, my_first_file_2.txt, my_first_file_3.txt....my_first_file_10.txt
# Please do not use hardcoded names like: c:\\PythonFiles\\my_first_file_1.txt, rather use string append to make filename in the for loop.
# So, something like:
#   for x in range(10)
#       filename = "c:\\PythonFiles\\ + "my_first_file..." (Please replace ... with your own code)
#       fo = open(filename, "r+")
#       fo.write(<string passed into the function as argument>)
#
# I am putting code snippet from our session today for reference.
def add_and_write_to_a_file(x, y):
    sum_of_numbers = x + y
    try:
        fo = open("c:\\PythonFiles\\my_first_file.txt", "r+")
        fo.write("Sum of numbers is: " + str(sum_of_numbers) + "\n")
    except IOError as e:
        print("Failed with error: ", e, " now opening in w+ mode")
        fo = open("c:\\PythonFiles\\my_first_file.txt", "w+")
        fo.write("Sum of numbers is: " + str(sum_of_numbers) + "\n")
        fo.close()

    return sum_of_numbers




fo = open("c:\\PythonFiles\\my_first_file.txt", "r")
print(fo.read(10))