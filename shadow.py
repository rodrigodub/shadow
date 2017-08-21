#! /usr/bin/python3

#################################################
#                   Shadow
# Python application to create an HTML file
# from all files in a directory
#
# v0.1.04
# for Issue #5
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
    Usage:
        f = ShProcess(dir, title)
    where
        dir: directory, as string
        title: HTML <title> and file name, as string
    """
    def __init__(self, direct, titulo):
        self.directory = direct
        self.title = titulo
        self.contents = os.listdir(self.directory)
        self.output()

    def __str__(self):
        return 'This is an object to write the contents of [{}] as an HTML file.'.format(self.directory)

    def output(self):
        f = open('{}/{}.html'.format(self.directory, self.title), 'w')
        f.write('<html>')
        f.write('    <head>')
        f.write('        <title>')
        f.write('        {}'.format(self.title))
        f.write('        </title>')
        f.write('    </head>')
        f.write('    <body>')
        f.write('        <h1>')
        f.write('        {}'.format(self.title))
        f.write('        </h1>')
        f.write('        </br>')
        for i in self.contents:
            if '.html' not in i:
                f.write('        <p><img src="{}" width="800px"/></br>'.format(i))
                f.write('        <small>{}</small></p>'.format(i))
                f.write('        </br>')
        f.write('    </body>')
        f.write('</html>')
        f.close()


# test loop
def test():
    print('------------------------')
    print('Test.')
    print('------------------------')
    d = input('Enter directory: ')
    t = input('Enter the file title: ')
    a = ShProcess(d, t)
    # print(a)
    # print('Contents:\n')
    # [print(i) for i in a.contents]
    print('Done.')


# main loop
def main():
    print('------------------------')
    print('Main.')
    print('------------------------')


# main, calling main loop
if __name__ == '__main__':
    test()
    # main()
