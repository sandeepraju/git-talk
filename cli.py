import argparse

from gittalk import GitTalk

def run():
    """ 
    `run` drives the command line interface for Git Talk.
    It exposes a command line interface through which users
    can interact with Git Talk to configure or invoke various
    functionalities.
    """
    # TODO: add a Tkiner check here

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
        return

    if args.disable:
        gt.disable()
        return

    if args.trigger:
        gt.trigger()
        return

if __name__ == '__main__':
    run()
