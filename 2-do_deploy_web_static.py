#!/usr/bin/python3
"""Deploying the webstatic to the server
"""
from fabric.api import env, put, run
import os

env.hosts = ["54.237.227.137", "54.237.62.143"]


def do_deploy(archive_path):

    if not os.path.isfile(archive_path):
        return False

    to_compress = archive_path.split("/")[-1]
    extension_none = to_compress.split(".")[0]

    The_path = "/data/web_static/releases/{}".format(extension_none)
    try:
        put(archive_path, "/tmp/")
        run("sudo mkdir -p {}".format(The_path))
        run("sudo tar -xvzf /tmp/{} -C {}".format(to_compress, The_path))
        run("sudo rm /tmp/{}".format(to_compress))
        run("sudo ln -sf {} /data/web_static/current".format(The_path))
    except Exception as e:
        return False
    return True
