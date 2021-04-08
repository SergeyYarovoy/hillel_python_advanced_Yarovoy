import logging
from typing import Union
from accessify import protected
#import math                                    # пробовал ниже использовать isinf из
#import numpy as np                             # этих обоих либ, но проверка не получается. Почему?

class Account:
    '''
    The account class for the home assignment no6
    '''

    MAX_FUNDS_STEP = 10000

    def __init__(self, funds: Union[int, float] = 0, logsize: Union[int] = 10, syslog_size: Union[int] = 10):
        self.funds = self._round_to_centesimal(funds)
        self.logsize = logsize
        self.syslog_size = syslog_size
        self.logger_setup(self)
        self.s_logger.warning(f"The account has initialized with {self.funds} value")

    def get_last_tx_list(self):
        if self.logsize == 0:
            return list()
        else:
            return list(open("tx_account.log", "r"))[-self.logsize:]

    def get_syslog_list(self):
        return list(open("sys_account.log", "r"))[-self.syslog_size:]

    @protected
    def logger_setup(self, dummy_var):                          # без этой dummy_var падает с ошибкой. Почему?
        self.tx_logger = logging.getLogger('account_tx_logger')
        self.s_logger = logging.getLogger('account_system_logger')
        self.tx_logger.setLevel(logging.INFO)
        self.s_logger.setLevel(logging.WARNING)
        s_logger_handler = logging.FileHandler('sys_account.log', 'a')
        tx_logger_handler = logging.FileHandler('tx_account.log', 'a')
        logger_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        s_logger_handler.setFormatter(logger_formatter)
        tx_logger_handler.setFormatter(logger_formatter)
        self.s_logger.addHandler(s_logger_handler)
        self.tx_logger.addHandler(tx_logger_handler)

    def get_funds(self):
        return self.funds

    def grow_funds(self, grow_step: Union[int, float]):
        if abs(grow_step) > Account.MAX_FUNDS_STEP:
            self.s_logger.warning(f"The funds change cannot be more than {Account.MAX_FUNDS_STEP} at a time!")
            return False

        '''
        print(np.isinf(grow_step))              # почему-то тут получается True
        if np.isinf(grow_step):                 # но сюда все равно не заходит. Почему так может быть?
            print('INF')
            self.s_logger.warning(f"The funds change cannot be changed with infinite value!")
            return False
        '''

        if abs(grow_step) < 0.01:
            self.s_logger.warning(f"The funds change cannot be less than 0.00 at a time!")
            return False

        self.funds += grow_step
        self.funds = self._round_to_centesimal(self.funds)
        self.tx_logger.info(f"The funds has changed to {self.funds}")

    @protected
    @staticmethod
    def _round_to_centesimal(val):
        return round(val + 0.001, 2)


if __name__ == '__main__':

    account = Account(-123.125, 0)

    print(account.get_funds())

    account.grow_funds(10001)
    print(account.get_funds())

    account.grow_funds(1000)
    print(account.get_funds())

    account.grow_funds(-1324)
    print(account.get_funds())

    account.grow_funds(0.001)
    print(account.get_funds())

    account.grow_funds(float('inf'))
    print(account.get_funds())

    for i in range(30):
        account.grow_funds(i)
        print(account.get_funds())

    for i in account.get_last_tx_list():
        print(i.rstrip())

    for i in account.get_syslog_list():
        print(i.rstrip())