from file import File
from folder import Folder

file1 = File("File1")
file2 = File("File2")
file3 = File("File3")

folder1 = Folder("Folder1")
folder2 = Folder("Folder2")

folder1.add(file1)
folder1.add(file2)

folder2.add(file3)

folder2.add(folder1)

folder2.show_details()