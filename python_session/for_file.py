import glob
import shutil
import pathlib


def hoge():
    return print('hoge')


def join_filename():
    list = glob.glob('**/*', recursive=True)
    for i in list:
        split_list = i.split('/')
        print('_'.join(split_list))


def join_and_cp():
    output_dir_path = 'archive'
    list = glob.glob('**/*', recursive=True)
    for i in list:
        if is_file(i):
            split_list = i.split('/')
            rename_filename = '_'.join(split_list)
            shutil.copy(i, pathlib.Path(output_dir_path, rename_filename))


def is_file(path):
    if isinstance(path, str):
        path = pathlib.Path(path)
    return path.suffix
