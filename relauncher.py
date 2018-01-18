"""Main module to run other scripts.

1. Launch SCRIPT_TO_LAUNCH python's script.
2. Wait TIME_FOR_WORK to complete SCRIPT_TO_LAUNCH script.
3. Check if SCRIPT_TO_LAUNCH completed.
4. If not completed, check when was changed FILE_TO_CHECK.
   If FILE_TO_CHECK changed more than TIME_TO_UNFREEZE sec ago,
   then kill SCRIPT_TO_LAUNCH and launch it again (go to point 1).
5. Wait SEC_RESTARTING and go to point 1.
"""
from subprocess import Popen
import os
import time
import sys


SCRIPT_TO_LAUNCH = 'main.py'
FILE_TO_CHECK = 'last_result.log'
TIME_FOR_WORK = 10
TIME_TO_UNFREEZE = 60
SEC_RESTARTING = 10


def run_relauncher():
    """Main function of relauncher."""
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)
    while True:
        # start other script in main_app.py
        print('*' * 80)
        print('Launch main script')
        print('*' * 80)
        process = Popen(['python', SCRIPT_TO_LAUNCH])
        time.sleep(TIME_FOR_WORK)  # give the program some time to write into logfile
        while True:
            if process.poll() is not None:
                # script terminated. No need to check crash or usual
                # print('Regularly terminated or crashed.')
                break
            file_age_in_s = time.time() - os.path.getmtime(FILE_TO_CHECK)
            if file_age_in_s > TIME_TO_UNFREEZE:
                # script frozen, so we need to kill it
                print('Frozen, so kill it.')
                process.kill()
                break
            time.sleep(1)
        print('Restarting...')
        if SEC_RESTARTING < 2:
            print('*' * 80)
            break
        print(1, end='')
        for i in range(2, SEC_RESTARTING):
            time.sleep(1)
            print(',', i, end='')
            sys.stdout.flush()
        print('\n', '*' * 80, sep='')


if __name__ == '__main__':
    run_relauncher()
