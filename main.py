import re


def haha_separator(strng):
    hahas = ['HA', 'ha', 'Ha', 'hA']
    haha = re.split(r'(HA|ha|Ha|hA)',strng)
    return ''.join(haha[x] if haha[x] != '' else ' ' for x in range(len(haha)) )
     
print(haha_separator("Hi, HAHAHAHA! let's go!"))