'''
Copyright: Reese Wells
2017

This is the business program, run if you need to do business
**Works best in a black command line environment
'''
import sys # for important system information
import time # for sleeping
from colorama import init, Fore, Back, Style # for styling

def getSystem():
    '''
    returns the OS type, noting which operating systems are not being used
    '''
    message = Fore.RED + 'Determining operating system...' # init message
    sys.stdout.write(message)
    sys.stdout.flush()
    time.sleep(1)
    sys.stdout.write('\n')
    nextSym = 0
    disks = ['a','b','d','e','g','h','z']
    for i in range(0, len(disks)):
        for j in range(0, 50):
            symbols = ['\\','|','/','-']
            message = Fore.GREEN + 'Checking disk ' + disks[i] + " " + symbols[nextSym]
            nextSym = (nextSym + 1) % 4
            sys.stdout.write(message + '\r')
            sys.stdout.flush()
            time.sleep(.1)
        message = Fore.RED + 'Checking disk ' + disks[i] + '.'
        sys.stdout.write(message)
        time.sleep(.1)
        sys.stdout.write('\r')
        message = Fore.RED + 'Checking disk ' + disks[i] + '..'
        sys.stdout.write(message)
        time.sleep(.1)
        sys.stdout.write('\r')
        message = Fore.RED + 'Checking disk ' + disks[i] + '...failed.'
        sys.stdout.write(message)
        time.sleep(.1)
        sys.stdout.write('\n')
        sys.stdout.flush()

getSystem()
