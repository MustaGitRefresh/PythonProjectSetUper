from gitauto import *
import os


class Dir:
    def __init__(self):

        self.project_name = None
        self.output_list = None
        self.error_list = None
        self.path = "E:\\Pyton Projects"

        """
            We have to define the git_dir first because it will throw AttributeError
            because it will be created the Git object after function createDir is called.
        """
        self.taking_project_name_user()
        self.createDir()
        self.error_output_list(self.output_list, self.error_list)
        self.sub_main_folder()
        self.src_tests()

    def createDir(self):
        os.chdir(self.path)
        print(os.getcwd())
        try:
            os.mkdir(self.project_name)
        except FileExistsError:
            print('choose a new name')

        new_path = os.path.join(self.path, self.project_name)
        os.chdir(new_path)
        print(os.getcwd())
        self.git_repo_init()

    def os_ones(self, sub_folder_path, folder_name):
        if not folder_name:
            folder_name = self.project_name
        os.chdir(sub_folder_path)
        print("change sub")
        print(os.getcwd())
        os.mkdir(folder_name)
        os.path.join(sub_folder_path, folder_name)
        print(os.getcwd())

    def sub_main_folder(self):
        sub_folder_path = self.path + "\\{}".format(self.project_name)
        self.os_ones(sub_folder_path, None)

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

    def taking_project_name_user(self):
        project_name = input("Enter the project name:\n")
        self.project_name = project_name

    def src_tests(self):
        folders = ['src', 'tests']
        for i in range(len(folders)):
            src_tests = self.path + '\\{}'.format(folders[i])
            self.os_ones(src_tests, folders[i])


git_directory = Dir()
