from Sto.center import Center 
com = str
sto = Center()
while(True):
    com = input('''Меню: 
    1.- Регистрация автомобиля
    2.- Регистрация услуги
    3.- Оказание услуги
    4.- Список автомобилей
    5.- Список услуг
    6.- Информация об учлуге
    7.- Выход
     >> ''')
    if com == '1':
        #Function registration auto
        print("Добавление автомобиля")
        sto.auto_add()
    elif com == '2':
        #Function registration service
        print("Добавление услуги")
        sto.service_add()
    elif com == '3':
        #Function doing to a servce
        print("Оказание услуги")
    elif com == '4':
        #Function display list auto from local database
        print("Список зарегистрированных автомобилей")
        sto.auto_list()
    elif com == '5':
        #Function display list services
        sto.service_list()
        print("Оказание услуги")
    elif com == '6':
        #Function information services
        print("Информация об услуге")
    elif com == '7':
        #Exit application
        break
    else:
        #Don't found command
        print("Команда не найдена, повторите ввод!")