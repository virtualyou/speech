#!flask/bin/python
from app import app
from flask import Flask, jsonify, abort, make_response, request, send_file
import os


@app.route('/')
def home():
    return "My first production Flask app!"

@app.route('/speech/v1/assist/create/contact', methods=['GET'])
def contact_create_wav():
    file_path = os.path.join(os.getcwd(), './app/static/contact-create.wav')
    return send_file(file_path, mimetype='audio/wav')

@app.route('/speech/v1/assist/create/asset', methods=['GET'])
def asset_create_wav():
    file_path = os.path.join(os.getcwd(), './app/static/asset-create.wav')
    return send_file(file_path, mimetype='audio/wav')

@app.route('/speech/v1/assist/create/debt', methods=['GET'])
def debt_create_wav():
    file_path = os.path.join(os.getcwd(), './app/static/debt-create.wav')
    return send_file(file_path, mimetype='audio/wav')

@app.route('/speech/v1/assist/create/doc', methods=['GET'])
def doc_create_wav():
    file_path = os.path.join(os.getcwd(), './app/static/doc-create.wav')
    return send_file(file_path, mimetype='audio/wav')

@app.route('/speech/v1/assist/create/prescription', methods=['GET'])
def rx_create_wav():
    file_path = os.path.join(os.getcwd(), './app/static/rx-create.wav')
    return send_file(file_path, mimetype='audio/wav')

@app.route('/speech/v1/assist/create/task', methods=['GET'])
def task_create_wav():
    file_path = os.path.join(os.getcwd(), './app/static/task-create.wav')
    return send_file(file_path, mimetype='audio/wav')

