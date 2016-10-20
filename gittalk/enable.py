"""
Module for enabling and disabling git talk
"""

import os

class HookInstaller(object):
    """ Class for all enable and disable methods """

    # Global var
    pwd = os.getcwd()
    git_talk_head = "#### Git Talk (begin)"
    git_talk_tail = "#### Git Talk (end)"

    def isGitInitialized(self):
        ''' Checks whether the project has a git project initialized '''
        git_folder = os.path.abspath("".join((self.pwd, '/.git')))
        return os.path.isdir(git_folder)

    def isHookInitialized(self):
        ''' Checks whether the project has a git project initialized '''
        hook_file = os.path.abspath("".join((self.pwd, '/.git/hooks/post-commit')))
        return os.path.isfile(hook_file)

    def addHook(self):
        ''' Looks into .git/hooks to add hook from post-commit '''
        if self.isGitInitialized():
            if self.isHookInitialized():
                hook_file = open("".join((self.pwd, '/.git/hooks/post-commit')), 'r+')
            else:
                hook_file = open("".join((self.pwd, '/.git/hooks/post-commit')), 'w+')

            # look for git commit head
            hook_content = hook_file.read()
            head_loc = hook_content.find(self.git_talk_head)

            # writes to post-commit
            if head_loc == -1:
                hook_file.seek(0, 2)
                with open("githook.txt", "r") as hook:
                    for line in hook:
                        hook_file.write(line)
            else:
                print("Hook was already installed")
        else:
            print("Not in a git root folder")

    def rmHook(self):
        ''' Looks into .git/hooks to remove hook from post-commit '''
        if self.isGitInitialized():
            if self.isHookInitialized():
                hook_file = open("".join((self.pwd, '/.git/hooks/post-commit')), 'r+')

                # look for git commit head
                hook_content = hook_file.read()
                head_loc = hook_content.find(self.git_talk_head)
                hook_file.close()

                # writes to post-commit
                if head_loc == -1:
                    hook_file = open("".join((self.pwd, '/.git/hooks/post-commit')), 'w')
                    hook_content = hook_file.readlines()
                    omit = False
                    deletedHook = False
                    for line in hook_content:
                        if deletedHook:
                            ## stops checking for the hook
                            hook_file.write(line)
                        elif omit:
                            if line.find(self.git_talk_tail)!=-1:
                                ## found the tail
                                omit = False
                                deletedHook = True
                        else:
                            if line.find(self.git_talk_tail)!=-1:
                                ## found the head
                                omit = True
                            else:
                                hook_file.write(line)
            else:
                print("post-commit does not exist")
        else:
            print("Not in a git root folder")
