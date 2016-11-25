import os
import sys
import errno
import subprocess as sp

# Define some constants
AUDIO, VIDEO, SCREEN = 0, 1, 2
LINUX, MAC, WINDOWS = 0, 1, 2

# src: http://stackoverflow.com/a/377028/1044366
def which(program):
    def is_exe(fpath):
        return os.path.isfile(fpath) and os.access(fpath, os.X_OK)

    fpath, fname = os.path.split(program)
    if fpath:
        if is_exe(program):
            return program
    else:
        for path in os.environ["PATH"].split(os.pathsep):
            path = path.strip('"')
            exe_file = os.path.join(path, program)
            if is_exe(exe_file):
                return exe_file

    return None

def detectPlatform():
    if sys.platform.startswith('linux'):
        return LINUX
    elif sys.platform.startswith('win') or sys.platform.startswith('cyg'):
        return WINDOWS
    elif sys.platform.startswith('darwin'):
        return MAC
    else:
        return None

def get_git_root(cwd):
    git_root = os.path.abspath(cwd)
    # TODO: pep8
    # TODO: while generating the commit-msg hook,
    #       don't forget to write the python path
    # FIXME: doesn't work on windows
    while git_root != '/':
        if os.path.isdir(os.path.join(git_root, '.git')):
            # this is the git's root
            return git_root

        git_root = os.path.dirname(git_root)

    # at this point, the root (/) is the git root or there is not git root
    if os.path.isdir(os.path.join(git_root, '.git')):
        return git_root

    raise Exception('This is not a Git repository!')

def make_sure_path_exists(path):
    try:
        os.makedirs(path)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise

