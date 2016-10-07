import argparse

def run():
    """ 
    `run` drives the command line interface for Git Talk.
    It exposes a command line interface through which users
    can interact with Git Talk to configure or invoke various
    functionalities.
    """
    parser = argparse.ArgumentParser(description='gittalk')
    args = parser.parse_args()
    print 'Hello Git Talk!'


if __name__ == '__main__':
    run()
