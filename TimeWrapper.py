#!/usr/bin/env python
#
# Kenny Kirtland
# @2015
#
# Time Wrapper - used to break dependencies on the time module
#
#

import time

class TimeWrapper(object):
    def __init__(self):
        pass

    def sleep(self, delay):
        time.sleep(delay)
