from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
from route import test

data = [###รอข้อมูลจาก database

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
@app.route('/')
def home():
    return jsonify(data)

@app.route('/api')
def api():
    return jsonify(test())

@app.route('/get_all')
def return_all():
    return jsonify(get_all())

@app.route('/get_name/<name>')
def get_name(name):
    return jsonify(get_anime())

@app.route('/name_anime')#name
def name_anime(names):
    return jsonify(name_anime())

@app.route('/type_anime/<type>')#type
def type_anime(types):
    return jsonify(type_anime())

@app.route('/link_anime/<type>')#link
def link_anime(link):
    return jsonify(link_anime())

if __name__ == '__main__':
    app.run(debug=True)
