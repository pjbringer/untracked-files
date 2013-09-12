#!/usr/bin/env python3

import codecs
import sys

from gentoolkit.helpers import *
from gentoolkit.package import Package

for pkg in sorted(Package(x) for x in get_installed_cpvs()):
	files = pkg.parsed_contents()
	for file in files:
		print(file)

