#!/usr/bin/env python3
from sys import argv
from pathlib import Path

def printUsage():
    print('Usage: move.py <file> <dir>')

def printErrorAndExit(message, errorCode):
    print(message)
    printUsage()
    exit(errorCode)

if __name__ == '__main__':
    if len(argv) != 3:
        printUsage()
    else:
        srcFile = Path(argv[1])
        if not srcFile.is_file() :
            printErrorAndExit(f'Error: "{srcFile}" must be a file!', 1)

        dstDir = Path(argv[2])
        if not dstDir.is_dir():
            printErrorAndExit(f'Error: "{dstDir}" must be a dir!', 2)

        ## print (f'{srcFile.absolute()} -> {dstDir.absolute()} = {dstDir/srcFile.name}')       
        result = srcFile.rename(dstDir/srcFile.name)
        ## print(result)
        srcFile.symlink_to(result)

        if not srcFile.is_symlink() :
            print(f"Error: Symlink {srcFile.absolute()} not created!")
            exit(-1)

