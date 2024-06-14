import argparse
import os

parser = argparse.ArgumentParser(description='Process a file.')
parser.add_argument('--file-name', type=str, help='The name of the file to process')

args = parser.parse_args()

def process_file(file_name):
    print(f"Processing file: {file_name}")

print(os.environ['FILES'])
process_file(args.file_name)
