import argparse

def run():
    """ 
    `run` drives the command line interface for Git Talk.
    It exposes a command line interface through which users
    can interact with Git Talk to configure or invoke various
    functionalities.
    """
    parser = argparse.ArgumentParser(description='gittalk')

    parser.add_argument('-e', '--enable', action='store_true', required=False,
                        help='Enable Git Talk in the current Git repository.',
                        dest='enable')
    parser.add_argument('-d', '--disable', action='store_true', required=False,
                        help='Disable Git Talk in the current Git repository.',
                        dest='disable')
    parser.add_argument('-t', '--trigger', action='store_true', required=False,
                        help='Trigger Git Talk.',
                        dest='trigger')
    args = parser.parse_args()

    print 'hello git talk!'

if __name__ == '__main__':
    run()
