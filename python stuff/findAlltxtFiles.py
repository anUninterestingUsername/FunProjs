import os, re, sys


def get_txt(cur_dir, txt_file_regex):
    file_list = os.listdir(cur_dir)
    txt_files = []
    for file in file_list:
        file_dir = os.path.join(cur_dir, file)
        if txt_file_regex.search(file_dir):
            txt_files.append(file_dir)
        elif os.path.isdir(file_dir):
            txt_files.extend(get_txt(file_dir, txt_file_regex))
    return txt_files


def print_files_nice(txt_files):
    for file in txt_files:
        print(file)


txt_file_regex = re.compile(r".txt$")
file_dir = sys.argv[1]
if os.path.isdir(file_dir):
    print("running")
    txt_files = get_txt(file_dir, txt_file_regex)
    print("\nFiles found:")
    print_files_nice(txt_files)
else:
    print("dir does not exist")