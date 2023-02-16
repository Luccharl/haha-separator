import re
def haha_separator(strng):
    lst = []
    hahas = ['HA','ha', 'Ha', 'hA']
    haha = re.split(r'(HA|ha|Ha|hA)',strng)
    for x in haha:
        if x in hahas:
            lst.append(f'{x} ')
        else:
            lst.append(x)
    return ''.join(lst).strip()
    
print(haha_separator('HAHAHAhaHAHAHahAha'))