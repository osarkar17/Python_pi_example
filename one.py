#!/usr/bin/python3
import os;
import subprocess;

os.system("touch two.py");
def create_lvm():
    commands = [
        "sudo lvcreate -L 200M -n mylv1 myvg1",
        "sudo mkfs.ext4 /dev/myvg1/mylv1",
        "sudo mkdir /mnt/mylv1",
        "sudo mount /dev/myvg1/mylv1 /mnt/mylv1",
    ]
    for command in commands:
        subprocess.run(command, shell=True, check=True);

if __name__ == "__main__":
    create_lvm();

