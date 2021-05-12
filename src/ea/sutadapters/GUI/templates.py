#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ------------------------------------------------------------------
# MIT License
#
# Copyright (c) 2010-2021 Denis MACHARD
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# -------------------------------------------------------------------

import sys

from ea.testexecutorlib import TestValidatorsLib
from ea.testexecutorlib import TestTemplatesLib
from ea.testexecutorlib import TestOperatorsLib
from ea.testexecutorlib import TestAdapterLib

# templates for gui client
def gui(more=None, action=None, actionId=None, description=None,
        result=None, text=None, length=None,
        img=None, mainImg=None, mainLength=None, countResult=None, 
        textResult=None, value=None, parameters=None,
        x=None, y=None, steps=None, repeat=None, out=None, state=None):
	"""
	Construct a template for a gui event
	"""
	tpl = TestTemplatesLib.TemplateLayer('GUI')

	# add additional keys
	if more is not None:
		tpl.addMore(more=more)
		
	if state is not None:
		tpl.addKey(name='state', data=state )
		
	if out is not None:
		tpl.addKey(name='out', data=out )
		
	if x is not None:
		tpl.addKey(name='x', data=x )
		
	if y is not None:
		tpl.addKey(name='y', data=y )
		
	if steps is not None:
		tpl.addKey(name='steps', data=steps )
		
	if repeat is not None:
		tpl.addKey(name='repeat', data=repeat )
		
	if action is not None:
		tpl.addKey(name='action', data=action )

	if actionId is not None:
		tpl.addKey(name='action-id', data=actionId )
		
	if description is not None:
		tpl.addKey(name='description', data=description )

	if text is not None:
		tpl.addKey(name='txt', data=text )
		
	if result is not None:
		tpl.addKey(name='result', data=result )

	if countResult is not None:
		tpl.addKey(name='count-result', data=countResult )
	
	if textResult is not None:
		tpl.addKey(name='text-result', data=textResult )
		
	if length is not None:
		tpl.addKey(name='length', data=length )

	if img is not None:
		tpl.addKey(name='img', data=img )

	if mainImg is not None:
		tpl.addKey(name='main-img', data=mainImg )

	if mainLength is not None:
		tpl.addKey(name='main-length', data=mainLength )

	if value is not None:
		tpl.addKey(name='value', data=value )

	if parameters is not None:
		tpl.addKey(name='parameters', data=parameters )
	return tpl