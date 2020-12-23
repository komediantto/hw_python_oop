import datetime as dt


class Calculator:
    def __init__(self, limit):
        self.records = []
        self.limit = abs(limit)

    def add_record(self, record):
        self.records.append(record)

    def get_today_stats(self):
        today = dt.date.today()
        spend_money = [record.amount for record in self.records
                      if record.date == today]        
        sum_today = sum(spend_money,)
        return sum_today

    def get_week_stats(self):
        today = dt.date.today()
        week = dt.timedelta(7)
        week_ago = today - week
        return sum([
        record.amount for record in self.records
        if (today >= record.date >= week_ago)
        ])
        #for record in self.records:
        #    print(week_ago, record.date, today)   
        #    if week_ago <= record.date <= today:
        #        week_sum += record.amount     
        #return week_sum

class Record:
    def __init__(self, amount, comment, date=None):
        self.amount = amount
        self.comment = comment
        self.date = date
        if date is None:
            self.date = dt.date.today()
        else:
            self.date = dt.datetime.strptime(date, '%d.%m.%Y').date()    

class CaloriesCalculator(Calculator):
    def get_calories_remained(self):
        today_cal = self.get_today_stats()
        remain = self.limit - today_cal
        if today_cal < self.limit:    
            return ('Сегодня можно съесть что-нибудь ещё, '
             f'но с общей калорийностью не более {remain} кКал')
        return('Хватит есть!')


class CashCalculator(Calculator):
    USD_RATE = 72.85
    EURO_RATE = 89.04
    RUB_RATE = 1

    def get_today_cash_remained(self, currency):
        today_sum = self.get_today_stats()
        dict_of_cur = {
            'eur' : (self.EURO_RATE, 'Euro'),
            'usd' : (self.USD_RATE, 'USD'),
            'rub' : (self.RUB_RATE, 'руб')
        }
        if currency in dict_of_cur.keys():
            rate = dict_of_cur[currency][0]
            money_name = dict_of_cur[currency][1]
        else:
            print('Я не знаю такой валюты')

        if today_sum < self.limit:
            remains = round((self.limit - today_sum)/rate, 2)    
            return (f'На сегодня осталось {remains} {money_name}')
        elif today_sum == self.limit:
            return ('Денег нет, держись')
        remains = abs(round((self.limit - today_sum)/rate, 2))
        return(f'Денег нет, держись: твой долг - {remains} {money_name}')         

if __name__ == "__main__":
    wallet = CashCalculator(5000)
    wallet.add_record(Record(67,'сиськи','16.12.2020, 19:50'))
    wallet.add_record(Record(67,'жопа','15.12.2020, 17:00'))
    wallet.add_record(Record(67,'fffffff','16.12.2020, 19:44'))
    print(wallet.get_week_stats())