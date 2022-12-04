from gitauto import *
import os


class Dir:
    def __init__(self):
        """
            We have to define the git_dir first because it will throw AttributeError
            because it will be created the Git object after function createDir is called.
        """
        self.createDir()
        self.error_output_list()

    def createDir(self):
        path = "E:\\Pyton Projects"
        os.chdir(path)
        print(os.getcwd())
        try:
            os.mkdir('GitAuto')
        except FileExistsError:
            print('choose a new name')

        new_path = os.path.join(path, 'GitAuto')
        os.chdir(new_path)
        print(os.getcwd())
        Git().subprocess_git()

    def error_output_list(self):
        out, err = Git().return_output_error_list()
        print(out)
        print('_______________________________')
        print(err)


git_directory = Dir()
