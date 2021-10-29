import io
import json
import re

from pq.Config import Config
from pq.Intervals import Intervals

class Input():

    def __init__(self, stdin):
        stdin_string = ''
        stdin_json = ''
        stdin_config = ''
        config = {}
        json_started = False
        for line in stdin:
            stdin_string += line

            if json_started:
                stdin_json += line

            if line == u'\x0A':
                json_started = True

            if not json_started:
                stdin_config += line
                m = re.search('^([^:]+):( (.*))?$', line, re.MULTILINE)
                config[m.group(1)] = m.group(3) if m.group(2) is not None else ""

        self.__content = stdin_string
        self.__json_content = stdin_json
        self.__config_content = stdin_config
        self.__intervals_json = json.loads(self.__json_content)
        self.__config = Config(config)
        self.__intervals = Intervals(self.__intervals_json)

    def get_json_content(self) -> str:
        return self.__json_content

    def get_config_content(self) -> str:
        return self.__config_content

    def get_content(self) -> str:
        return self.__content

    def get_intervals_json(self) -> dict:
        return self.__intervals_json

    def get_config(self) -> Config:
        return self.__config

    def get_intervals(self) -> Intervals:
        return self.__intervals

    def create_stream(self) -> str:
        return io.StringIO(self.__content)
