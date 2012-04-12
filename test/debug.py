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
Minimal test/debug sample
'''

"""
<definition>
SEP			: ' '						: drop
DOT			: '.'
digit		: [0..9]
integer		: digit+					: join
real		: integer DOT integer?		: join
number		: real / integer			: toReal
moreNum		: SEP number				: liftNode
numbers		: number (moreNum)*			: extract

"""

from pijnu import *

# with recursive patterns


### title: debug ###
###   <toolset>
def toReal(node):
    node.value = float(node.value)

###   <definition>
SEP = Char(' ', format="' '")(drop)
DOT = Char('.', format="'.'")
digit = Klass(format='[0..9]', charset='0123456789')
integer = Repetition(digit, numMin=1, numMax=False, format='digit+')(join)
real = Sequence([integer, DOT, Option(integer, format='integer?')], format='integer DOT integer?')(join)
number = Choice([real, integer], format='real / integer')(toReal)
moreNum = Sequence([SEP, number], format='SEP number')(liftNode)
numbers = Sequence([number, Repetition(copy(moreNum), numMin=False, numMax=False, format='(moreNum)*')], format='number (moreNum)*')(extract)

debugParser = Parser(locals(), 'numbers', 'debug', 'debug.py')
