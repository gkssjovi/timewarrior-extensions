
from sys import intern
from pq.Input import Input
from pq.Intervals import Intervals

class IdsCommand():

    def __init__(self, input: Input):
        self.__intervals = input.get_intervals()

    def get(self):
        return self.__intervals.get_ids()

    def get_join(self):
        return self.__intervals.get_ids_join()

    def output(self):
        print(self.get_join(), end='')
