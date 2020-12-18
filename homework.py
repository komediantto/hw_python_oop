import datetime as dt


class Calculator:
    def __init__(self, limit):
        self.records = []
        self.limit = abs(limit)

    def add_record(self, record):
        self.records.append(record)

    def get_today_stats(self):
        sum = 0
        today = dt.date.today()
        for record in self.records:
            if record.date == today:
                sum += record.amount
            else:
                pass
        print(f'За сегодня вышло {sum}')
        return sum

    def get_week_stats(self):
        week_sum = 0
        for record in self.records:
            today = dt.date.today()
            week = today - dt.timedelta(days=8)
            if week <= record.date <= today:
                week_sum += record.amount
        return week_sum


class Record:
    def __init__(self, amount, comment, date=None):
        self.amount = abs(amount)
        self.comment = comment
        self.date = date
        if date == None:
            self.date = dt.date.today()
        else:
            self.date = dt.datetime.strptime(date, "%d.%m.%Y").date()    

    def show(self):
        print(f"Сумма: {self.amount}, Цель: {self.comment}, Дата: {self.date}")
    pass

class CaloriesCalculator(Calculator):
    def __init__(self, limit):
        super().__init__(limit)

    def get_calories_remained(self):
        today_cal = Calculator.get_today_stats(self)
        remain = self.limit - today_cal
        if today_cal < self.limit:    
            return ("Сегодня можно съесть что-нибудь ещё, "
             f"но с общей калорийностью не более {remain} кКал")
        else:
            return('Хватит есть!')


class CashCalculator(Calculator):
    USD_RATE = 72.85
    EURO_RATE = 89.04
    RUB_RATE = 1

    def __init__(self, limit):
        super().__init__(limit)

    def get_today_cash_remained(self, currency):
        today_sum = Calculator.get_today_stats(self)
        if currency == 'eur':
            rate = self.EURO_RATE
            money_name = 'Euro'
        elif currency == 'usd':
            rate = self.USD_RATE
            money_name = "USD"   
        elif currency == 'rub':
            rate = self.RUB_RATE
            money_name = 'руб'    
        else:
            print('Я не знаю такой валюты')

        if today_sum < self.limit:
            remains = round((self.limit - today_sum)/rate, 2)    
            return (f"На сегодня осталось {(remains)} {money_name}")
        elif today_sum == self.limit:
            return ('Денег нет, держись')
        else:
            remains = abs(round((self.limit - today_sum)/rate, 2))
            return(f'Денег нет, держись: твой долг - {(remains)} {money_name}')         


wallet = CashCalculator(5000)
wallet.add_record(Record(5000, 'LoL'))
print(wallet.get_today_cash_remained('rub'))


