#!/usr/bin/env python3

import sys
from pq.CollapseCommand import CollapseCommand, LOG_INFO, LOG_DEBUG, LOG_NONE

from pq.Input import Input

input = Input(sys.stdin)
collapse = CollapseCommand(input)

collapse.call(log=LOG_INFO)
