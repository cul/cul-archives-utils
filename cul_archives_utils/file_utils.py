"""Perform actions on files."""


import subprocess
from time import time


def rsync_process(from_path, to_path, ssh_key_path=None, options=None):
    """Rsync files in a given directory.

    Args:
        from_path (str): Path to directory to sync from
        to_path (str): Path to directory to sync to
        ssh_key_path (str): Path to ssh config
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


def remove_old_files(directory, days):
    """Remove files from a directory that are of a certain age.

    Args:
        directory (pathlib.Path): Path to directory
        days (int): Number of days beyond which old files should be deleted

    Returns:
        list: removed files
    """
    now = time()
    old = now - int(days) * 24 * 60 * 60
    removed_files = []
    files_to_remove = [
        x for x in directory.iterdir() if x.is_file() and x.stat().st_mtime < old
    ]
    for f in files_to_remove:
        f.unlink()
        removed_files.append(f)
    return removed_files
