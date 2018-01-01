import os
import pprint

def current_files():
    files_with_path = []
    path = "F:/Test"
    for root, dirs, files in os.walk(path):
        for f in files:
            f = os.path.join(root, f)
            files_with_path.append(f)
    pprint.pprint(files_with_path)
    return current_files

current_files()