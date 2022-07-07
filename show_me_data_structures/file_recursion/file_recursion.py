import os


def find_files(suffix, path):
    if not os.path.exists(path):
        return []

    files_and_folders = os.listdir(path)

    sfx = '.' + suffix
    files = [file for file in files_and_folders if sfx in file]
    folders = [folder for folder in files_and_folders if '.' not in folder]

    for file in files:
        print(file)
    for folder in folders:
        files.extend(find_files(suffix, path + '/' + folder))

    return files


path_base = os.getcwd() + \
    "/Desktop/algorithmsUdacityNanoDegree/show_me_data_structures/file_recursion/testdir"

print(find_files(suffix='c', path=path_base))
