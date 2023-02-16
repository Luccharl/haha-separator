import re

def haha_separator(strng):
    haha = re.split(r'(HA|ha|Ha|hA)',strng)
    return ''.join(haha[x] if haha[x] != '' else ' ' for x in range(len(haha)))
     
strng = input()
print(haha_separator(strng))