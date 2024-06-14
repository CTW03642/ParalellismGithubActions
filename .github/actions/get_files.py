import os

def get_files() -> None:
    # List of file names to process
    file_names = os.listdir('files')
    print(' '.join(file_names))
    return
    #os.environ['FILES'] = ','.join(file_names)
    env_file = os.getenv('GITHUB_ENV')

    with open(env_file, "a") as myfile:
        myfile.write(f"FILES={','.join(file_names)}")

    #print(os.environ['FILES'])

if __name__ == '__main__':
    get_files()