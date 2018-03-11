import connexion
import six

from swagger_server.models.dir import Dir  # noqa: E501
from swagger_server import util
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.rest_db

def create_dir(dir_name, body=None):  # noqa: E501
    """create_dir

    create/update a directory with the directory name dir_name # noqa: E501

    :param dir_name: name of the directory to be created
    :type dir_name: str

    :rtype: Dir
    """
    if connexion.request.is_json:
        body = Dir.from_dict(connexion.request.get_json())  # noqa: E501

    print(body)
    print(body.to_dict())
    
    #db.dirs.insert_one({dir_name = dir_name,
    #                    parent_directory = parent_dir,
    #                    files = files})
    #new_dir = Dir(name = dir_name,
    #              parent_directory = parent_dir,
    #              files = files)
    
    return body
                                                


def dirs_get():  # noqa: E501
    """dirs_get

    Returns a list of all directories # noqa: E501


    :rtype: List[Dir]
    """
    dirs = db.dirs.find()
    arr = []
    for d in dirs:
        name = d["dir_name"]
        parent_dir =  d["parent_dir"] if 'parent_dir' in d else None
        files = d['files'] if 'files' in d else []
        obj = Dir(name = name, parent_directory = parent_dir, files = files)
        arr.append(obj)
    return arr


def get_dir_by_id(dir_name):  # noqa: E501
    """get_dir_by_id

    Returns a list of files in the directory dir_name # noqa: E501

    :param dir_name: name of the directory to fetch
    :type dir_name: str

    :rtype: List[str]
    """
    # get request
    directory = db.dirs.find_one({'dir_name': dir_name})
    if directory:
        name = directory['dir_name']
        parent_dir = directory['parent_dir'] if 'parent_dir' in directory else None
        files = directory['files'] if 'files' in directory else []
        obj = Dir(name = name, parent_directory = parent_dir, files = files)
        return obj
    else:
        return "Object Not Found"
