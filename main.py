#!/usr/bin/env python

import sys
import os
import subprocess
import argparse
import datetime
from testing import DIR_TO_BACKUP


# -C ~/Books . -C ~/bin . -C ~/Computer_Science . -C ~/Documents . -C ~/Desktop . -C ~/Dev . -C ~/Downloads .\
            # -C ~/home . -C ~/Music . -C ~/nextcloud . -C ~/node_modules . -C ~/
# parser = argparse.ArgumentParser(description='A script for back up')
# parser.add_argument('--a', default=1, type=int, help='The "a" variable')

# # Global Variables # #
EXCLUDE = "--exclude='backup' --exclude='playground' --exclude='tmp' --exclude='VirtualBox\ VMs'"


def what_to_backup():
    '''User chooses what to backup. Returns the argument for tar.'''
    print('\tChoose an option for backing up:\n \
            1. Home directory (/home/mohamad/) NOTE!: Use --exlude to see excluded directories.\n\
            2. Library\n\
            3. Developer work\n\
            4. Computer Science Program/Courses\n\
            5. Medical School\n\
            6. Photos\n\
            ')
    option = input()
    return {
        1: '~/',
        2: '~/Books',
        3: '~/Dev',
        4: '~/Computer_Science/Programvaruteknik*',
        5: '~/Documents/GUMED/',
        6: '~/Photos/'
    }[option]

def where_to_backup():
    '''User chooses where to backup. Returns the argument for tar.'''
    print('\t Where to backup?\n \
            1. ~/backups\n\
            2. farman_storage\n\
            ')
    option = input()
    return {
        1: '~/backups',
        2: '/mnt/storage/backups'
    }[option]

def back_up():
    '''
    Performs the actual backup using tar
    Tar params: c = create, z = zip, p = preserve permissions, 
    f = tells tar that next argument is the file name the archive
    '''
    
    directories_to_backup = what_to_backup()
    where = where_to_backup()
    OUTPUT_NAME = 'mohamad@ZMachine_backup_{}'.format(datetime.datetime.now().strftime('%d-%B-%Y'))

    print(f'Name of created back up: {OUTPUT_NAME}')

    command_tar = f'tar --exclude-backups {EXCLUDE} -cfzp {str(where) + str(OUTPUT_NAME)} {directories_to_backup}'        # c = create, z = zip, p = preserve permissions 

    tar = os.system(command_tar) 

    return print(tar)

if __name__ == '__main__':
    back_up()