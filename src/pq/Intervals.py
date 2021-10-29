
from typing import List
from pq.Interval import Interval
import datetime


class Intervals():

    def __init__(self, intervals_json: dict):
        self.__intervals_json = intervals_json
        intervlas = []
        
        for item in self.__intervals_json:
            intervlas.append(Interval(
                item['id'],
                item['start'],
                item['end'] if 'end' in item else None,
                item['tags'] if 'tags' in item else [],
                item['annotation'] if 'annotation' in item else None
            ))
        
        self.__intervals = intervlas

    def get(self):
        return self.__intervals

    def get_json(self):
        return self.__intervals_json

    def get_ids(self):
        ids = []
        for line in self.__intervals_json:
            id = '@' + str(line['id'])
            ids.append(id)

        return ids
    
    def get_diff(self):
        total = datetime.timedelta(0, 0, 0)

        for interval in self.__intervals:
            total += interval.get_diff()

        return total
    
    def get_last_close(self):
        for interval in reversed(self.__intervals):
            if not interval.is_open():
                return interval

        return None
    
    def get_annotation(self, last=True):
        intervals = reversed(self.__intervals) if last else self.__intervals

        for interval in intervals:
            annotation = interval.get_annotation()
            if annotation is not None:
                return annotation

        return None
            
    def get_tags(self) -> List[str]:
        tags = []

        for interval in self.__intervals:
            for tag in interval.get_tags():
                if tag not in tags:
                    tags.append(tag)

        return tags

    def get_tags_string(self) -> str:
        tags = self.get_tags()
        tags_string = ''
        for tag in tags:
            tag = tag.replace("'", "\\'")
            if ' ' in tag:
                tag = f"'{tag}'" 
            tags_string += tag + ' '

        return tags_string.rstrip()

    def get_ids_join(self):
        ids_join = ''

        for id in self.get_ids():
            ids_join += id + ' '

        return ids_join.rstrip()
    
    def print(self):
        print('\nIntervals list:', end='\n\n')
        for line in self.__intervals_json:
            print(line)
