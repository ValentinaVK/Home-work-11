
class Num:
    def __init__(self, *args):
        self.my_list = []

    def my_input(self):
        while True:
            try:
                numbers = int(input('Введите значения и нажимайте Enter - '))
                self.my_list.append(numbers)
                print(f'Текущий список - {self.my_list} \n ')
            except:
                print(f"Недопустимое значение - строка")
                y_or_n = input(f'Попробовать еще раз? R/S ')

                if y_or_n == 'R' or y_or_n == 'r':
                    print(try_except.my_input())
                elif y_or_n == 'S' or y_or_n == 's':
                    return f'Вы вышли'
                else:
                    return f'Вы вышли'
                
try_except = Num(1)
print(try_except.my_input())