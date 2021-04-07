import logging
from typing import Union
from accessify import protected

#logging.basicConfig(filename='Account.log', filemode='a', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#                    level=logging.INFO)

class Account:
    '''
    The account class for the home assignment no6
    '''

    THE_MAX_REFILL_PER_FUNDS_ITERATION = 10000

    def __init__(self, funds: Union[int, float] = 0, logsize: Union[int] = 10):
        self.funds = self._round_to_centesimal(funds)
        self.logsize = logsize
        self.logcount = 0
        self.logiter = 0

        if logsize != 0:
            self.logiter += 1

        self.logger_setup(self)


    @protected
    #@staticmethod
    def log_operation(self, msg):
        if self.logsize == 0:
            return
        if self.logcount == self.logsize:
            print(f" The logging of operations has stopped because "
                  f"the log size has reached its maximum value {self.logsize}")
            return
        self.logcount += self.logiter

        try:
            self.logger.info(msg)
        except:
            pass

    @protected
    #@staticmethod
    def logger_setup(self, logsize):
        if self.logsize <= 0:
            print(f"Logging of operations is not required, since the log size is set to {self.logsize}")
            return

        self.log_operation(f"The account has initialized with {self.funds} value")
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)
        logger_handler = logging.FileHandler('Account.log', 'a')
        logger_handler.setLevel(logging.INFO)
        logger_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        logger_handler.setFormatter(logger_formatter)
        self.logger.addHandler(logger_handler)

    def get_funds(self):
        return self.funds

    def grow_funds(self, grow_step: Union[int, float]):
        if self.funds + grow_step <= 0:
            print("The funds cannot be less or equal 0!")
            return False
        elif grow_step > Account.THE_MAX_REFILL_PER_FUNDS_ITERATION:
            print(f"The funds change cannot be more than {Account.THE_MAX_REFILL_PER_FUNDS_ITERATION} at a time!")
            return False
        self.funds += grow_step
        self.funds = self._round_to_centesimal(self.funds)
        self.log_operation(f"The funds has changed to {self.funds}")

    @protected
    @staticmethod
    def _round_to_centesimal(val):
        return round(val + 0.001, 2)

if __name__ == '__main__':

    account = Account(123.125, 9)

    print(account.get_funds())

    account.grow_funds(10001)
    print(account.get_funds())

    account.grow_funds(1000)
    print(account.get_funds())

    account.grow_funds(-1324)
    print(account.get_funds())

    account.grow_funds(float('inf'))
    print(account.get_funds())

    for i in range(10):
        account.grow_funds(i)
        print(account.get_funds())

    print(float('inf'))
