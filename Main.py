import os
from DirectoryUtility import CheckValidDirectory
from DirectoryUtility import CountAmountOfFiles
from DirectoryUtility import CountAmountOfFilesWithSpecificExtension

def main():
    checkDirectoryExists()
    GetAmountOfFilesInDirectory()
    GetAmountOfFilesWithSpecificExtension()

def checkDirectoryExists():
    directory = 'DirectoryGoesHere'
    print("Directory Available: {}".format(CheckValidDirectory(directory)))

def GetAmountOfFilesInDirectory():
    directory = 'DirectoryGoesHere'
    count = CountAmountOfFiles(directory)
    print("There are {} files in {} ".format(count, directory))

def GetAmountOfFilesWithSpecificExtension():
    directory = 'DirectoryGoesHere'
    extension = '.txt'
    count = len(CountAmountOfFilesWithSpecificExtension(directory, extension))
    print("There are {} files in {} with the {} extension ".format(count, directory, extension))

if __name__ == "__main__":
    main()