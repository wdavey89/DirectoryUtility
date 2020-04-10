import os
def CheckValidDirectory(directory):
    try:
        os.chdir(directory)
        return directory
    except FileNotFoundError:
        return ("Directory does not exist")

def CountAmountOfFiles(directory):
    try:
        os.chdir(directory)
        path, dirs, files = next(os.walk(directory))
        count = len(files)-1
        return count
    except FileNotFoundError:
        return ("Directory does not exist")

def CountAmountOfFilesWithSpecificExtension(directory, extension):
    try:
        os.chdir(directory)
        amountOfFiles = []
        for file in os.listdir(directory):
            if file.endswith(extension):
                amountOfFiles.append(file)
        return amountOfFiles


    except FileNotFoundError:
        return("Directory does not exist")

