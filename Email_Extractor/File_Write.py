import os


class File_Write(object):
    def __init__(self):
        # File Name [Private]
        self.__File_Name = "Emails.txt"

    def File_W(self, _Emails):
        # Write text to file
        with open(self.__File_Name, "w") as File:
            for Email in _Emails:
                File.write(Email)
        # File save path
        print(">> File saved: " + os.path.dirname(__file__) + "\\" + self.__File_Name)
