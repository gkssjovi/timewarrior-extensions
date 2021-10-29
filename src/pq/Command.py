import os

from pq.Filter import Filter

class Command():
    def __init__(self, filter: Filter) -> None:
        self.__filter = filter

    def execute(self, command):
        os.system(self.__filter.summary_command(True))
        os.system(command)

    def summary(self, label: str, sync=False):
        if sync:
            os.system("echo '{label}'".format(
                label=label.replace("'", "\'")
            ))
            os.system(self.__filter.summary_command(False))
        else:
            stream = os.popen(self.__filter.summary_command(False))
            output = stream.read()
            print(label)
            print(output.rstrip())
