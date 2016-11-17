"""
Module for enabling and disabling git talk
"""

import os


class Hook(object):
    """ Class for all enable and disable methods """

    def __init__(self, git_r):
        self.git_root = git_r
        self.git_hook_path = os.path.join(
            self.git_root, '.git/hooks/commit-msg')
        self.git_talk_head = "##### gittalk hook (begin) #####\n"
        self.git_talk_tail = "##### gittalk hook (end) #####\n"

    def isGitInitialized(self):
        ''' Checks whether the project has a git project initialized '''
        git_folder = os.path.abspath(os.path.join(self.git_root, '.git'))
        return os.path.isdir(git_folder)

    def isHookInitialized(self):
        ''' Checks whether the project has a git project initialized '''
        hook_file = os.path.abspath(os.path.join(
            self.git_root, '.git/hooks/commit-msg'))
        return os.path.isfile(hook_file)

    def create(self):
        ''' Looks into .git/hooks to add hook from commit-msg '''
        if self.isGitInitialized():
            if self.isHookInitialized():
                hook_file = open(self.git_hook_path, 'r+')
            else:
                hook_file = open(self.git_hook_path, 'w+')
                hook_file.write("#!/bin/sh\n")

            # look for git commit head
            hook_content = hook_file.read()
            head_loc = hook_content.find(self.git_talk_head)

            # writes to commit-msg
            if head_loc == -1:
                hook_file.seek(0, 2)
                with open(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                       '../gittalk/assets/hooks/commit-msg'), "r") as hook:
                    # @TODO: add gittalk's full path with which('gittalk')
                    for line in hook:
                        hook_file.write(line)

                _st = os.stat(self.git_hook_path)
                os.chmod(self.git_hook_path, _st.st_mode | 0o111)
            else:
                print("Hook was already installed")
        else:
            print("Not in a git root folder")

    def destroy(self):
        ''' Looks into .git/hooks to remove hook from commit-msg '''
        if self.isGitInitialized():
            if self.isHookInitialized():
                hook_file = open(self.git_hook_path, 'r+')

                # look for git commit head
                hook_content = hook_file.read()
                head_loc = hook_content.find(self.git_talk_head)

                # writes to commit-msg
                if head_loc != -1:
                    hook_file.seek(0)
                    hook_content = hook_file.readlines()
                    # reopen for rewrite
                    hook_file = open(self.git_hook_path, 'w')

                    omit = False
                    deleted_hook = False
                    for line in hook_content:
                        if deleted_hook:
                            # stops checking for the hook
                            hook_file.write(line)
                        elif omit:
                            if line == self.git_talk_tail:
                                # found the tail
                                omit = False
                                deleted_hook = True
                        else:
                            if line == self.git_talk_head:
                                # found the head
                                omit = True
                            else:
                                hook_file.write(line)
            else:
                print("commit-msg does not exist")
        else:
            print("Not in a git root folder")
