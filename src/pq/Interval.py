from typing import List
import dateutil
from dateutil import parser
from dateutil.tz import tz
from datetime import datetime, date, timedelta

class Interval(object):
    def __init__(self, id, start, end, tags, annotation):
        self.id = id
        self.start = start
        self.end = end
        self.tags = tags
        self.annotation = annotation
        
    def get_id(self):
        return '@' + str(self.id)
    
    def get_start(self):
        return self.__get_local_datetime(self.start)
    
    def get_end(self):
        return self.__get_local_datetime(self.end) if self.end is not None else None
    
    def get_tags(self) -> List[str]:
        return self.tags

    def get_tags_string(self) -> str:
        tags = self.get_tags()
        tags_string = ''
        for tag in tags:
            tag = tag.replace("'", "\\'")
            if ' ' in tag:
                tag = f"'{tag}'" 
            tags_string += tag + ' '

        return tags_string.rstrip()

    def get_annotation(self):
        return self.annotation

    def get_duration(self):
        if self.is_open():
            return datetime.now(tz=tz.tzlocal()) - self.get_start()
        else:
            return self.get_end() - self.get_start()

    def get_diff(self):
        start = self.get_start()
        end = self.get_start() if self.is_open() else self.get_end()
        diff = end - start
        return diff
    
    def is_open(self):
        return self.end is None

    def __get_local_datetime(self, datetime_input):
        if type(datetime_input) is str:
            local_datetime = parser.parse(datetime_input)
        elif type(datetime_input) is datetime:
            if datetime_input.tzinfo is None:
                local_datetime = datetime_input.replace(tzinfo=tz.tzutc())
            else:
                local_datetime = datetime_input

        else:
            raise TypeError("Unknown type for datetime input: {}".format(type(datetime_input)))

        return local_datetime.astimezone(tz.tzlocal())
