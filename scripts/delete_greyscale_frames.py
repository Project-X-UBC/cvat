import cv2
import sys
import os
import argparse

def isgray(imgpath):
    img = cv2.imread(imgpath)
    if len(img.shape) < 3: return True
    if img.shape[2]  == 1: return True
    b,g,r = img[:,:,0], img[:,:,1], img[:,:,2]
    if (b==g).all() and (b==r).all(): return True
    return False

def main(dir_path):
    for root, subdirs, files in os.walk(dir_path):
        print('--\nEntering %s...' % root)

        for filename in files:
            file_path = os.path.join(root, filename)
            if '.png' not in file_path:
                continue

            if isgray(file_path):
                print('\t- removing greyscale image %s' % filename)
                # delete greyscale
                os.remove(os.path.join(root, filename))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', required=True, help='path containing frames')
    io_args = parser.parse_args()
    path = io_args.path
    main(path)
