class DivisionByNull:
    def __init__(self, divid, denominator):
        self.divider = divid
        self.denominator = denominator

    @staticmethod
    def divide_by_null(divid, denominator):
        try:
            return (divid / denominator)
        except:
            return (f"Деление на ноль невозможно")


div = DivisionByNull(5, 100)
print(DivisionByNull.divide_by_null(5, 100))
print(DivisionByNull.divide_by_null(10, 0.1))
print(div.divide_by_null(100, 0))