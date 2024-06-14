import argparse

def process_file(file_name):

    print(f"\nProcessing file: {file_name}")

    with open(f'files/{file_name}', 'r') as file:
        # Read the content of the file
        file_content = file.read()
         
        # Print the content
        print("File Content:\n", file_content)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process a file.')
    parser.add_argument('--file-name', type=str, help='The name of the file to process')

    args = parser.parse_args()

    process_file(args.file_name)