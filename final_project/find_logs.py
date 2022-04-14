#!/usr/bin/env python3

import re
import sys

line = "May 27 11:45:40 ubuntu.local ticky: ERROR: Error creating ticket [#1234] (kiquetal)"
print(line)
success = re.search(r"ticky: INFO: ([\w ]*) ",line)
if success is not None:
    print(success[1])
error = re.search(r"ticky: ERROR: ([\w ]*).*(\(\w+\))$",line)
print(error[1])
print(re.sub('[\(\)]','',error[2]))

