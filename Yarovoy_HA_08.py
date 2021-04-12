from datetime import datetime
from typing import Union
import sys
import json


class LogMessageCreator():

    def level_to_str(self, level):
        return levels[level - 1]

    def append_log_message(self, level, msg, *args, **kwargs):
        datetimenow_formatted = datetime.now(tz=None).strftime("%Y-%m-%d %H:%M:%S")
        self.log.append(f'{datetimenow_formatted} - {self.level_to_str(level)} - {msg}'
                        f'\n')
        self.last_row += 1

    def return_log(self, row=None):
        if row != None:
            return self.log[row-1]
        return self.log


# Log levels:
INFO = 1
WARNING = 2
ERROR = 3
levels = ['INFO', 'WARNING', 'ERROR']

# type of logger:
TO_STDOUT = 1
TO_FILE = 2
types = ['TO_STDOUT', 'TO_FILE']

class Logger(LogMessageCreator):

    def __init__(
            self,
            name: str = "LOGGER",
            level=INFO,
            init_msg: str = 'Logger started',
            type_of = TO_FILE,                     #TO_FILE, TO_STDOUT,
            filename: str ='log.json',
            buffer_length: int = 10):

        LogMessageCreator.__init__(self)
        self.log = []
        self.last_row = 0
        self.logger_name = name
        self.level = self._checkLevel(level)
        self.type_of = self._checkType(type_of)
        self.log_filename = filename
        self.buffer_length = buffer_length
        self.row_counter = 0
        self.filename_message = f'The log file is "{self.log_filename}" '
        if self.type_of == TO_STDOUT:
            self.filename_message = ""

        self.append_log_message(msg=f'{init_msg}, the type of log is "{self.type_of_to_str()}". '
                                    f'The level is "{self.level_to_str(self.level)}". {self.filename_message}'

                                , level=INFO)
        self.show_last_log_message()

    def type_of_to_str(self):
        return types[self.type_of - 1]

    def show_last_log_message(self):
        sys.stdout.write(''.join([str(elem) for elem in (self.return_log(self.last_row))]))

    def _checkLevel(self, level):
        if not isinstance(level, int) or level <= 0 or level > 3:
            raise TypeError("level must be an integer \
                            and it should be between 1 and 3")
        else:
            return level

    def _checkType(self, type_of):
        if not isinstance(type_of, int) or type_of <= 0 or type_of > 2:
            raise TypeError("type must be an integer \
                            and it should be between 1 and 2")
        else:
            return type_of

    def warning(self, msg, *args, **kwargs):
        self.append_log_message(WARNING, msg, args, **kwargs)
        self.send_log_to_out()

    def error(self, msg, *args, **kwargs):
        self.append_log_message(ERROR, msg, args, **kwargs)
        self.send_log_to_out()

    def info(self, msg, *args, **kwargs):
        self.append_log_message(INFO, msg, args, **kwargs)
        self.send_log_to_out()

    def send_log_to_out(self):
        if self.type_of == TO_STDOUT:
            self.show_last_log_message()

        if self.type_of == TO_FILE:
            if self.row_counter == self.buffer_length:
                with open(self.log_filename, 'a') as outfile:
                    json.dump(self.return_log(), outfile)
                self.row_counter = 0
            else:
                self.row_counter += 1


    def __repr__(self):
        return '<LogRecord: %s, %s, %s">'%(self.logger_name,
                                           self.level_to_str(self.level),
                                           self.type_of)

if __name__ == '__main__':

    myLogger = Logger(name='myLogger', filename='my_logger.json', level=WARNING, buffer_length=2)
    print(myLogger)
    print(myLogger.show_last_log_message())
    myLogger.warning("This is warning message")
    myLogger.warning("This is next warning message")
    myLogger.info("This is info message")
    myLogger.error("This is error message", 1, val = 2)