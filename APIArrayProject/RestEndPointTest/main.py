#!/usr/bin/env python
# encoding: utf-8
import json
from flask import Flask, jsonify, request

mylist = {}


app = Flask(__name__)

# # Exposed to user
# @app.route('/')
# def readName():



@app.route('/president', methods=['POST'])
def addName():

    fname = request.json['fname']
    sname = request.json['sname']

    mylist[fname] = sname

    return jsonify({'message': 'Data has been added'})


@app.route('/president', methods=['GET'])
def getName():

    fname = request.args.get('fname')
    sname = mylist[fname]

    
    return jsonify({"sname":sname})



@app.route('/president', methods=['DELETE'])
def delName():

    fname = request.json['fname']
    sname = mylist[fname]

    del mylist[fname]

    return jsonify({'message': 'Data has been deleted'})
    




@app.route('/hello')
def readName():
    return "Hello World"

app.run()