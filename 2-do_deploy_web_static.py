#!/usr/bin/python3
""" A fabric script that distributes an archive to servers """

from fabric.api import run, env, put
import os.path

env.hosts = ['54.237.227.137','54.237.62.143']
env.key_filename = '~/.ssh/school'
env.user = 'ubuntu'

def do_deploy(archive_path):
""" The deploy function starts """ 
    if not os.path.isfile(archive_path):
        return False
    to_compress = archive_path.split("/")[-1]
    extension_none = to_compress.split(".")[0]

    try:
        the_path = "/data/web_static/releases/{}/".format(extension_none)
        symbolic_link = "/data/web_static/current"
        put(archive_path, "/tmp/")
        run("sudo tar -xvzf /tmp/{} -C {}".format(to_compress, the_path))
        run("sudo rm /tmp/{}".format(to_compress))
        run("sudo ln -sf {} {}".format(the_path, symbolic_link))
       return True
    except Exception as e:
       return False
