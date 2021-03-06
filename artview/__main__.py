# add this folder to path so I can import artview
import sys
import os

path = os.path.dirname(sys.modules[__name__].__file__)
path = os.path.join(path, '..')
sys.path.insert(0, path)

import artview


def main(argv):
    script, DirIn, filename, field = artview.parser.parse(argv)

    if script:
        artview.scripts.scripts[script](DirIn, filename, field)
    else:
        artview.run(DirIn, filename, field)

if __name__ == "__main__":
    main(sys.argv)
