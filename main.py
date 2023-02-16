import re

#return ''.join(x + ' ' if x in hahas else x for x in haha)


def hahas_separator(strng):
    hahas = ['HA', 'ha', 'Ha', 'hA']
    haha = re.split(r'(HA|ha|Ha|hA)',strng)
    for x in range(len(haha)):
        if haha[x] is '':
            haha[x] = ' '
    return ''.join(haha)
     
print(hahas_separator("Hi, HAHAHAHA! let's go!"))