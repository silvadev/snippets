#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, random

try:
	ni,nf = sys.argv[1],sys.argv[2]
	print random.choice(range(int(ni),int(nf)+1))
except:
	print u"Use: python aleatorio.py <faixa inicial> <faixa final>\nEx.: python aleatorio.py -5 8"
