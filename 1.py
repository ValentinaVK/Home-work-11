class Data:
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def extract(cls, day_month_year):
        my_date = []

        for i in day_month_year.split():
            if i != '-': my_date.append(i)

        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def valid(day, month, year):
  
        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2023 >= year >= 0:
                    return f'Хорошо'
                else:
                    return f'Неправильный год'
            else:
                return f'Неправильный месяц'
        else:
            return f'Неправильный день'

    def __str__(self):
        return f'Текущая дата {Data.extract(self.day_month_year)}'


today = Data('09 - 02 - 2022')
print(today)
print('41 - 02 - 2022 : ' + Data.valid(41, 2, 2022))
print('9 - 13 - 2022 : ' + today.valid(9, 13, 2022))
print('9 - 02 - 2026 : ' + today.valid(9, 2, 2026))
print(Data.extract('9 - 2 - 2022'))
print(today.extract('9 - 2 - 2022'))
print(Data.valid(9, 2, 2022))