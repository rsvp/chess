#!/usr/bin/env python
#  vim: set fileencoding=utf-8 ff=unix tw=78 ai syn=python : per PEP 0263 
#        python 2.7.13 under Linux Ubuntu 14.04.5     Date : 2017-08-21
#  [/] - Cross-platform code compatible with python2.7 and python3.
''' 
_______________|  chess_quote.py : Random chess quote

       Examples:  $ python chess_quote.py  # Either python2.7 or python3
                  $ ./chess_quote.py       # As shell command

   Dependencies:  Maxims from https://git.io/chess

CHANGE LOG  For latest version, see https://github.com/rsvp/chess
2017-08-21  First version in Python, without regex filtration.
'''

from __future__ import absolute_import, print_function, division
import random
 
try:
    from urllib.request import urlopen
    #    ^for python3 
except ImportError:
    from urllib2 import urlopen
    #    ^for python2 


def url2list( URL ):
    '''Retrieve content from URL, and convert to list of UTF-8 lines.'''
    content = urlopen( URL )
    return [linebyte.decode('utf-8').rstrip('\r\n') for linebyte in content]


def get_maxims():
    '''From README.md extract the maxims into a list.'''
    readme = url2list('https://git.io/chessraw')
    return [ line for line in readme if line.startswith('* ') ]


def main():
    '''Do that thing! Do that thing! --Tuco'''
    ranmaxim = random.choice( get_maxims() )
    #                ^Only a single choice is available.
    #  Note: numpy.random.choice can return multiple random lines,
    #  however, for casual users the numpy package would be overkill here.
    print( ranmaxim.replace('* ', '', 1) )


if __name__ == "__main__":
    main()

