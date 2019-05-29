#!/usr/bin/env python3


def steg_encode_char(char, cover):
    
    index = 0
    key_index = 0    
    key = format(ord(char),'0>8b')
    
    
    binlist = cover[:]
    index = 0
    final_list = []    
    for element in binlist:
        binary = list(format((binlist[index]),'0>8b'))
        binary[-1] = key[key_index]
   
        
        final_list.append(str(int(''.join(binary),2)))
        index = index + 1
        key_index = key_index + 1
    return final_list

    '''LSB encodes a character
    Args:
        char (str): a single character string
        cover (list): list of 8 strings representing integers in the range [0-255]
    Returns:
        None
    '''
    pass

def steg_decode_char(stego):
    msgbits = []
    index = 0
    for element in stego:
        finalbit = list(format((stego[index]),'0>8b'))[-1]
        msgbits.append(finalbit)
        index = index + 1
    key = chr(int(''.join(msgbits),2))
    return key
    '''LSB decodes a character
    Args:
        stego (list): list of 8 strings representing integers in the range [0-255]
    Returns:
        str: character that was decoded
    '''
    pass

if __name__ == '__main__':
    a = steg_encode_char('a',[250,251,252,251,250,249,248,249])
    b = steg_decode_char([250, 251, 253, 250, 250, 248, 248, 249])
    print(a)
    print(b)    
    pass
