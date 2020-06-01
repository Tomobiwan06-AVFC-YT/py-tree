import sys
import time

'''
Initial code sourced from Casey Neale,
adapted (with permission) by Tom Dillon for
use as an importable script.
'''

def slow_print(s, timer):
  for c in s:
    sys.stdout.write( '%s' % c )
    sys.stdout.flush()
    time.sleep(timer)

