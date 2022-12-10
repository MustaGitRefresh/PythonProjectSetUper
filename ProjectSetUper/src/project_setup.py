from gitauto import *
import os


class Dir:
    def __init__(self):

        self.output_list = None
        self.error_list = None

        """
            We have to define the git_dir first because it will throw AttributeError
            because it will be created the Git object after function createDir is called.
        """
        self.createDir()
        self.error_output_list(self.output_list, self.error_list)
        self.sub_main_folder()

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
        self.git_repo_init()

    def sub_main_folder(self):
        path = 'E:\\Pyton Projects\\GitAuto'
        os.chdir(path)
        print("change sub")
        print(os.getcwd())
        os.mkdir('GitAuto')
        os.path.join(path, 'GitAuto')
        print(os.getcwd())

    def git_repo_init(self):
        out_list, err_list = Git().subprocess_git()
        self.output_list = out_list
        self.error_list = err_list
        return None

    @staticmethod
    def error_output_list(out, err):
        print(out)
        print("_____________________________________________________")
        print(err)


git_directory = Dir()
