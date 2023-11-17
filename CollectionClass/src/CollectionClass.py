class Collection():
    '''
    A class that creates a collection of people. Contains a dictionary of first name keys and second name values
    contains a list/array that keeps track of the first names in the order they are added and used to call the second name
    values from the dictionary.
    '''

    # Initilize class.
    def __init__(self):
        self.__people = {}
        self.__peopleIndex = []


    # Add name to collection.
    def addName(self, fname, sname):
        '''
        Adds a name to the collection dict and array.
        '''
        # Check it doesn't already exist, otherwise there's duplicates in the array.
        if fname not in self.__people.keys():
            self.__people[fname] = sname
            self.__peopleIndex.append(fname)

    # Given first name as key, search dictionary for second name value.
    def getName(self, fname):
        '''
        Given a first name as a key, returns the second name value stores in the dict.
        '''
        return self.__people.get(fname)


    # Given index position, return item at that position.
    def getNameByIndex(self, num):
        '''
        Given an integer as an index position, returns the first name at that position of the array and the coressponding
        sname value in the dict.
        '''
        # Check argument is valid.
        if num < 0:
            return None
        if num > len(self.__peopleIndex):
            return None

        # Collect first name from array.
        fname = self.__peopleIndex[num-1]
        # Using firstname as a key, collect second name from the dict.
        sname = self.__people[fname]
        # Return whole name
        fullname = fname + " " + sname
        return fullname


    def delNameByIndex(self, num):
        '''
        Given an integer as an index position, reads the value in the array and uses it to delete the key/value pair of dict 
        before deleting itself from the array.
        '''
        # Check input is valid, else return None
        if num > len(self.__peopleIndex):
            return None
        elif num < 0:
            return None

        # Using input index position, collect the name from that position of the array.
        name = self.__peopleIndex[num-1]

        del self.__people[name]  # Use the name/key to delete itself from dictionary.
        del self.__peopleIndex[num-1]  # Delete value at the given index from list.


    def delByName(self, fname):
        '''
        Given a name as an argument, finds the name in the array and uses its index position to to call delNameByIndex function.
        '''
        # Check the name you want to delete exists, else return None
        if self.__people.get(fname) == None:
            return None

        # Collect the index positon of the name from the array.
        pos = self.__peopleIndex.index(fname)
        # Use the index position to call the delete by index function above. Deletes it from the array and dict.
        # Adding 1 here because this is the actual index position and the delByIndex funtion will minus the 1.
        self.delNameByIndex(pos+1) 


    def listOfNames(self):
        '''
        Returns a list containing all names currently in the collection
        '''
        listOfNames = []
        for k, v in self.__people.items():
            listOfNames.append(k + " " + v)
        return listOfNames
  

    def deleteAll(self):
        '''
        Deletes everything from the collection dict and array
        '''
        # While the array is still populated keep deleting the data at index position 0.
        while 1 <= len(self.__peopleIndex):
            self.delNameByIndex(0)


