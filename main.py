#
#Cre: dtbao20
#
from unicodedata import normalize, combining
import keyboard
import re
list_key = ""

def _converter():
    global list_key
    if not len(list_key)>1: return
    u = ''

    txt = list_key.lower()

    txt = normalize("NFKD", txt)
    txt = ''.join([c for c in txt if not combining(c)])

    check = re.search("^(ngh|ch|gh|kh|ng|nh|gi|ph|th|tr|đ)|^[^aeiouwfjz]", txt)
    if check: index = check.span()[1]
    else:
        check = re.search("[aeiou]", txt)
        index = check.span()[0]

    PHU = list_key[:index]
    VAN = list_key[index:]
    phu = txt[:index]
    van = txt[index:]
    print(phu, van)
    if not van: return
    ivan = -1
    # if len(van)>1 and van[-2] in 'aeiou': ivan = -2
    # if len(van)>2 and van[-3] in 'aeiou': ivan = -3
    # if len(van)>3 and van[-4] in 'aeiou': ivan = -4
    # if len(van)>3 and van[-3] in 'aeiou': ivan = -3
    if len(van)>1 and re.search("[aeiouwsfrjx]",van): ivan = -2
    if len(van)>2 and re.search("[aeiouwsfrjx]",van): ivan = -3
    if len(van)>2 and re.search("[aeiouwsfrjx]",van) and VAN[-2].lower()!=van[-2]: ivan = -2
    if len(van)>3 and re.search("ch|ng|nh",van): ivan = -4

    char_van = van[ivan]

    if len(van)>2 and van[-1]==van[-2] and van[-2] in 'aeo': 
        ivan = -2
        u = '\u0302'
    if van[-1]==char_van and char_van in 'aeo' and len(van)>1: u = '\u0302'
    if van[-1]=='w' and char_van in 'ou': u = '\u031B'
    if van[-1]=='w' and char_van in 'a': u = '\u0306'

    # if list_key[-1]=='f': u = '\u0300'
    # if list_key[-1]=='s': u = '\u0301'
    # if list_key[-1]=='x': u = '\u0303'
    # if list_key[-1]=='r': u = '\u0309'
    # if list_key[-1]=='j': u = '\u0323'
    [u:='\u0300\u0301\u0303\u0309\u0323'[i] for i in range(5) if van[-1]=='fsxrj'[i]]

    # fix bug change mark more times
    Lvan = list(normalize("NFKD", VAN[ivan]))
    if len(Lvan)==2: VAN = VAN[:ivan] + Lvan[0] + VAN[ivan+1:]

    char = VAN[ivan] + u
    # print(PHU)
    # print(list_key)
    if not u: 
        if list_key[-2:].lower()=='dd': 
            if list_key[-2]=='d': list_key = 'đ'
            elif list_key[-2]=='D': list_key = 'Đ'
            keyboard.write("\b\b"+list_key)
            print(list_key)
        return

    char = normalize("NFC", char)
    VAN = list(VAN)
    VAN[ivan] = char
    if u: VAN = VAN[:-1]
    VAN = "".join(VAN)
    list_key = PHU + VAN
    keyboard.write("\b"*(len(VAN)+1) + VAN)
    # print("->",list_key, char, ivan, VAN)
"""

"""
while True:
    event = keyboard.read_event()
    key = event.name
    if event.event_type == keyboard.KEY_DOWN:
        if key.isalpha() and len(key)==1: list_key += key
        elif key=='shift': pass
        elif key=='backspace': list_key = list_key[:-1]
        else: list_key = ""
        # print(">>",key, list_key)
        # print(list_key)
        _converter()


