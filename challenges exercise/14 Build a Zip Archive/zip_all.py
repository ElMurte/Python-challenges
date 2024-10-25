import os
from zipfile import ZipFile

def zip_all(search_dir, extension_list, output_path):
    search_dir = os.path.abspath(search_dir)
    output_path = os.path.abspath(output_path)

    print(f"Searching in directory: {search_dir}")
    print(f"Output zip file will be created at: {output_path}")

    with ZipFile(output_path, 'w') as output_zip:
        for root, _, files in os.walk(search_dir):
            rel_path = os.path.relpath(root, search_dir)
            for file in files:
                file_path = os.path.join(root, file)
                _, ext = os.path.splitext(file)

                # Debug print: show all files found
                print(f"Found file: {file_path}, Extension: {ext.lower()}")

                if ext.lower() in extension_list:
                    arcname = os.path.join(rel_path, file)
                    print(f"Adding {file_path} as {arcname}")
                    output_zip.write(file_path, arcname=arcname)

if __name__ == '__main__':
    # Use the relative path for my_stuff since you're in the main directory
    zip_all('c:/Users/elvis/Desktop/python exercises/src/14 Build a Zip Archive/', ['.jpg', '.txt'], './my_stuff.zip')
