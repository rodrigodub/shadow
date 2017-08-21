#! /usr/bin/python3

#################################################
#                   Shadow
# Python application to create an HTML file
# from all files in a directory
#
# v0.1.01
# for Issue #1
#
# Rodrigo Nobrega
# 20170821-
#################################################
__author__ = 'Rodrigo Nobrega'


# import modules
import os


# ShProcess()
class ShProcess(object):
    """
    Class to process the directory contents
    """
    def __init__(self, dir):
        self.directory = dir

    def __str__(self):
        return 'This is an object to write the contents of [{}] as an HTML file.'.format(self.directory)


# test loop
def test():
    print('------------------------')
    print('Test.')
    print('------------------------')
    d = input('Enter directory: ')
    a = ShProcess(d)
    print(a)


# main loop
def main():
    print('------------------------')
    print('Main.')
    print('------------------------')


# main, calling main loop
if __name__ == '__main__':
    test()
    # main()
