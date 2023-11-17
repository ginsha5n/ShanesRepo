import json
from flask import Flask, jsonify, request
from flask import *
from CollectionClass import Collection
from distutils.log import debug
from fileinput import filename


# Initilize Collection class
presidents = Collection()
# Flask class
app = Flask(__name__)

# POST functions
@app.route('/president', methods=['POST'])
def addName():
    '''
    Adds a name or list of names to the collection.
    '''
    data = request.get_json()
    fname = data.get('fname')
    sname = data.get('sname')

    # If first name and second name variables dont exist, look for a list.
    if fname == None or sname == None:
        presidentList = data.get('presidents')
        # If list data isnt given, produce error message.
        if presidentList == None:
            return jsonify({'message': 'Failed expected data not set'}), 400 # 400, Bad request

        return addList(presidentList)
    
    # Add data into Collection using class functions
    presidents.addName(fname, sname)
    return jsonify({'message': 'Data has been added'})


def addList(presidentList):
    '''
    Function to iterate through list of JSON objects and add variables to collection class object.
    '''   
    for item in presidentList:
        fname = item.get('fname')
        sname = item.get('sname')
        presidents.addName(fname, sname)

    return jsonify({'message': 'Data has been added'})


# Get functions
@app.route('/president', methods=['GET'])
def getByName():
    '''
    Takes a first name argument as a key and searches the collection for its value.
    Or, takes an index position and returns the key and value pair at that position of the array
    '''
    fname = request.args.get('fname')
    index=request.args.get("index")

    # If name or index variables arn't given, print a list of all current values in the collection.
    if fname == None and index == None:
        return printAll()

    # If name value is not given use get by index function.
    elif fname == None:
        indexPos = presidents.getNameByIndex(int(index))

        # If index out of bounds, show error message.
        if indexPos == None:
            return jsonify({'message': 'Failed data not found. Index out of bounds'}), 404
        
        else:
            return getByIndex(index)

    # If index arg not given, use get by name function.
    elif index == None :
        sname = presidents.getName(fname)
        if sname == None:
            return jsonify({'message': 'Failed data not found. Name not found'}), 404

        return jsonify({"sname": sname})


def getByIndex(index):
    '''
    Take an index position argument and returns the name at that position of the array
    '''
    fullName=presidents.getNameByIndex(int(index))
    return jsonify({"fullName": fullName})


def printAll():
    '''
    prints all names in the collection 
    '''
    return jsonify({"presidents":presidents.listOfNames()})


@app.route('/president', methods=['DELETE'])
def delByName():
    '''
    Takes a name as a key argument and deletes that key/pair value from the collection
    '''
    fname = request.args.get('fname')
    index = request.args.get("index")

    # If name variable doesnt exist use delete by index function.
    if fname == None:
        indexPos = presidents.getNameByIndex(int(index))

        # If an incorrect index postion is passed in, show error message.
        if indexPos == None:
            return jsonify({'message': 'Failed data not found. Index out of bounds'}), 404
        return delByIndex(index)

    # If an index isn't given, use delete by name function.
    elif index == None:

        # If name doesn't exist in the collection, show an error.
        if presidents.getName(fname) == None:
            return jsonify({'message': 'Name doesnt exist'}), 404
    
        presidents.delByName(fname)
        return jsonify({'message': 'Data has been deleted'})


def delByIndex(index):
    '''
    Given an index position as an argument, delete the value at that position of the array from the collection
    '''
    presidents.delNameByIndex(int(index))
    return jsonify({'message': 'Data has been deleted'})


# Delete all names in Collection
@app.route('/president/deleteAll', methods=['DELETE'])
def deleteAll():
    '''
    Delete all values from the collection.
    '''
    presidents.deleteAll()
    return jsonify({'message': 'Everything was deleted'})


@app.route('/president/Add', methods=['GET'])
def addAll():
    '''
    Using the file presidents.json reads in data from all past presidents of the U.S. to populate the app.
    The data is sorted by the order 
    '''
    f = open("presidents.json")
    data = json.load(f)
    presidentList = data.get("presidents")

    for i in range(1,47):
        for item in presidentList:

            fname = item.get('fname')
            sname = item.get('sname')
            order = item.get("order")
            
            if int(order) == i:
                presidents.addName(fname,sname)

        i += 1

    return jsonify({'message': 'Data has been added'})


@app.route('/president/upload')
def main():
    return render_template("index.html")


@app.route('/president/success', methods=['POST'])
def upload():
    '''
    Upload the president.json file from the client side
    '''
    # Request file and save in src dir
    if request.method == 'POST':
        f = request.files['file']
        f.save(f.filename)  

        if f.filename == "presidents.json":
            addAll()
            return render_template("Acknowledgement.html", name = "presidents.json") 
                
        return render_template("Acknowledgement.html", name = f.filename)  


app.run()

