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

"""
<definition>
item		: '1'
SEP			: ','
itemList	: item  (SEP item)*	: intoList

"""

from pijnu import *

### title: itemList ###
###   <definition>
item = Char('1', format="'1'")
SEP = Char(',', format="','")
itemList = Sequence([item, Repetition(Sequence([SEP, item], format='SEP item'), numMin=False,numMax=False, format='(SEP item)*')], format='item  (SEP item)*')(intoList)

itemListParser = Parser(vars(), 'itemList', 'itemList', 'None')
