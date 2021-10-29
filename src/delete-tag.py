#!/usr/bin/env python3

import sys
from pq.DeleteTagCommand import DeleteTagCommand, LOG_INFO, LOG_DEBUG, LOG_NONE

from pq.Input import Input

input = Input(sys.stdin)
delete_tag = DeleteTagCommand(input)

delete_tag.call(log=LOG_INFO)
