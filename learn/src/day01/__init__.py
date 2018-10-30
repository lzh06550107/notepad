#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Function:
【记录】使用Python的IDE：Eclipse+PyDev
http://www.crifan.com/try_with_python_ide_eclipse_pydev

Author:     Crifan Li
Version:    2012-12-29
Contact:    admin at crifan dot com
"""
from tkinter.constants import MULTIPLE
from pickle import FALSE

SUFFIXES = {1000:['KB','MB','GB','TB','PB','EB','ZB','YB'],
            1024:['KiB','MiB','GiB','TiB','PiB','EiB','ZiB','YiB']}

def approximate_size(size, a_kilobyte_is_1024_byte=True):
    '''
        Convert a file size to human-readable form.
        
        Keyword arguments:
        size --fiel size in bytes
        a_kilobyte_is_1024_byte -- if True(default),use multiples of 1024
                                   if Flase,use multiples of 1000
        
        Returns: string
        
    '''
    if size < 0:
        raise ValueError('number must be non-negative')
    multiple = 1024 if a_kilobyte_is_1024_byte else 1000
    for suffix in SUFFIXES[multiple]:
        size /= multiple
        if size < multiple:
            return '{0:.1f} {1}'.format(size, suffix)
    
    raise ValueError('number too large')    

if __name__ == '__main__':
    print(approximate_size(100000000000,False))
    print(approximate_size(100000000000))
    
        

