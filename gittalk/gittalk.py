import os
import Tkinter

from ui import frames
from utils import get_git_root, write_hook, parse_message
from enable import HookInstaller

class GitTalk(object):
    def __init__(self, *args, **kwargs):
        self.git_root = get_git_root(os.getcwd())
        self.installer = HookInstaller(self.git_root)
        pass

    def enable(self):
        try:
            # git_root = get_git_root(os.getcwd())
            # # commit_msg_hook = os.path.join(git_root, '.git', 'hooks', 'commit-msg')
            # # write_hook(commit_msg_hook)
            # installer = HookInstaller(git_root)
            self.installer.addHook()
            print 'GitTalk enabled successfully!'
        except Exception as e:
            print 'GitTalk cannot be enabled. {}'.format(e.message)

    def disable(self):
        try:
            # git_root = get_git_root(os.getcwd())
            # installer = HookInstaller(git_root)
            self.installer.rmHook()
            print 'GitTalk disabled successfully!'
        except Exception as e:
            print 'GitTalk cannot be disabled. {}'.format(e.message)

    def trigger(self):
        # TODO: implement trigger
        # root = Tkinter.Tk()
        # frames.VideoRecordControlFrame(root).pack()
        # root.mainloop()
        print parse_message('ashdihasi $$method=record, location=commit, title=Explain funcA$$')
        # print 'TODO: trigger'
