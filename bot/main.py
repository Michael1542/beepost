from reader import Reader
from appscript import *

def main():
    reader = Reader()
    print("main")
    reader.write_image()
    app('Finder').desktop_picture.set(mactypes.File("sample_image.jpg"))

if __name__ == "__main__":
    main()