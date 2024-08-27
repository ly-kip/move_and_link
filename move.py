#!/usr/bin/env python3
from sys import argv
from pathlib import Path

def printUsage():
    print('Usage: mov <file> <dir>')


if __name__ == '__main__':
    if len(argv) != 3:
        printUsage()
    else:
        srcFile = Path(argv[1])
        if not srcFile.is_file() :
            print(f'Error: "{srcFile}" must be a file!')
            printUsage()
            exit(-1)

        dstDir = Path(argv[2])
        if not dstDir.is_dir():
            print(f'Error: "{dstDir}" must be a dir!')
            printUsage()
            exit(-2)


        print (f'{srcFile.absolute()} -> {dstDir.absolute()} ={dstDir/srcFile.name}')       
        result = srcFile.rename(dstDir/srcFile.name)
        print(result)
        srcFile.symlink_to(result)
