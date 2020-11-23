#!/usr/bin/env python

# import sys
import os
# import subprocess
import argparse
import datetime

print('A script to back up any or my home directory...\n')

parser = argparse.ArgumentParser(description='A script for back up')
# Doesn't allow -b and -m arguments to be used simultaneously. Since they're in the same group.
group = parser.add_mutually_exclusive_group(required=True)

group.add_argument('-b', 
            default=None, type=str,
            required=False, help='Directory for what to backup')

group.add_argument('-m', 
            default='~/', type=str, 
            required=False, help='Will backup home dir & exclude hard coded dir')

# Loads the arguments to args variabel.
args = parser.parse_args()

# Assigning arguments to a variabel
directory = args.b
directory_home = args.m

# # Global variables
EXCLUDE = "--exclude='playground' --exclude='tmp' --exclude='VirtualBox\ VMs'"

def back_up(arg):
    '''Performs the actual backup using tar
    Tar params: c = create, z = zip, p = preserve permissions, 
    f = tells tar that next argument is the file name the archive 
    '''

    dir_to_backup = arg
    where = '/backups/home_dir/'
    output_name = 'mohamad@ZMachine_backup_{}.tar.gz'.format(datetime.datetime.now().strftime('%d-%B-%Y'))
    print(f'Directory backed up {dir_to_backup} to {where} with the name: \n\t{output_name}\n')

    command_tar = f'tar cfzp {where}{output_name} {EXCLUDE} {dir_to_backup}'

    status = os.system(command_tar)

    return (status)

def main():

    # Flag for storing return value of back_up() function.
    flag = 0

    # directory = -b argument
    # directory_home = -m argument
    if directory:
        flag = back_up(directory)
    else: 
        flag = back_up(directory_home)

    if flag == 0:
        print('Backing up files & directories successful.')
    else:
        print('Backing up files & directories failed.')
    
if __name__ == '__main__':
    main()