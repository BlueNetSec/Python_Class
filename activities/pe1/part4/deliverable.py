#!/usr/bin/env python3

def read_pgm(filename):
    with open(filename) as fp:
        data = fp.read()
    data = data.split()
    #header = data[:4]
    #pixel = data[4:]
    return(data[:4],data[4:])
    #print(header)    
        
    #return result
    #return (tuple(header,pixel))

    #print(pixel)
    #print (data[0:])
    #print(type(data))
    #print(data)
    '''Reads a PGM file
    Args:
        filename (str): the file name of a PGM file on disk to read from
    Returns:
        tuple:
            1st element is a list of PGM header values as strings
            2nd element is a list of pixel intensities as strings
    '''
    pass

def write_pgm(filename,content):
    with open(filename,'w') as fp:
        #for p in content[0]+content[1]
            #fp.write('{}\n'.format(p))
        fp.write('\n'.join(content[0]+content[1]))
    '''Writes a PGM file
    Args:
        filename (str): the file name to be used for the written file
        content (tuple):
            1st element is a list of PGM header values as strings
            2nd element is a list of pixel intensities as strings
    Returns:
        None
    '''
    pass

def invert(content):
    for pi in range(len(content[1])):
        content[1][pi] = str(255 - int(content[1][pi]))
    '''Modifies the pixel intensities of the given content to be inverted
    Args:
        content (tuple):
            1st element is a list of PGM header values as strings
            2nd element is a list of pixel intensities as strings
    Returns:
        None
    '''
    pass

if __name__ == '__main__':
    #read_pgm('plain.pgm')	
    pass
