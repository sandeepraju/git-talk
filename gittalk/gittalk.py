import os

from utils import get_git_root
from hook import Hook
from gui import GUI

class GitTalk(object):
    def __init__(self, *args, **kwargs):
        self.git_root = get_git_root(os.getcwd())
        self.hook = Hook(self.git_root)
        pass

    def enable(self):
        try:
            self.hook.create()
            print 'GitTalk enabled successfully!'
        except Exception as e:
            print 'GitTalk cannot be enabled. {}'.format(e.message)

    def disable(self):
        try:
            self.hook.destroy()
            print 'GitTalk disabled successfully!'
        except Exception as e:
            print 'GitTalk cannot be disabled. {}'.format(e.message)

    def trigger(self):
        commit_file_path = os.environ.get('GITTALK_COMMIT_MSG', None)
        commit_message = ''
        if commit_file_path:
            with open(commit_file_path, 'r+') as f:
                commit_message = f.read()

        window = GUI(commit_message=commit_message)