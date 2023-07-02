from package_hasher import PackageHashMap
import random
import math

def get_random_character():
    characters = ["a", "b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","Y","Z","1","2","3","4","5","6","7","8","9","0"]
    index = math.floor(random.random()*len(characters)) - 1
    return characters[index]

def generate_random_string():
    length = math.floor(random.random() * 10)
    string = ""
    for index in range(0, length):
        string = string + get_random_character()

    return string

cell_number = 40

hasher = PackageHashMap(cell_number)
cells = []

for cell in range(0, cell_number):
    cells.append(0)

for eggs in range(0, 10**5):
    arguments = []
    for argument in range(0,6):
        arguments.append(generate_random_string())

    value = hasher.package_hash_function(arguments[0],arguments[1],arguments[2],arguments[3],arguments[4],arguments[5])
    cells[value] = cells[value] + 1

for cell in cells:
    print(cell/10**5)
