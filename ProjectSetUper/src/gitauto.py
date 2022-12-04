# This is the file which will try to automate the git
# IMPORTS
import subprocess


# Class git
class Git:
    @staticmethod
    def subprocess_git():
        cmd = ['git init',
               'git branch -m main'
               ]
        for i in cmd:
            sp = subprocess.Popen(i, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            out, err = sp.communicate()
            print('----------------------')
            print(out)
            print('\n \n')
            print(err)
