import os
import Tkinter

from ui import frames
from utils import get_git_root, write_hook

class GitTalk(object):
    def __init__(self, *args, **kwargs):
        pass

    def enable(self):
        try:
            git_root = get_git_root(os.getcwd())
            commit_msg_hook = os.path.join(git_root, '.git', 'hooks', 'commit-msg')
            write_hook(commit_msg_hook)
            print 'GitTalk enabled successfully!'
        except Exception as e:
            print 'GitTalk cannot be enabled. {}'.format(e.message)

    def disable(self):
        # TODO: implement disable
        print 'TODO: disable'

    def trigger(self):
        # TODO: implement trigger
        root = Tkinter.Tk()
        frames.VideoRecordControlFrame(root).pack()
        root.mainloop()
        print 'TODO: trigger'
