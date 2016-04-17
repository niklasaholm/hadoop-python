#!/usr/bin/env python

import sys

# input lines come STDIN
for line in sys.stdin:
  # remove leading and trailing whitespaces
  line = line.strip()
  # split the linp into words
  words = line.split()
  # increase counters

  for word in words:

    print '%s\t%s'  % (word, 1)
