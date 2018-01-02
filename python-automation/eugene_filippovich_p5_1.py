import os


def current_files(path):
    for root, dirs, files in path:
        for f in files:
            yield os.path.join(root, f)


generator = current_files(os.walk("C:/"))

for _ in generator:
    print _