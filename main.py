import re

def haha_separator(strng):
    haha = re.split(r'(HA|ha|Ha|hA)',strng)
    return ''.join(haha[x] if haha[x] != '' else ' ' for x in range(len(haha)))

try:
    while True:     
        strng = input("Enter your message: ")
        print(haha_separator(strng))
except KeyboardInterrupt:
    exit()