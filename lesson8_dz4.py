class Sklad:
    sklad_names = []

    def __init__(self, name):
        self.name = name
        Sklad.sklad_names.append(self)

    def __str__(self):
        return f'{self.name}'

    @staticmethod
    def inventory(name):
        for item in Orgtechnika.items:
            if item.sklad_name == name:
                print(item)


class Orgtechnika:
    items = []

    def __init__(self, classtype='', vendor='', model='', price='', sale_date='', sn='', sklad_name=''):
        self.classtype = input(f'Введите тип устройства: ') if classtype == '' else classtype
        self.vendor = input(f'Введите производителя {self.classtype}а: ') if vendor == '' else vendor
        self.model = input(f'Введите модель {self.classtype}а: ') if model == '' else model
        self.price = input(f'Введите цену {self.classtype}а: ') if price == '' else price
        self.sale_date = input(f'Введите дату закупки {self.classtype}а: ') if sale_date == '' else sale_date
        self.sn = input(f'Введите серийный номер {self.classtype}а: ') if sn == '' else sn
        Orgtechnika.items.append(self)
        self.sklad_name = sklad_name

    def __str__(self):
        return f'{self.classtype} {self.vendor} {self.model} sn: {self.sn} sklad: {self.sklad_name}'

    def move(self, sklad_name=''):
        if sklad_name == '':
            print('Input sklad number:')
            for i, sklad_name1 in enumerate(Sklad.sklad_names, start=1):
                print(f'{i}: {sklad_name1}')
            sklad_number = input('sklad №: ')
            self.sklad_name = Sklad.sklad_names[int(sklad_number)-1].name
        else:
            self.sklad_name = sklad_name

    @classmethod
    def set_unit(cls, data):
        c, v, m, p, d, sn = data
        return cls(c, v, m, p, d, sn)


class Printer(Orgtechnika):
    def __init__(self, classtype='Принтер', vendor='', model='', price='', sale_date='', sn='', sklad_name=''):
        super().__init__(classtype, vendor, model, price, sale_date, sn, sklad_name)
        self.iscolor = input('iscolor(yes/no): ')
        self.isnetwork = input('isnetwork(yes/no): ')
        self.type = input('lazer or inkjet: ')


class Scanner(Orgtechnika):
    def __init__(self, classtype='Сканер', vendor='', model='', price='', sale_date='', sn='', sklad_name=''):
        super().__init__(classtype, vendor, model, price, sale_date, sn, sklad_name)
        self.ismultipage = input('ismultipage(yes/no): ')


class Copier(Orgtechnika):
    def __init__(self, classtype='Копир', vendor='', model='', price='', sale_date='', sn='', sklad_name=''):
        super().__init__(classtype, vendor, model, price, sale_date, sn, sklad_name)
        self.format = input('format(A3/A4): ')


def menu():
    while True:
        m_a = input('MENU: 1-input unit, 2-move unit, 3-list units, 4-sklad operations, 5-end programm  ')
        if m_a == '5':
            break
        elif m_a == '1':
            while True:
                m_unit = input('Choose type: 1-printer, 2-scanner, 3-copier, 4-other  ')
                if m_unit == '1':
                    new_object = Printer()
                    new_object.move()
                    break
                elif m_unit == '2':
                    new_object = Scanner()
                    new_object.move()
                    break
                elif m_unit == '3':
                    new_object = Copier()
                    new_object.move()
                    break
                elif m_unit == '4':
                    new_object = Orgtechnika()
                    new_object.move()
                    break
                else:
                    print('Wrong input')
                    continue
        elif m_a == '2':
            print('choose unit')
            for i, item in enumerate(Orgtechnika.items, start=1):
                print(f'{i}: {item}')
            org_number = input(f'unit №: ')
            print(f'This unit is located on sklad: {Orgtechnika.items[int(org_number)-1].sklad_name}')
            while True:
                answer = input('Do you want to move it to another sklad? (y/n): ')
                if answer == 'y':
                    Orgtechnika.items[int(org_number) - 1].move()
                    print('successful')
                    break
                elif answer == 'n':
                    break
                else:
                    print('Your input is wrong')
                    continue
        elif m_a == '3':
            for item in Orgtechnika.items:
                print(item)
        elif m_a == '4':
            while True:
                m_sklad = input(f'MENU-SKLAD: 1-new sklad, 2-list sklads, 3-inventory sklad, 4-exit  ')
                if m_sklad == '1':
                    new_sklad = input('Input sklad name: ')
                    Sklad(new_sklad)
                    print('successful')
                elif m_sklad == '2':
                    for i, sklad_name1 in enumerate(Sklad.sklad_names, start=1):
                        print(f'{i}: {sklad_name1}')
                elif m_sklad == '3':
                    print('choose sklad')
                    for i, sklad_name1 in enumerate(Sklad.sklad_names, start=1):
                        print(f'{i}: {sklad_name1}')
                    sklad_number = input('sklad №: ')
                    sklad_name = Sklad.sklad_names[int(sklad_number)-1]
                    Sklad.inventory(sklad_name.name)
                elif m_sklad == '4':
                    break
                else:
                    print('Wrong input')
                    continue

        else:
            print('Your input is wrong!')
            continue
    print('The end!!!')


Org1 = Orgtechnika.set_unit(['Сканер', 'Canon', 'Canoscan lide 300', '5900', '03.04.2020', '1231sd123'])
Org2 = Orgtechnika.set_unit(['Сканер', 'Canon', 'Canoscan lide 300', '5900', '03.04.2020', '1231js567'])
Org3 = Orgtechnika.set_unit(['Принтер', 'HP', 'OfficeJet Pro 6230', '5600', '02.02.2021', '1236asd'])
Org4 = Orgtechnika.set_unit(['Принтер', 'HP', 'LaserJet Pro M404', '23000', '03.04.2021', 'ads123fsd'])
Sklad('room1')
Sklad('room2')
Org1.move('room1')
Org2.move('room1')
Org3.move('room1')
Org4.move('room2')

menu()
