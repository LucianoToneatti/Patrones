from file_component import FileComponent

class Folder(FileComponent):
    def __init__(self, name):
        self.name = name
        self.files = []

    def add(self, file):
        self.files.append(file)

    def show_details(self):
        print(self.name)
        for file in self.files:
            file.show_details()