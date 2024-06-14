import os

def get_files() -> None:
    # List of file names to process
    file_names = os.listdir('files')

    print(','.join(file_names))

if __name__ == '__main__':
    get_files()