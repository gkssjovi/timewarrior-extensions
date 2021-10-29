
import os
from pq.Command import Command
from pq.Input import Input
from pq.Interval import Interval
from pq.Intervals import Intervals
from pq.Filter import Filter

LOG_DEBUG = 'debug'
LOG_INFO = 'info'
LOG_NONE = 'none'

class CollapseCommand():

    def __init__(self, input: Input):
        self.__intervals = input.get_intervals()
        self.__filter = Filter(input)

    def call(self, log=LOG_INFO):
        command = Command(self.__filter)
        intervals = self.__intervals

        if log == LOG_DEBUG:
            self.__intervals.print()

        last_interval = intervals.get_last_close()

        if last_interval:

            if len(intervals.get()) == 1 and (log == LOG_INFO or log == LOG_DEBUG):
                command.summary("\nThere is only one record:")
                return None

            last_end = last_interval.get_end()
            start = last_end - intervals.get_diff()
            interval = Interval(last_interval.id, start, last_end, intervals.get_tags(), intervals.get_annotation(True))

            delete_intervals_ids = []

            for item in intervals.get():
                if item.id == last_interval.id:
                    break
                delete_intervals_ids.append(item.get_id())

            if log == LOG_INFO or log == LOG_DEBUG:
                command.summary("\nBefore collapse command:")

            if len(delete_intervals_ids) > 0:
                join_ids = ' '.join(delete_intervals_ids).rstrip()
                command.execute("timew delete {ids}".format(ids=join_ids))

            command.execute("timew tag {id} {tags}".format(
                id=interval.get_id(),
                tags=' '.join(interval.get_tags())
            ))

            if interval.get_annotation():
                command.execute("timew annotate {id} {annotation}".format(
                    id=interval.get_id(),
                    annotation=interval.get_annotation()
                ))

            command.execute("timew modify start {id} {start_date} :adjust".format(
                id=interval.get_id(),
                start_date=interval.get_start().isoformat()
            ))

            if log == LOG_INFO or log == LOG_DEBUG:
                command.summary("After collapse command:")

        else:
            print('There are no records to collapse', end='')

        return None
