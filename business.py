'''
Copyright: Reese Wells
2017

This is the business program, run if you need to do business
**Works best in a black command line environment
'''
import sys # for important system information
import time # for sleeping
from colorama import init, Fore, Back, Style # for styling
import random

def getSystem():
    '''
    returns the OS type, noting which operating systems are not being used
    '''
    message = Fore.RED + 'Determining operating system...' # init message
    sys.stdout.write(message)
    sys.stdout.flush()
    os = sys.platform
    sys.stdout.write('\nPlatform detected as ' + os)
    sys.stdout.flush()
    time.sleep(.25)

    sys.stdout.write(Fore.RED + '\n\nERROR: memory diagnostics suggests the platform is incorrect? Use advanced detection algorithm? (Y/N)')
    sys.stdout.flush()
    answer = input()
    if answer == 'N' or answer == 'n':
        sys.stdout.write(Fore.YELLOW + '\nUsing less advanced detection algorithm.')
    if answer == 'Y' or answer == 'y':
        sys.stdout.write(Fore.YELLOW + '\nUsing advanced algorithms and memory scanning. Ensure no private information is stored in RAM, leaks will occur.')
    else:
        sys.stdout.write(Fore.YELLOW + '\nUser has been determined incompetent, proceeding with advanced scan.')

    sys.stdout.flush()
    time.sleep(.25)
    sys.stdout.write(Fore.GREEN + '\nOperating system has been set as: LINUX MINT')
    sys.stdout.flush()

    sys.stdout.write(Fore.YELLOW + '\n\nAttempting automatic lookup of disks using SERIAL BUS A\n')
    sys.stdout.flush()
    for i in range(0,random.randint(20,30)):
        sys.stdout.write('.')
        sys.stdout.flush()
        time.sleep(random.randint(0,10)/10)
    sys.stdout.write('\nAutomatic lookup failed. Checking maually...\n')
    sys.stdout.flush()
    time.sleep(.5)
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
