#!/usr/bin/python3
""" Fabric script to create an archive file """
from fabric.api import local
from datetime import datetime


def do_pack():
    """ Compression of a file and return path """
    """ Current timestamp and file path """
    time_created = datetime.now().strftime("%Y%m%d%H%M%S")
    file_path = "versions/web_static_{}.tgz".format(time_created)

    try:
        local("mkdir -p versions")
        local("tar -cvzf {} web_static".format(file_path))
        return file_path
    except Exception as e:
        return None
