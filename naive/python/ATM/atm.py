
class ATM:
    """
    Conceptual implementation of the basic ATM functionality.

    Methods
    -------
    enter_pin
    get_balance
    deposit
    withdraw
    """

    DAILY_LIMIT = 100

    def __init__(self):
        self.initialized = False
        self.balance = 0.0
        self.pin = 1234

    def enter_pin(self, pin):
        if self.initialized:
            print('You have already logged in.')
            return
        if not pin:
            print('Please, provide a 4-digit PIN for your account')
            return
        if pin == self.pin:
            print('Login successful, welcome to BOP (Bank Of Python)')
            self.initialized = True
        else:
            print('You have entered an invalid PIN, please try again')

    def get_balance(self):
        if self._initialized():
            return self.balance
        else:
            return None

    def deposit(self, deposit_amount):
        if not self._initialized():
            return None
        if not deposit_amount:
            print('Please, enter a valid amount to deposit')
            return
        if deposit_amount <= 0:
            print('Sorry, the amount to deposit needs to be a positive value, rather then: {}'.format(deposit_amount))
            return
        self.balance += deposit_amount

    def withdraw(self, withdraw_amount):
        if not self._initialized():
            return None
        if not withdraw_amount:
            print('Please, enter a valid amount to withdraw')
            return
        if withdraw_amount > self.balance:
            print('Sorry, you can not withdraw more than the currently available amount: {}'.format(self.balance))
            return
        if withdraw_amount > ATM.DAILY_LIMIT:
            print('Sorry, you can not withdraw more than the daily max amount: {}'.format(ATM.DAILY_LIMIT))
            return
        self.balance -= withdraw_amount
        return withdraw_amount

    def _initialized(self):
        if not self.initialized:
            print('Please, enter a valid 4-digit PIN number for your account')
            return False
        else:
            return True
