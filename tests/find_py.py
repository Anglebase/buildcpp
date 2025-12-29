from pycmake import find_files

if __name__ == '__main__':
    print(find_files(r'src', '*.py'))
    print(find_files(r'src', '*.py', True))
