
import os
from pq.Command import Command
from pq.Input import Input
from pq.Intervals import Intervals
from pq.Filter import Filter

LOG_DEBUG = 'debug'
LOG_INFO = 'info'
LOG_NONE = 'none'

class DeleteTagCommand():

    def __init__(self, input: Input):
        self.__intervals = input.get_intervals()
        self.__filter = Filter(input)
        self.__command = Command(self.__filter)

    def call(self, log=LOG_INFO):
        ids = self.__intervals.get_ids()

        if len(ids) == 0:
            print('No records found for delete', end='')
            return None

        if log == LOG_DEBUG:
            self.__intervals.print()

        if log == LOG_INFO or log == LOG_DEBUG:
            self.__command.summary("\nBefore delete command:")
            self.__delete()
        else:
            self.__delete()

    def __delete(self):
        join_ids = self.__intervals.get_ids_join()
        self.__command.execute("timew delete {ids}".format(ids=join_ids))
