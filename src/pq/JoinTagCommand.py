
import os
import re
from datetime import date, timedelta
from pq.Command import Command
from pq.Filter import Filter
from pq.Input import Input
from pq.Intervals import Intervals

LOG_DEBUG = 'debug'
LOG_INFO = 'info'
LOG_NONE = 'none'

class JoinTagCommand():

    def __init__(self, input: Input):
        self.__intervals = input.get_intervals()
        self.__filter = Filter(input)
        self.__command = Command(self.__filter)

    def call(self, log=LOG_INFO):
        if log == LOG_DEBUG:
            self.__intervals.print()

        if log == LOG_INFO or log == LOG_DEBUG:
            self.__command.summary("\nBefore join command:")
            self.__join()
            self.__command.summary("After join command:")
        else:
            self.__join()

    def __join(self):
        ids = self.__intervals.get_ids()

        while len(ids) > 0:
            first = ids.pop(0)
            length = len(ids)
            if length > 0:
                next = ids[0]
                join_ids = first + ' ' + next
                self.__command.execute("timew join {ids} :adjust".format(ids=join_ids))
