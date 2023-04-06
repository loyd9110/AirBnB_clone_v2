#!/usr/bin/python3
""" A fabric script that distributes an archive to servers """

from fabric.api import run, env, put
import os.path
from fabric import Connection

def do_deploy(archive_path):

