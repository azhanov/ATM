import fileinput
from atm import ATM


class UI:
    """
    Simple console based interface over ATM class.
    """

    HELP = """b - balance\nl PIN - to login\nw XYZ - withdraw XYZ amount\nd XYZ - deposit XYZ amount\ne - exit"""
    BALANCE = 'b'
    DEPOSIT = 'd '
    EXIT = 'e'
    LOGIN = 'l '
    WITHDRAW = 'w '

    def __init__(self):
        self.atm = ATM()

    def execute(self):
        """
        Reads from a command line and processes the command
        :return:
        """
        for line in fileinput.input():
            line = line.rstrip()
            self._process_command(line)

    @staticmethod
    def help():
        """
        Print out help line
        :return:
        """
        print(UI.HELP)

    def _process_command(self, command):
        if not command:
            return
        if command == UI.BALANCE:
            balance = self.atm.get_balance()
            if balance is not None:
                print('Your balance is: [{}]'.format(balance))
        elif command == UI.EXIT:
            print('Thank you. Come again.')
            exit(0)
        elif command.startswith(UI.LOGIN):
            pin = self._get_input_value(command)
            self.atm.enter_pin(pin)
        elif command.startswith(UI.DEPOSIT):
            deposit_amount = self._get_input_value(command)
            self.atm.deposit(deposit_amount)
        elif command.startswith(UI.WITHDRAW):
            withdraw_amount = self._get_input_value(command)
            self.atm.withdraw(withdraw_amount)
        else:
            print('Unsupported command: [{}]'.format(command))

    @staticmethod
    def _get_input_value(command):

        if not command:
            return None
        inputs = command.split(' ')
        if not inputs or len(inputs) != 2:
            print('Invalid input, expecting one of the following options: {}'.format(UI.HELP))
        try:
            value = float(inputs[1])
            return value
        except ValueError:
            print('Expecting a number following option: {}'.format(inputs[0]))
            return None


if __name__ == '__main__':
    ui = UI()
    ui.help()
    ui.execute()
