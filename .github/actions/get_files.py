import os

def get_files() -> None:

    # List of file names to process
    file_names = os.listdir('files')

    # Print to extract the output
    print(file_names)

if __name__ == '__main__':
    get_files()