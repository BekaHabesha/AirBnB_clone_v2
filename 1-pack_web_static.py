#!/usr/bin/python3
"""
Fabric script to generates a .tgz archive
from the contents of the web_static folder
execute: fab -f 1-pack_web_static.py do_pack.
"""

from fabric.api import local
import time


def do_pack():
    """
    Making and Generate an tgz archive
    from web_static folder
    """

    try:
        local("mkdir -p versions")
        local("tar -cvzf versions/web_static_{}.tgz web_static/".
              format(time.strftime("%Y%m%d%H%M%S")))
        return ("versions/web_static_{}.tgz".format(time.
                                                    strftime("%Y%m%d%H%M%S")))
    except:
        return None
