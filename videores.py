#!/bin/env python

from ffvideo import VideoStream
from glob import iglob
from os import getcwd, chdir
import sys

def print_usage():
    pass


def enum_files(dir):
    chdir(dir)
    for file in iglob("*.mkv"):
        vs = VideoStream(file)
        print "Res: %dx%d\tFile: %s" % (vs.frame_width, vs.frame_height, file)

if __name__ == "__main__":
    print("videores.py")
    enum_files(sys.argv[1])

