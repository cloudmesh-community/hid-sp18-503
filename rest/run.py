import platform
import json
import shutil
import socket
import getpass
import os
from eve import Eve
from psutil import virtual_memory
from flask import Response

settings = {
    'MONGO_HOST': 'localhost',
    'MONGO_PORT': 27017,
    'DOMAIN': {}
    }

app = Eve(settings = settings)

def get_response(data):
    response = Response()
    response.headers['status'] = 200
    response.headers['Content-Type'] = "application/json ; charset=utf-8"
    response.data = json.dumps(data)
    return response

@app.route('/processor')
def processor():
    proc =  platform.processor()
    arch = platform.architecture()[0]
    sys = platform.system()
    data = {
        'proc': proc,
        'sys': sys,
        'arch': arch
    }
    response = get_response(data)
    return response


@app.route('/ram')
def ram():
    mem = virtual_memory()
    data = {
        'total': mem.total,
        'available': mem.available,
        'used': mem.used,
        'free':  mem.free,
        'cached': mem.cached,
        'shared': mem.shared,
    }
    
    response = get_response(data)
    return response

@app.route('/disk')
def disk():
    hdd = shutil.disk_usage("/home/arnav")
    data = {
        'total': hdd[0],
        'used': hdd[1],
        'free': hdd[2],
    }
    response = get_response(data)
    return response

@app.route('/user')
def user():
    username = getpass.getuser()
    hostname = socket.gethostname()
    data = {
        'username': username,
        'hostname': hostname,
    }
    response = get_response(data)
    return response

@app.route('/files')
def files():
    data = {
        'files': os.listdir('.')
    }
    response = get_response(data)
    return response

if __name__ == "__main__":
    app.run()
