import os

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

def write_hook(git_root):
    print "TODO: write git hook here"
    # TODO: remember to enable chmod +x on the file
    # TODO: make the function respect other hooks in the same file
    # TODO: make the function idempotent
    # TODO: don't forget to write python from PATH