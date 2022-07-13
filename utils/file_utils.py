import os
import subprocess
import sys
import time


def rsync_process(from_path, to_path, ssh_key_path=None, options=None):
    """Rsync files in a given directory. Relies on SSH_KEY_PATH from config.

    Args:
        fromPath (str): Path to directory to sync from
        toPath (str): Path to directory to sync to
        options (str, optional): Rsync additional option flags, e.g., "--exclude '*.zip'". Defaults to False.

    Returns:
        str: Result stdout
    """
    cmd = ["/usr/bin/rsync", "-zarvhe", from_path, to_path]
    if ssh_key_path:
        cmd.insert(2, f'"ssh -i {ssh_key_path}"')
    if options:
        cmd.insert(-2, options)
    result = subprocess.Popen(
        cmd,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        shell=True,
    ).communicate()

    if result[1]:  # error
        raise Exception("RSYNC ERROR: " + str(result[1].decode("utf-8")))
    else:
        return result[0].decode("utf-8")


def file_cleanup(_dir, _days):
    """Remove files from a directory that are of a certain age.

    Args:
        _dir (str): Path to directory
        _days (int): Number of days beyond which old files should be deleted
    """
    # Remove files from a directory that are of a certain age.
    now = time.time()
    old = now - int(_days) * 24 * 60 * 60
    # print(old)
    for f in os.listdir(_dir):
        path = os.path.join(_dir, f)
        if os.path.isfile(path):
            stat = os.stat(path)
            # print("")
            # print(stat.st_mtime)
            if stat.st_mtime < old:
                print("removing: ", path)
                os.remove(path)


def find_config(name="config.ini"):
    """Get the abs path to config.ini file, based on sys.path.

    Args:
        name (str, optional): config file name. Defaults to "config.ini".

    Returns:
        str: path to config file
    """
    for dirname in sys.path:
        for root, dirs, files in os.walk(dirname):
            if name in files:
                return os.path.join(root, name)
