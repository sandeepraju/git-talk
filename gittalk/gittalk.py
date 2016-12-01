import os
import sys

from utils import get_git_root
from hook import Hook
from gui import GUI
from capture import FFmpeg, VIDEO, SCREEN
from upload import upload_to_youtube

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

        config_path = os.path.join(
            os.environ['HOME'], '.gittalk/.config')
        if os.path.isfile(config_path):
            while True:
                sys.stderr.write('>> press ENTER to start')
                raw_input()
                mode = open(config_path, 'r').read().strip().lower()
                ffmpeg = FFmpeg()
                proc = None
                if mode == 'screen':
                    proc = ffmpeg.start(SCREEN, os.path.join(
                    os.environ['HOME'], '.gittalk/output.mp4'))
                else:
                    proc = ffmpeg.start(VIDEO, os.path.join(
                    os.environ['HOME'], '.gittalk/output.mp4'))

                sys.stderr.write('>> press ENTER to stop')
                raw_input()
                ffmpeg.stop(proc)

                video_file_path = os.path.join(
                    os.environ['HOME'], '.gittalk/output.mp4')
                upload_to_youtube(
                    video_file_path, commit_message, commit_message)
                break
        else:
            window = GUI(commit_message=commit_message)

