from eve import Eve
import platform
from psutil import virtual_memory

settings = {
    'MONGO_HOST': 'localhost',
    'MONGO_PORT': 27017,
    'DOMAIN': {}
    }

app = Eve(settings = settings)

@app.route('/processor')
def processor():
    proc =  platform.processor()
    arch = platform.architecture()[0]
    sys = platform.system()
    response = {
        'proc': proc,
        'sys': sys,
        'arch': arch
    }
    return str(response)


@app.route('/ram')
def ram():
    mem = virtual_memory()
    response = {
        'total': mem.total,
        'available': mem.available,
        'used': mem.used,
        'free':  mem.free,
        'cached': mem.cached,
        'shared': mem.shared,
    }
    return str(response)

if __name__ == "__main__":
    app.run()
