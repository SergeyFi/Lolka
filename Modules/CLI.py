import Modules.Greeting as Greeting
from Modules.FractionHolder import FractionHolder


class CLI:
    def __init__(self):
        self._FractionHolder: FractionHolder

    def greeting(self):
        greeting = Greeting.greeting

        print(greeting)

    def input_period(self):
        print('Input period: ')

        period_raw = input()

        if period_raw.isdigit():
            self._FractionHolder = FractionHolder(period_raw)
        else:
            print('Bad period')
            self.input_period()

    def print_answer(self):
        print("Periodic fraction: ", self._FractionHolder.get_answer())
        print("Fraction: ", str(int(self._FractionHolder.get_numerator())) + "/" + str(int(self._FractionHolder.get_denominator())))

    def to_repeat(self):
        print('Repeat ? Yes/No')
        answer = str(input())
        answer.lower()

        if answer == 'yes' or answer == 'y':
            self.input_period()
            self.print_answer()
            self.to_repeat()
        else:
            exit()
