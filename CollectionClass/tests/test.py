import sys
sys.path.append("/mnt/c/Users/z004swjt/Documents/CodeBase/CollectionClass/src/")

from CollectionClass import Collection


# test untils
def setDummyData(testObj):
    '''
    Add George Washington, Donald Trump and Joe Biden to the collection in that order
    '''
    testObj.addName("George", "Washington")
    testObj.addName("Donald", "Trump")
    testObj.addName("Joe", "Biden")


def testGetName():

    presidents = Collection()

    # Adding test data for add name
    presidents.addName("Joe", "Biden")

    # Pass: Getting added test data
    sname = presidents.getName("Joe")
    assert sname == "Biden"


def testGetNameNotThere():
    presidents = Collection()
    # Fail: Getting bad president
    sname = presidents.getName("bob")
    assert sname == None


def testGetIndex():

    presidents = Collection()
    setDummyData(presidents)

    # Pass: Isolate and get data
    passData = presidents.getNameByIndex(1)
    assert passData == "George Washington"
    passData = presidents.getNameByIndex(2)
    assert passData == "Donald Trump"
    passData = presidents.getNameByIndex(3)
    assert passData == "Joe Biden"


def testGetIndexOutOfBounds():

    presidents = Collection()
    setDummyData(presidents)

    # Fail: Getting Out of bound Index
    failData = presidents.getNameByIndex(10)
    assert failData == None
    failData = presidents.getNameByIndex(-10)
    assert failData == None


def testDelPersonByIndex():

    presidents = Collection()

    # Add data for testing
    presidents.addName("Joe", "Biden")

    # Pass: Data inserted correctly and then Removed
    name = presidents.getNameByIndex(1)
    assert name == "Joe Biden"

    presidents.delNameByIndex(1)

    # Test its not in the array
    name = presidents.getNameByIndex(1)
    assert name == None
    # Test its not in the dict
    assert presidents.getName("Joe") == None


def testDelPersonByIndexOutOfBounds():

    presidents = Collection()

    # Fail: Attempt to delete from outside list
    failData = presidents.delNameByIndex(-1)
    assert failData == None

    # Fail: Attempt to delete from outside list
    failData = presidents.delNameByIndex(10)
    assert failData == None


def testDelbyName():

    presidents = Collection()

    presidents.addName("Bill", "Clinton")  # Add data to collection.

    # Test data made it into collection.
    name = presidents.getNameByIndex(1)
    assert name == "Bill Clinton"

    presidents.delByName("Bill")    # Delete data.

    # Test data was succesfully deleted.
    name = presidents.getNameByIndex(1)
    assert name == None
    assert presidents.getName("Bill") == None


def testDelFromCollectionByIndex():

    presidents = Collection()
    setDummyData(presidents)

    name = presidents.getNameByIndex(2)
    assert name == "Donald Trump"

    presidents.delNameByIndex(2)

    # Check it was deleted from dict
    assert presidents.getName("Donald") == None

    name = presidents.getNameByIndex(2)
    assert name == "Joe Biden"


def testDelFromCollectionByName():

    presidents = Collection()
    setDummyData(presidents)

    # Test data is at index 1
    name = presidents.getNameByIndex(2)
    assert name == "Donald Trump"

    presidents.delByName("Donald")

    # Check it was deleted from dict
    assert presidents.getName("Donald") == None

    # Check it was deleted from list (The succeeding name takes its index position)
    name = presidents.getNameByIndex(2)
    assert name == "Joe Biden"


def testDelNameNotThere():
    
    presidents = Collection()
    setDummyData(presidents)

    presidents.delByName("Bob")
    assert presidents.getName("Bob") == None

    # Check data remains unchanged.
    name = presidents.getNameByIndex(1)
    assert name == "George Washington"
    name = presidents.getNameByIndex(2)
    assert name == "Donald Trump"
    name = presidents.getNameByIndex(3)
    assert name == "Joe Biden"
