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
Simple test profiler -- just case needed
'''

from pijnu import makeParser


def parseTest():
    numbersTransformGrammar = """\
numbersTransform
<toolset>
def toReal(node):
	node.value = float(node.value)
<definition>
SEP			: ' '						: drop
DOT			: '.'
digit		: [0..9]
integer		: digit+					: join
real		: integer DOT integer?		: join
number		: real / integer			: toReal
addedNum	: SEP number				: liftNode
numbers		: number (addedNum)*		: extract
"""
    makeParser(numbersTransformGrammar)


def profile(command, logFile):
    import cProfile
    import pstats
    ruler = 33 * "="
    # run with profiler & timer
    cProfile.run(command, logFile)
    print ruler
    ps = pstats.Stats(logFile)
#~  ps.strip_dirs()
    ps.sort_stats("time")
    ps.print_stats(11)
    print ruler

profile("parseTest()", "testProfileStats")
