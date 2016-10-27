import os
import re
import sys
import time
from ui import frames
import Tkinter
import upload_youtube
import subprocess as sp

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



# if no upload, simply don't include $$.*$$ in the commit message
# if upload, include the following strings in the commit message:
# $$method=mm, location=ll, title=tt (optional), description=dd (optional)$$
# method
    # record: record from local camera
    # local: choose existing file from file picker
# location
    # commit: include video url in the commit message
    # x: insert video url as a comment in line x
# title: title of the video shown on Youtube
# description (optional): description of the video on Youtube
#
# e.g. This is a commit message $$method=record, location=58, title=Explain funcA$$


def has_upload_task(message):
    if re.search(r'\$\$.*\$\$', message):
        return True
    return False

def parse_message(message):
    if has_upload_task(message):
        method = re.search(r'\$\$method=(.*?),', message).group(1)
        location = re.search(r'location=(.*?),', message).group(1)
        title = re.search(r'title=([^\$]*)[,\$]', message).group(1)
        description = ''
        if re.search('description=',message):
            description = re.search('description=(.*?),', message).group(1)

    # more codes to be added to use method etc.

    if method == 'record':
        # os.system('gittalk/ffmpeg.sh v')
        try:
            ff = sp.Popen(['gittalk/ffmpeg.sh', 's'])
            while True:
                pass
        except KeyboardInterrupt:
            pass
        except Exception, e:
            print e
        finally:
            try:
                ff.kill()
            except OSError:
                pass
            print 'Recording stopped.'

        url = upload_youtube.upload_youtube('./output.mp4')
        print url
    elif method == 'local':
        root = Tkinter.Tk()
        frames.VideoRecordControlFrame(root).pack()
        root.mainloop()




