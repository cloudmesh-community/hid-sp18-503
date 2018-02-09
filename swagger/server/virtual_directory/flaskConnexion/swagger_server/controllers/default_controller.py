import connexion
import six

from swagger_server.models.dir import Dir  # noqa: E501
java.io.File  # noqa: E501
from swagger_server import util


def create_dir(dir_name):  # noqa: E501
    """create_dir

    create/update a directory with the directory name dir_name # noqa: E501

    :param dir_name: name of the directory to be created
    :type dir_name: str

    :rtype: Dir
    """
    return 'do some magic!'


def dirs_get():  # noqa: E501
    """dirs_get

    Returns a list of all directories # noqa: E501


    :rtype: List[Dir]
    """
    return 'do some magic!'


def get_dir_by_id(dir_name):  # noqa: E501
    """get_dir_by_id

    Returns a list of files in the directory dir_name # noqa: E501

    :param dir_name: name of the directory to fetch
    :type dir_name: str

    :rtype: List[File]
    """
    return 'do some magic!'
