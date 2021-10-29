
import re
from datetime import date, timedelta

from pq.Input import Input

class Filter():

    def __init__(self, input: Input):
        self.__config = input.get_config()
        self.__intervals = input.get_intervals().get()
        
    def summary_command(self, silent=False) -> str:
        return "timew summary {tags} {interval_date} :ids {silent}".format(
            tags=self.get_tags(),
            interval_date=self.get_interval_date(),
            silent=(" > /dev/null" if silent else '')
        )

    def get_tags(self):
        tags = self.__config.get_value('temp.report.tags', '')
        tags_string = ''

        if tags != '':
            tmp_tags = re.split(r',(?=")', tags)

            if len(tmp_tags) == 1:
                tags_string = "'" + tags + "'"
            else:
                for i in range(0, len(tmp_tags)):
                    tmp_tags[i] = tmp_tags[i].replace(',', ' ')
                tags_string = ' '.join(map(str, tmp_tags))

        return tags_string

    def get_interval_date(self):
        intervals = self.__intervals
        intervals_len = len(intervals)

        interval_date = ''
        if intervals_len > 1:
            start_date = intervals[0].get_start().isoformat()
            last_interval = intervals[intervals_len - 1]
            end_date = last_interval.get_end().isoformat() if last_interval.is_open() is False else (date.today() + timedelta(days=1)).isoformat()
            interval_date = start_date + ' - ' + end_date
        elif intervals_len == 1:
            start_date = intervals[0].get_start().isoformat()
            last_interval = intervals[0]
            end_date = last_interval.get_end().isoformat() if last_interval.is_open() is False else (date.today() + timedelta(days=1)).isoformat()
            interval_date = start_date + ' - ' + end_date
        return interval_date
