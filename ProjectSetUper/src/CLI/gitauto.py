# This is the file which will try to automate the git
# IMPORTS
import subprocess


# Class git
class Git:

    def __init__(self):
        self.output = []
        self.error = []

    def subprocess_git(self):
        cmd = ['git init',
               'git branch -m main'
               ]
        for i in cmd:
            sp = subprocess.Popen(i, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            out, err = sp.communicate()
            self.output.append(out)
            self.error.append(err)
            return self.output, self.error
