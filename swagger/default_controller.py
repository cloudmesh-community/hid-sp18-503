from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['ONGO_DBNAME'] = 'rest_db'
mongo = PyMongo(app)

def create_dir(dirName):
    directory = mongo.db.dirs.find({'dir_name': dirName})
    if direcory:
        return directory
    else:
        directory = {"dir_name": dirName}
        mongo.db.dirs.insert(directory)   
    return directory

def dirs_get():
    dirs = mongo.db.dirs.find()
    return dirs

def get_dir_by_id(dirName):
    directory = mongo.db.dirs.find_one_or_404({'dir_name': dirName})
    return directory
