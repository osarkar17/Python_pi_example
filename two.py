#!/usr/bin/python3

import os;
import subprocess;

def create_lvm():
    commands = [
        "sudo lvcreate -L 1000M -n mylv myvg",
        "sudo mkfs.ext4 /dev/myvg/mylv",
        "touch three.py",
    ]
    for command in commands:
        subprocess.run(command, shell=True, check=True);

if __name__ == "__main__":
    create_lvm();