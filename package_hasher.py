#This functino takes in information from a package, an input key, and returns it's hash.
#Parameters: all value assosiated with the package as per the requirements of the project.
#Returns: Either None in the case of invalid inputs or the output of the hash function.
#!Warning! Changing the variable names changes the hash function itself. The hash function takes into account the name of it's inputs to increase extendability.
class PackageHashMap:
    def __init__(self, number_of_cells : int): 
        self.number_of_cells = number_of_cells
        self.table_cells = []

        for value in range(0, number_of_cells-1):
            self.table_cells.append(None)

    def package_hash_function(self, id :str, address :str, deadline : str, zip_code :str, weight : str, status : str):
        keys = [] #List of the names of the function parameters:
        for key in locals().keys(): #Put all variable names into a list
            keys.append(key)

        super_string = "" #The string consisting of all the argument values concatinated together.

        keys.remove("keys") #keys is a local variable not passed as a paramter
        keys.remove("self") #keys is a local variable not passed as a paramter
        keys.sort() #Sorted by alphanumeric order
        for key in keys: 
            if(type(locals()[key]) != str): #Only strings are allowed to be passed
                print("package_hash_function only takes string arguments.", key, "Is not of type str it is of type", type(key))
                return None
            super_string = super_string + locals()[key] #Append value to super_string
        sum_of_characters = 0
        product = 0
        for character in super_string:
            value = ord(character)
            sum_of_characters = sum_of_characters + value
            product = product*value % 100

        sum_of_both = sum_of_characters + product
        return sum_of_characters % self.number_of_cells
