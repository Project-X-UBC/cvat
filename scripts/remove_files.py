import sys
import os
import argparse
import shutil

def main(dir_path, to_remove, new_dir=None):
    for root, subdirs, files in os.walk(dir_path):
        print('--\nEntering %s...' % root)

        for filename in files:
            file_path = os.path.join(root, filename)
            if filename in to_remove:
                if not new_dir:
                    # delete file
                    print('\t- removing file %s' % filename)
                    os.remove(os.path.join(root, filename))
                else:
                    # move file to new directory
                    print('\t- moving file %s' % filename)
                    if not os.path.exists(new_dir):
                        os.makedirs(new_dir)
                    shutil.move(os.path.join(root, filename), os.path.join(new_dir, filename))
                # remove remove/moved file from to_remove list
                to_remove.remove(filename)
      
    print("\n\nDone. Following files to be remove/moved were not found...")
    for f in to_remove:
        print('\t- %s' % f)


# example usage:
# python remove_files.py --path ~/project_x/data --to_remove files_to_remove.txt --new_dir ~/project_x/data/bad_footage/
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', required=True, help='path containing files')
    parser.add_argument('--to_remove', required=True, help='.txt file path containing list of files to remove. Each line should contain a single file name.')
    parser.add_argument('--new_dir', required=False, help='path of directory to move the to_remove files to. Directory can already exist.')
    io_args = parser.parse_args()
    with open(io_args.to_remove) as f:
      to_remove_list = f.read().splitlines() 
    print(to_remove_list)
    main(io_args.path, to_remove_list, io_args.new_dir)
