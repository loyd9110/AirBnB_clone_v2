#!/usr/bin/python3
""" Fabric script to create an archive file """
from fabric.api import *
from datetime import datetime

def do_pack():
    """ Compression of a file and return path """
    
    """ Current timestamp and file path """
    time_created = datetime.now().strftime("%Y%m%d%H%M%S")
    file_path = f"versions/web_static_{time_created}.tgz"

    try:
        local("mkdir -p versions")
        local(f"tar -cvzf {file_path} web_static/")
        return f"{file_path}"
    except Exception as e:
        return None
