class Date:
    def __init__(self, str_date):
        try:
            if Date.transform(str_date):
                self.str_date = Date.transform(str_date)
                print(f'Объект успешно создан\n{self}')
            else:
                raise MyErr(f'Объект не может быть создан, неверный формат данных')
        except (TypeError, ValueError, MyErr) as err:
            # print(f'Объект не может быть создан, неверный формат данных')
            print(err)
        # except ValueError:
        #    print(f'Объект не может быть создан, неверный формат данных')

    def __str__(self):
            d, m, y = self.str_date
            return f'Day:{d}, Month:{m}, Year:{y}'

    @classmethod
    def transform(cls, str_date):
        try:
            d, m, y = map(int, str_date.split('-'))
            if cls.validate(d, m, y):
                return d, m, y
            else:
                return False
        except ValueError:
            return False

    @staticmethod
    def validate(a, b, c):
        if (1 <= a <= 31) and (1 <= b <= 12) and (1 <= c <= 9999):
            return True
        else:
            return False


class MyErr(Exception):
    def __init__(self, txt):
        self.txt = txt


x = Date('03-abc-2020')
y = Date('02-14-2021')
z = Date('02 - 12 - 2000')

print(z.str_date)

