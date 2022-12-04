# This is the file which will try to automate the git
# IMPORTS
import subprocess


# Class git
class Git:

    def __init__(self):
        self.out = []
        self.err = []

    def return_output_error_list(self):
        return self.out, self.err

    def subprocess_git(self):
        cmd = ['git init',
               'git branch -m main'
               ]
        for i in cmd:
            sp = subprocess.Popen(i, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            out, err = sp.communicate()
            self.out.append(str(out))
            self.err.append(str(err))
