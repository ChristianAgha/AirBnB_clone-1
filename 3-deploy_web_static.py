#!/usr/bin/python3
"""
creates and distributes an archive to my web servers
"""
import os.path
from fabric.api import *
from time import strftime
env.hosts = ['66.70.184.162', '142.44.164.120']


def do_pack():
    """Makes .tgz archive from web_static folder"""
    now = strftime("%Y%m%d%H%M%S")
    try:
        local("mkdir -p versions")
        local("tar -cvzf versions/web_static_{}.tgz web_static".format(now))
        return("versions/web_static_{}.tgz web_static".format(now))
    except:
        return(None)


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


def deploy():
    """
     deploys func definition
    """
    try:
        arch_address = do_pack()
        status = do_deploy(arch_address)
        return status
    except:
        return False
