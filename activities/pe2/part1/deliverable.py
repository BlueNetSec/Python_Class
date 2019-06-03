#!/usr/bin/env python3

from utility import *

def encode_pgm(msg, infile, outfile):
    with open(infile,'rb') as fp:
        data = bytearray(fp.read())
    ri = raster_index(date)
    
    msg = bytearray(mag)
    msg.append(128)

    for byt in msg:
        for i in range(7,-1,-1):
            if byt & (1<<i): #get eacch bits within the byte
                data[ri] |= 1
            else:
                data[ri] &= ~1
            ri += 1
    with open(outfile,'wb') as fp:
        fp.write(data)

    '''LSB encodes a message
    Args:
        msg (bytes): bytes object to encode
        infile (str): name of the raw PGM file on disk to use as the cover
        outfile (str): name of the new PGM file to write
    Returns:
        None
    '''
    pass

def decode_pgm(infile):

    msg = bytearray()
    with open(infile,'rb') as fp:
        data = fp.read()
    ri = raster_index(data)

    while True:
        msgbyte = 0
        for shift in range(7,-1,-1):
            msgbyte |=(data[ri] & 1) << shift
            ri +=1
        if msgbyte == 128:
            break
        msg.append(msgbyte)
    return bytes(msg)
    '''LSB decodes a message
    Args:
        infile (str): name of the PGM file to read/decode
    Returns:
        bytes: message that was decoded from the PGM file
    '''
    pass

if __name__ == '__main__':
    pass
