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

"""		wikiLine
	lineChar		: [\x20..\x7e]
	rawChar			: [\x20..\x7e  !!/!_]
	DISTINCT		: "//"								: drop
	IMPORTANT		: "!!"								: drop
	MONOSPACE		: "__"								: drop
	rawText			: rawChar+							: join
	distinctText	: DISTINCT inline DISTINCT			: liftValue
	importantText	: IMPORTANT inline IMPORTANT		: liftValue
	monospaceText	: MONOSPACE inline MONOSPACE		: liftValue
	styledText		: distinctText / importantText / monospaceText
	text			: styledText / rawText
	inline			: @ text+

"""

from pijnu import *

# title: wikiLine
inline = Recursion()
lineChar = Klass(' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~')
rawChar = Klass(' "#$%&\'()*+,-.0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^`abcdefghijklmnopqrstuvwxyz{|}~  ')
DISTINCT = Word('//')(drop)
IMPORTANT = Word('!!')(drop)
MONOSPACE = Word('__')(drop)
rawText = OneOrMore(rawChar)(join)
distinctText = Sequence(DISTINCT, inline, DISTINCT)(liftValue)
importantText = Sequence(IMPORTANT, inline, IMPORTANT)(liftValue)
monospaceText = Sequence(MONOSPACE, inline, MONOSPACE)(liftValue)
styledText = Choice(distinctText, importantText, monospaceText)
text = Choice(styledText, rawText)
inline **= OneOrMore(text)

parser = Parser('wikiLine', locals(), 'inline')
