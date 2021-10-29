#!/usr/bin/env python3

import sys

from pq.Input import Input
from pq.IdsCommand import IdsCommand

input = Input(sys.stdin)
pqids = IdsCommand(input)

pqids.output()

