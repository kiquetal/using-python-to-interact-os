import os
def new_directory(directory, filename):
    # Before creating a new directory, check to see if it already exists
    if os.path.isdir(directory) == False:
        os.mkdir(directory)
    else:
        print("ya existe")
        # Create the new file inside of the new directory
    os.chdir(directory)
    with open(filename,"w") as file:
        pass

    # Return the list of files in the new directory
    os.chdir("..")
    return os.listdir(os.path.join(directory))
print(new_directory("PythonPrograms", "script.py"))

def modifiedTime():
    import datetime
    file = os.path.join("PythonPrograms", "script.py")
    print(os.path.getmtime(file))
    word = datetime.datetime.fromtimestamp(os.path.getmtime(file)).date()
    print(word)

modifiedTime()



import os
import csv

# Create a file with data in it
def create_file(filename):
    with open(filename, "w") as file:
        file.write("name,color,type\n")
        file.write("carnation,pink,annual\n")
        file.write("daffodil,yellow,perennial\n")
        file.write("iris,blue,perennial\n")
        file.write("poinsettia,red,perennial\n")
        file.write("sunflower,yellow,annual\n")

# Read the file contents and format the information about each row

def create_file(filename):
    with open(filename, "w") as file:
        file.write("name,color,type\n")
        file.write("carnation,pink,annual\n")
        file.write("daffodil,yellow,perennial\n")
        file.write("iris,blue,perennial\n")
        file.write("poinsettia,red,perennial\n")
        file.write("sunflower,yellow,annual\n")

def contents_of_file(filename):
    import csv
    import os


    csv_f = csv.reader(filename)
    for row in csv_f:
        name, phone, role = row
        print(f"{name} - {phone} - {role}")





#Call the function
print(contents_of_file("flowers.csv"))
