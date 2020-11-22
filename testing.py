import os
import subprocess


def where_to_backup():
    print('\t Where to backup?\n \
            1. ~/backups\n\
            2. farman_storage\n\
            ')
    option = int(input())
    return {
        1: '~/backups',
        2: '/mnt/storage/backups'
    }[option]

DIR_TO_BACKUP = where_to_backup()

print(DIR_TO_BACKUP)

def main():
    print('in main')

if __name__ == '__main__':
    print('in if')
    main()
    where_to_backup()