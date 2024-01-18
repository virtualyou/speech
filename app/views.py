#
# VirtualYou Project
# Copyright 2023 David L Whitehurst
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# views.py - API methods with Path Decorator
#

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

@app.route('/speech/v1/assist/create/need', methods=['GET'])
def need_create_wav():
    file_path = os.path.join(os.getcwd(), './app/static/need-create.wav')
    return send_file(file_path, mimetype='audio/wav')
