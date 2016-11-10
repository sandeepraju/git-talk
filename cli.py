import argparse
import os

from gittalk import GitTalk
from gittalk.utils import which, make_sure_path_exists

def run():
    """ 
    `run` drives the command line interface for Git Talk.
    It exposes a command line interface through which users
    can interact with Git Talk to configure or invoke various
    functionalities.
    """

    # do explict dependency checks
    try:
        import Tkinter
    except Exception as e:
        print 'Make sure your Python has Tkinter installed before using GitTalk!'

    if not which('ffmpeg'):
        print 'Please make sure FFmpeg is installed before using GitTalk!'

    # create a folder to be used by GitTalk
    make_sure_path_exists(os.path.join(os.environ['HOME'], '.gittalk'))

    parser = argparse.ArgumentParser(description='Audio & Video annotations to your code via Git')
    group = parser.add_mutually_exclusive_group(required=True)

    group.add_argument('-e', '--enable', action='store_true', required=False,
                        help='Enable Git Talk in the current Git repository.',
                        dest='enable')
    group.add_argument('-d', '--disable', action='store_true', required=False,
                        help='Disable Git Talk in the current Git repository.',
                        dest='disable')
    group.add_argument('-t', '--trigger', action='store_true', required=False,
                        help='Trigger Git Talk.',
                        dest='trigger')
    args = parser.parse_args()

    gt = GitTalk()
    if args.enable:
        gt.enable()

    elif args.disable:
        gt.disable()

    elif args.trigger:
        gt.trigger()


if __name__ == '__main__':
    run()
