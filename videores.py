#!/bin/env python

from ffvideo import VideoStream
from glob import iglob
from os import getcwd, chdir
import sys


def print_usage():
    print("videores.py")    


def enum_files(directory):
    chdir(directory)
    for f in iglob("*.mkv"):
        vs = VideoStream(f)
        print("Res: %dx%d\tFile: %s") % (vs.frame_width, vs.frame_height, f)

if __name__ == "__main__":    
    enum_files(sys.argv[1])

