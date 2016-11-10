import os
import Tkinter

from ui import frames
from src.utils import get_git_root, write_hook, parse_message
from src.enable import HookInstaller

class GitTalk(object):
    def __init__(self, *args, **kwargs):
        self.git_root = get_git_root(os.getcwd())
        self.installer = HookInstaller(self.git_root)

    def enable(self):
        try:
            self.installer.addHook()
            print ('GitTalk enabled successfully!')
        except Exception as e:
            print ('GitTalk cannot be enabled.')

    def disable(self):
        try:
            self.installer.rmHook()
            print ('GitTalk disabled successfully!')
        except Exception as e:
            print ('GitTalk cannot be disabled.')

    def trigger(self):
        # TODO: implement trigger
        # root = Tkinter.Tk()
        # frames.VideoRecordControlFrame(root).pack()
        # root.mainloop()
        print (parse_message('ashdihasi $$method=record, location=commit, title=Explain funcA$$'))
        # print 'TODO: trigger'
