#!/usr/bin/env python3

import sys

from pq.Input import Input
from pq.JoinTagCommand import JoinTagCommand, LOG_DEBUG, LOG_INFO, LOG_NONE

input = Input(sys.stdin)
jointag = JoinTagCommand(input)

jointag.call(log=LOG_INFO)
