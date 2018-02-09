from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_DBNAME'] = 'rest_db'
mongo = PyMongo(app, config_prefix='MONGO')

def create_dir(dirName):
    directory = mongo.db.dirs.find({'dir_name': dirName})
    print(directory)
    if direcory:
        return directory
    else:
        directory = {"dir_name": dirName}
        mongo.db.dirs.insert(directory)   
    return directory

def dirs_get():
    print("trying to find all")
    dirs = mongo.db.dirs.find()
    return dirs

def get_dir_by_id(dirName):
    print("get by id ", dirNams)
    directory = mongo.db.dirs.find_one_or_404({'dir_name': dirName})
    return directory
