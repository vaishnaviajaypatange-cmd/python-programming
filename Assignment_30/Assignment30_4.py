# Q4) Copy File Contents into Another File

# Problem Statement:
# Write a program which accepts two file names from the user.

# First file is an existing file

# Second file is a new file

# Copy all contents from the first file into the second file.

# Input:
# ABC.txt Demo.txt

# Expected Output:
# Contents of ABC.txt copied into Demo.txt.

import sys
import os

def CopyFile(Filename1, Filename2):
    if not os.path.exists(Filename1):
        print("Source file does not exist")
        return

    with open(Filename1, "r") as fobj1, open(Filename2, "w") as fobj2:
        for line in fobj1:
            fobj2.write(line)

    print(f"Contents of {Filename1} copied into {Filename2}.")

def main():
    if len(sys.argv) < 3:
        return

    CopyFile(sys.argv[1], sys.argv[2])

if __name__ == "__main__":
    main()
