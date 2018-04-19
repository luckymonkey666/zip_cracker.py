from zipfile import ZipFile
from sys import version_info
import sys
import os, time

zipp = input('Enter path to ZipFile : ')
try:
    z = ZipFile(zipp, 'r')
    z.close()
except Exception as e:
    print(e)
    sys.exit()

wordlist = input('Enter path to wordlist : ')
try:
    w = open(wordlist, 'r')
    w.close()
except Exception as e:
    print(e)
    sys.exit()

wordlist = open(wordlist, 'r')

for word in wordlist:
    word = word.strip('\n')
    pwd = b""
    if version_info.major == 3:
        pwd += bytes(word, "utf-8")
    else:
        pwd += bytes(word)
    try:
        zf = ZipFile(zipp, 'r')
        zf.extractall(pwd=pwd)
        print('[+] Password : {}'.format(pwd.decode("utf-8")))
        print('[+] File(s) extracted to current directory')
        try:
            print('\nHit CTRL+C to exit...')
            time.sleep(500)
        except KeyboardInterrupt:
            sys.exit()
    except Exception as e:
        print('[-] Wrong password : {}'.format(pwd.decode("utf-8")))

##Coder : luckymonkey666
##Python3.6.4
##Last edit : 19/04/18
    



