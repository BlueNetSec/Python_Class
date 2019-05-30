#!/usr/bin/env python3

def steg_encode(msg, cover):
    coverindex = 0
    for char in msg:
        charbin = format(ord(char),'0>8b')
        for index in range(8):
            coverbinl = list(format(int(cover[coverindex]),'0>8b'))
            coverbinl[-1] = charbin[index]
            cover[coverindex] = str(int(''.join(coverbinl),2))
            coverindex += 1
    #print(cover)
    '''LSB encodes a message
    Args:
        msg (str): a string message to encode
        cover (list): list of strings representing integers in the range [0-255]
    Returns:
        None
    '''
    #pass

def steg_decode(stego):
    begin = 0
    end = 8    
    msgbits = []
    for b in stego:
        msgbits.append(bin(int(b))[-1])
    a = ''.join(msgbits)
        
    #print(a)
    #print(type(a))
    loop = int(len(a)/16)
    message = ''
    for index in range(loop+1):
        char = chr(int(a[begin:end],2))
        begin = begin + 8
        end = end + 8
        message = message + char
        #print (char)
    return message
    '''LSB decodes a message
    Args:
        stego (list): list of strings representing integers in the range [0-255]
    Returns:
        str: message that was decoded
    '''
    pass

if __name__ == '__main__':
    #steg_encode('at', [250]*16)
    #steg_decode([250, 251, 251, 250, 250, 250, 250, 251, 250, 251, 251, 251, 250, 251, 250, 250])
    pass
