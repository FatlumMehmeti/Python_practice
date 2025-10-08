# import platform as p
# import os as o
# print(p.uname())
##################################################################################################################
# try:
#     o.mkdir("new_dir")
#     o.makedirs("my_first_directory/my_second_directory")
# except FileExistsError as e:
#     print("Directory already exists:", e)
# print(o.listdir())
##################################################################################################################
# o.chdir("my_first_directory")
# print(o.getcwd())
# o.chdir("my_second_directory")
# print(o.getcwd())
##################################################################################################################
# o.mkdir("my_first_directory1")
# print(o.listdir())
# o.rmdir("my_first_directory1")
# print(o.listdir())
##################################################################################################################
import os

returned_value = os.system("mkdir my_first_directory")
print(returned_value)
##################################################################################################################
import os

def find(path, dir):
    # Walk through all directories and subdirectories
    for root, dirs, files in os.walk(path):
        for d in dirs:
            if d == dir:
                # Print the absolute path of the found directory
                print(os.path.abspath(os.path.join(root, d)))