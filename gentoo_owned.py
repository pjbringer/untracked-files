#!/usr/bin/env python2

import codecs
import sys

UTF8Writer = codecs.getwriter('utf-8')
sys.stdout = UTF8Writer(sys.stdout)

from gentoolkit.helpers import *
from gentoolkit.package import Package

for pkg in sorted(Package(x) for x in get_installed_cpvs()):
	files = pkg.parsed_contents()
	for file in files:
		print file

