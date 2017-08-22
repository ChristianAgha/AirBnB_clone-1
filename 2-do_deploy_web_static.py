#!/usr/bin/python3
"""
Fabric script that distributes an archive
to  web servers, using the function do_deploy
"""
import os.path
from fabric.api import *
env.hosts = ['66.70.184.162', '142.44.164.120']


def do_deploy(archive_path):
    """
    distributes an archive to 2 web servers
    """
    if (os.path.isfile(archive_path) is False):
        return False

    try:
        archive = archive_path.split('/')[-1]
        uncomp_dir = "/data/web_static/releases/" + archive[:-4] + "/"
        tmp_path = "/tmp/" + archive
        put(archive_path, "/tmp/")
        run("sudo mkdir -p " + uncomp_dir)
        run("sudo tar -xzf " + tmp_path + " -C " + uncomp_dir)
        run("sudo rm -rf " + tmp_path)
        run("sudo mv " + uncomp_dir + "web_static/* " + uncomp_dir)
        run("sudo rm -rf " + uncomp_dir + "web_static")
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s " + uncomp_dir + " /data/web_static/current")
        return True
    except:
        return False
