import os
import shutil
import argparse

def copy_files(source_dir, destination_dir):
    try:
        for item in os.listdir(source_dir):
            item_path = os.path.join(source_dir, item)
            if os.path.isfile(item_path):
                _, extension = os.path.splitext(item)
                extension_dir = os.path.join(destination_dir, extension[1:]) 
                os.makedirs(extension_dir, exist_ok=True)
                shutil.copy2(item_path, extension_dir)
            elif os.path.isdir(item_path):
                copy_files(item_path, destination_dir)
    except Exception as e:
        print(f"Error: {e}")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("src")
    parser.add_argument("-d", "--dst", default="dist")
    args = parser.parse_args()

    src = args.src
    dst = args.dst

    copy_files(src, dst)

if __name__ == "__main__":
    main()
