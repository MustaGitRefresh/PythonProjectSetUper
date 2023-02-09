from gitauto import *
import os

# MODULE LEVEL variables
sub_folder_path = ""


class Dir:
    def __init__(self):
        self.path = None

        self.project_name = None
        self.output_list = None
        self.error_list = None

        """
            We have to define the git_dir first because it will throw AttributeError
            because it will be created the Git object after function createDir is called.
        """
        self.taking_project_dir_user()
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
        with open('Plan.txt', 'w') as plan_creating_file:
            plan_creating_file.write(
                "#### CREATE YOUR PROJECT PLAN HERE ######")
        self.git_repo_init()

    def sub_main_folder(self):
        global sub_folder_path
        sub_folder_path = self.path + "\\{}".format(self.project_name)
        os.chdir(sub_folder_path)
        print("change sub")
        print(os.getcwd())
        os.mkdir(self.project_name)
        os.path.join(sub_folder_path, self.project_name)
        # print(os.getcwd())

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
        global sub_folder_path
        sub_folder_path += "\\{}".format(self.project_name)
        folders_main = ['src', 'tests']
        for i in folders_main:
            os.chdir(sub_folder_path)
            os.mkdir(i)
        return self.project_main_file_creator(self.project_name)

    @staticmethod
    def project_main_file_creator(project_name):
        project_name = project_name.replace(' ', '_')
        os.chdir(os.path.join(sub_folder_path, "src"))
        # print(os.getcwd())
        with open(f'{project_name}.py', 'w') as f:
            f.write(
                """print("Hello World")"""
            )

    def taking_project_dir_user(self):
        """
        This will take the input from the user which will be the project directory
        """
        project_dir = input("Enter the project directory:\n")
        self.path = project_dir


git_directory = Dir()
