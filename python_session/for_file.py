import glob

def hoge():
    return print('hoge')

def join_filename():
    list = glob.glob('**/*', recursive=True)
    for i in list:
        split_list = i.split('/')
        print('_'.join(split_list))