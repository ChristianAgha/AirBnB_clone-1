#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive
from the contents of the web_static folder
"""
from fabric.api import *
from time import strftime


def do_pack():
    """Makes .tgz archive from web_static folder"""
    now = strftime("%Y%m%d%H%M%S")
    try:
        local("mkdir -p versions")
        local("tar -cvzf versions/web_static_{}.tgz web_static".format(now))
        return("versions/web_static_{}.tgz".format(now))
    except:
        return(None)
