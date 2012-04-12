# -*- coding: utf8 -*-

'''
Copyright 2009 Denis Derman <denis.spir@gmail.com> (former developer)
Copyright 2011-2012 Peter Potrowl <peter017@gmail.com> (current developer)

This file is part of Pijnu.

Pijnu is free software: you can redistribute it and/or modify it
under the terms of the GNU Lesser General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Pijnu is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public
License along with Pijnu.  If not, see <http://www.gnu.org/licenses/>.
'''

'''
Pijnu command-line parser generator

A helper to generate a Python parser from a grammar, on the command line.
Avoids writing Python code to do that; also may be handy for end-users.

Call format:
    python gen.py grammarFileName  [parserFileName]

If parserFileName is not given, the parser is written into
    grammarTitle + "Parser.py"

'''

### import/export
from pijnu.generator import makeParser
from sys import argv as arguments
from pijnu.library.tools import *


def do():
    ''' write parser from grammar '''
    # get source grammar from command line argument
    try:
        grammar = file(arguments[1], 'r').read()
    except IndexError:
        message = ("\nCall Format:\n"
                   "\tpython gen.py grammar_file_name\n"
                   "or\n"
                   "\tpython gen.py grammar_file_name  parserFileName\n\n"
                   )
        write(message)
        end()
    # write parser into target file
    try:
        parserFile = file(arguments[2], 'w')
        makeParser(grammar, parserFile)
    except Exception:
        makeParser(grammar)

if __name__ == "__main__":
    do()
