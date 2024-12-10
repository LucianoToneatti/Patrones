from file_component import FileComponent

class File(FileComponent):
    def __init__(self, name):
        self.name = name

        
    def show_details(self):
        print(self.name)