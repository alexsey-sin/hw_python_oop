import datetime as dt


class Record:
    def __init__(self, amount, date='', comment=''):
        if date == '':
            new_date = dt.date.today()
        else:
            new_date = dt.datetime.strptime(date, '%d.%m.%Y').date()
        self.amount = amount
        self.date = new_date
        self.comment = comment


class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []

    def add_record(self, record):
        self.records.append(record)

    def get_today_stats(self):
        date_today = dt.date.today()
        amount_today = 0
        for rec in self.records:
            if rec.date == date_today:
                amount_today += rec.amount
        return amount_today

    def get_week_stats(self):
        date_today = dt.date.today()
        date_start = date_today - dt.timedelta(weeks=1)
        amount_week = 0

        for rec in self.records:
            if date_start < rec.date <= date_today:
                amount_week += rec.amount
        return amount_week


class CashCalculator(Calculator):
    # exchange rates for 09.02.2021
    USD_RATE = 74.30
    EURO_RATE = 89.58

    def __init__(self, limit):
        super().__init__(limit)

    def get_today_cash_remained(self, currency):
        balance = self.limit - self.get_today_stats()

        if currency == 'rub':
            str_currency = 'руб'
        elif currency == 'usd':
            str_currency = 'USD'
            balance /= self.USD_RATE
        elif currency == 'eur':
            str_currency = 'Euro'
            balance /= self.EURO_RATE
        else:
            return 'Unknown currency'

        balance = round(balance, 2)

        if balance == 0:
            sentence = 'Денег нет, держись'
        elif balance > 0:
            sentence = f'На сегодня осталось {balance} {str_currency}'
        else:
            balance *= -1
            sentence = f"""Денег нет, держись: 
                твой долг - {balance} {str_currency}"""

        return sentence


class CaloriesCalculator(Calculator):
    def __init__(self, limit):
        super().__init__(limit)

    def get_calories_remained(self):
        balance = self.limit - self.get_today_stats()

        if balance > 0:
            sentence = f"""Сегодня можно съесть что-нибудь ещё, 
                но с общей калорийностью не более {balance} кКал"""
        else:
            sentence = 'Хватит есть!'

        return sentence


if __name__ == '__main__':
    print('Интересно а сколько зарабатывают ревьюеры?')
