import requests

url = "http://localhost:5000/president"

def testGetResponse():
    response = requests.get(url)
    assert response.status_code ==200


def testPostName():
    '''
    Runs a post command to add data to the client and asserts the success message appears
    '''
    # Delete any data that may exist to test on a clean slate.

    tearDown()
    data = {"fname": "George", "sname": "Washington"}
    response = requests.post(url, json = data)
    response_body = response.json()

    assert response.status_code ==200
    assert response.headers["Content-Type"] == "application/json"
    assert response_body["message"] == "Data has been added"
    tearDown()


def testPostNameFail():
    '''
    Should return an error message because not enough data is provided for the post object.
    '''
    # Delete any data that may exist to test on a clean slate.
    tearDown()
    data = {"fname": "Theodore"}
    response = requests.post(url, json = data)
    response_body = response.json()

    assert response.status_code == 400
    assert response.headers["Content-Type"] == "application/json"
    assert response_body["message"] == "Failed expected data not set"
    tearDown()


def testGetByName():
    '''
    Tests the get function to retrieve the pair value of fname key parameter
    '''
    addNameForTest()
    response = requests.get(url+"?fname=George")
    response_body = response.json()

    assert response.status_code ==200
    assert response_body["sname"] == "Washington"
    tearDown()


def testGetByNameFail(): 
    '''
    Attempts to get a name that doesnt exist in the collection. Assets error message is returned
    '''
    addNameForTest()
    response = requests.get(url+"?fname=Joe")
    response_body = response.json()

    assert response.status_code == 404
    assert response_body["message"] == "Failed data not found. Name not found"
    tearDown()


def testGetByIndex():
    '''
    Tests the get function to retrieve the key/value pair data using array index position.
    '''
    addNameForTest()
    response = requests.get(url+"?index=0")
    response_body = response.json()

    assert response.status_code ==200
    assert response_body["fullName"] == "George Washington"
    tearDown()


def testGetByIndexFail():
    '''
    Attempts to retreive data at an index position that doesnt exist in the array. Asserts an error message is returned.
    '''
    addNameForTest()
    response = requests.get(url+"?index=2")
    response_body = response.json()

    assert response.status_code == 404
    assert response_body["message"] == "Failed data not found. Index out of bounds"
    tearDown()


def testDeleteByName():
    '''
    Tests the delete by name function using a first name parameter to delte ists data from the dict and array.
    '''
    addNameForTest()
    response = requests.delete(url+"?fname=George")
    response_body = response.json()

    assert response.status_code ==200
    assert response_body["message"] == "Data has been deleted"
    tearDown()


def testDeleteByNameFail():
    '''
    Attempts to delete a name that doesnt exist in the collection. Asserts an error message is returned
    '''
    addNameForTest()
    response = requests.delete(url+"?fname=Joe")
    response_body = response.json()

    assert response.status_code == 404
    assert response_body["message"] == "Name doesnt exist"
    tearDown()

def testDeleteByIndex():
    '''
    Tests the delete by index function using a values index position to read its data from the array 
    and use it to delete it from the dict and array
    '''
    addNameForTest()
    response = requests.delete(url+"?index=0")
    response_body = response.json()

    assert response.status_code ==200
    assert response_body["message"] == "Data has been deleted"
    tearDown()


def testDeleteByIndexFail():
    '''
    Attempts to delete an index position that doesnt exist. Asserts an error message is returned.
    '''
    addNameForTest()
    response = requests.delete(url+"?index=10")
    response_body = response.json()

    assert response.status_code == 404
    assert response_body["message"] == 'Failed data not found. Index out of bounds'
    tearDown()


def testAddNameMultipleTimes():
    '''
    Adding the same name multiple times should not result in duplication in the array.
    '''
    data = {"fname": "George", "sname": "Washington"}
    response = requests.post(url, json = data)
    data1 = {"fname": "George", "sname": "Washington"}
    response = requests.post(url, json = data1)
    data2 = {"fname": "George", "sname": "Washington"}
    response = requests.post(url, json = data2)

    # Data at index 0
    response = requests.get(url+"?index=1")
    response_body = response.json()
    assert response.status_code == 200
    assert response_body["fullName"] == "George Washington"

    response = requests.get(url+"?index=2")
    response_body = response.json()
    assert response.status_code == 404
    assert response_body["message"] == "Failed data not found. Index out of bounds"

    response = requests.get(url+"?index=3")
    response_body = response.json()
    assert response.status_code == 404
    assert response_body["message"] == "Failed data not found. Index out of bounds"
    tearDown()

    
def testAddListOfObjects():
    '''
    Adds a list containing additional data that is used to add to the collection. Adds the list, asserts the data was added correctly
    then asserts that the data made it into the array successfully by comparing it to its corresponding index position.
    '''
    tearDown()
    # Data being inserted.
    data = {"presidents": [
        {
            "fname":"Barack",
            "sname":"Obama"
        },
        {
            "fname":"John",
            "sname":"Adams"
        },
        {
            "fname":"Theodore",
            "sname":"Roosevelt"
        }]
    }
    response = requests.post(url, json = data)
    response_body = response.json()
    assert response.status_code ==200
    assert response.headers["Content-Type"] == "application/json"
    assert response_body["message"] == "Data has been added"

    response = requests.get(url+"?index=1")
    response_body = response.json()
    assert response.status_code ==200
    assert response_body["fullName"] == "Barack Obama"

    response = requests.get(url+"?index=2")
    response_body = response.json()
    assert response.status_code ==200
    assert response_body["fullName"] == "John Adams"

    response = requests.get(url+"?index=3")
    response_body = response.json()
    assert response.status_code ==200
    assert response_body["fullName"] == "Theodore Roosevelt"
    tearDown()


def addNameForTest():
    '''
    Function to add a name for use in test cases.
    '''
    data = {"fname": "George", "sname": "Washington"}
    response = requests.post(url, json = data)


def tearDown():
    '''
    function to delete all data that exists in the collection
    '''
    response = requests.delete(url + "/deleteAll")
    

    
