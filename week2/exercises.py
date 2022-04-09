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

