class LMcolor:
    CEND      = '\33[0m'
    CBOLD     = '\33[1m'
    CITALIC   = '\33[3m'
    CURL      = '\33[4m'
    CBLINK    = '\33[5m'
    CBLINK2   = '\33[6m'
    CSELECTED = '\33[7m'

    CBLACK  = '\33[30m'
    CRED    = '\33[31m'
    CGREEN  = '\33[32m'
    CYELLOW = '\33[33m'
    CBLUE   = '\33[34m'
    CVIOLET = '\33[35m'
    CBEIGE  = '\33[36m'
    CWHITE  = '\33[37m'

    CBLACKBG  = '\33[40m'
    CREDBG    = '\33[41m'
    CGREENBG  = '\33[42m'
    CYELLOWBG = '\33[43m'
    CBLUEBG   = '\33[44m'
    CVIOLETBG = '\33[45m'
    CBEIGEBG  = '\33[46m'
    CWHITEBG  = '\33[47m'

    CGREY    = '\33[90m'
    CRED2    = '\33[91m'
    CGREEN2  = '\33[92m'
    CYELLOW2 = '\33[93m'
    CBLUE2   = '\33[94m'
    CVIOLET2 = '\33[95m'
    CBEIGE2  = '\33[96m'
    CWHITE2  = '\33[97m'

    CGREYBG    = '\33[100m'
    CREDBG2    = '\33[101m'
    CGREENBG2  = '\33[102m'
    CYELLOWBG2 = '\33[103m'
    CBLUEBG2   = '\33[104m'
    CVIOLETBG2 = '\33[105m'
    CBEIGEBG2  = '\33[106m'
    CWHITEBG2  = '\33[107m'


def strc(text, ltype='Sy', alert='N'):
    color = LMcolor()
    if ltype == 'R':
        header = f'[{color.CGREEN}<{color.CEND}] '
    elif ltype == 'S':
        header = f'[{color.CGREEN}>{color.CEND}] '
    elif ltype == 'Sy':
        header = f'[{color.CGREEN}System{color.CEND}] '
    else:
        raise Exception("Invalid ltype it's ony can by 'R', 'S' or 'Sy'")

    if alert == 'N':
        palert = ''
    elif alert == 'W':
        palert = f'[{color.CWHITE2}WARNING{color.CEND}] '
    elif alert == 'C':
        palert = f'[{color.CREDBG}{color.CWHITE2}CRITICAL{color.CEND}] '
    else:
        raise Exception("Invalid alert it's only can be 'N','W' or 'C'")

    return palert+header+text

def printc(text, ltype='Sy', alert='N'):
    """
        type:   'R' pour les recv
                'S' pour send
                'Sy' pour system
        
        alert:  'N' pour normal
                'W' pour warning
                'C' pour critical

    """
    color = LMcolor()
    if ltype == 'R':
        header = f'[{color.CGREEN}<{color.CEND}] '
    elif ltype == 'S':
        header = f'[{color.CGREEN}>{color.CEND}] '
    elif ltype == 'Sy':
        header = f'[{color.CGREEN}System{color.CEND}] '
    else:
        raise Exception("Invalid ltype it's ony can by 'R', 'S' or 'Sy'")

    if alert == 'N':
        palert = ''
    elif alert == 'W':
        palert = f'[{color.CWHITE2}WARNING{color.CEND}] '
    elif alert == 'C':
        palert = f'[{color.CREDBG}{color.CWHITE2}CRITICAL{color.CEND}] '
    else:
        raise Exception("Invalid alert it's only can be 'N','W' or 'C'")

    print(palert+header+text)

def print_logo():
    print('   __       __     __ \n  |##|     |##\   /##|\n  |##|     |###\ /###|\n  |##|     |##|\#/|##|\n  |##|__   |##|   |##|\n  |#####|  |##|   |##|\n   ‾‾‾‾‾    ‾‾     ‾‾                   ')

