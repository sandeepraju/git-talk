import os
import Tkinter

# from ui import frames
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
            # git_root = get_git_root(os.getcwd())
            # # commit_msg_hook = os.path.join(git_root, '.git', 'hooks', 'commit-msg')
            # # write_hook(commit_msg_hook)
            # installer = HookInstaller(git_root)
            self.hook.create()
            print 'GitTalk enabled successfully!'
        except Exception as e:
            print 'GitTalk cannot be enabled. {}'.format(e.message)

    def disable(self):
        try:
            # git_root = get_git_root(os.getcwd())
            # installer = HookInstaller(git_root)
            self.hook.destroy()
            print 'GitTalk disabled successfully!'
        except Exception as e:
            print 'GitTalk cannot be disabled. {}'.format(e.message)

    def trigger(self):
        # TODO: implement trigger
        # root = Tkinter.Tk()
        # frames.VideoRecordControlFrame(root).pack()
        # root.mainloop()
        # print parse_message('ashdihasi $$method=record, location=commit, title=Explain funcA$$')
        commit_file_path = os.environ.get('GITTALK_COMMIT_MSG', None)
        commit_message = ''
        if commit_file_path:
            with open(commit_file_path, 'r+') as f:
                commit_message = f.read()

        window = GUI(commit_message=commit_message)
        window.show()