#!/usr/bin/env python

import sys
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
OUTPUT_NAME = 'mohamad@ZMachine_backup_{}.tar.gz'.format(datetime.datetime.now().strftime('%d-%B-%Y'))
EXT_STORAGE_MOUNT_DIR = '/mnt/storage/backups/archive/mohamad@ZMachine/'

def back_up(arg):
    '''Performs the actual backup using tar
    Tar params: c = create, z = zip, p = preserve permissions,
    f = tells tar that next argument is the file name the archive
    '''

    dir_to_backup = arg
    where = '/backups/home_dir/'
    print(f"Directory backed up: {dir_to_backup} to {where} as: \n\t{OUTPUT_NAME}\n")

    command_tar = f'tar cfzp {where}{OUTPUT_NAME} {EXCLUDE} {dir_to_backup} 2>stderr'

    status = os.system(command_tar)

    return status

def check_external_storage():
    ''' 
    Checks to see if external storage is mounted
    Returns True or False
    '''
    try:
        status = os.path.isdir(f'{EXT_STORAGE_MOUNT_DIR}')
    except OSError as e:
        print('\nExternal storage could not be accessed')
    
    return status

def mv_backup_to_storage():
    '''
    Function to move tar back up to external storage
    Return True or False
    '''
    print('Moving files with to external storage...')

    os.chdir('/backups/home_dir/')
    command_mv = f'mv {OUTPUT_NAME} {EXT_STORAGE_MOUNT_DIR} 2>stderr'
    exit_code = os.system(f'{command_mv}')

    if exit_code == 0:
        return True
    else:
        return False

def main():

    # Flag for storing return value of back_up() function.
    flag_back_up = 0

    # directory = -b argument
    # directory_home = -m argument
    if directory:
        flag_back_up = back_up(directory)
    else:
        flag_back_up = back_up(directory_home)

    if flag_back_up == 0:
        print('Backing up files & directories successful.\n')
    else:
        print('Backing up files & directories failed.\n')
        sys.exit()

    if mv_backup_to_storage() == True:
        print('Backup files moved to external storage successfully.\nExiting script.') and sys.exit()
    else:
        print('Failed to move backup files to external storage...\nExiting..') and sys.exit()

if __name__ == '__main__':
    main()