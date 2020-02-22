from Sto.auto import Auto
from Sto.services import Services

class DidSerives():
    auto = Auto.TempAuto
    service = Services.PriceServices
    timeService = int
    def __init__(self, auto, service):
        self.auto = auto
        self.service = service

class DidSerivesHight():
    auto = Auto.TempAutoHight
    service = Services.PriceServices
    timeService = int
    def __init__(self, auto, service):
        self.auto = auto
        self.service = service

class Center():
    base_auto = []
    base_hight_auto = []
    price_list = []
    list_did_services_auto = []
    list_did_services_hight_auto = []

    def __init__(self):
        base_auto = []
        base_hight_auto = []
        price_list = []
        list_did_services_auto = []
        list_did_services_hight_auto = []

    def auto_add(self):
        fr = str
        while(fr != "1" and fr != "2" and fr != "3"):
            fr = input("Тип автомобиля:\n1.- Легковой\n2.- Грузовой\n3.- Отмена действия\n>> ")
            if fr == '1':
                #Add low auto
                mark = input("Введите марку автомобиля >> ")
                color = input("Введите цвет автомобиля >> ")
                gos_number = input("Введите государственный регистрационный ноомер автомобиля >> ")
                start_year = input("Введите год выпуска автомобиля dd/mm/YYYY >> ")
                auto = Auto.TempAuto(mark,color,gos_number,start_year)
                self.base_auto.append(auto)
            elif fr == '2':
                #Add hight auto
                mark = input("Введите марку автомобиля >> ")
                color = input("Введите цвет автомобиля >> ")
                gos_number = input("Введите государственный регистрационный ноомер автомобиля >> ")
                start_year = input("Введите год выпуска автомобиля dd/mm/YYYY >>")
                pickup = str
                while(pickup != 'Да' and pickup != 'да' and pickup != 'Нет' and pickup != 'нет'):
                    pickup = input("Присутствует ли грузовой отсек? Да/Нет >> ")
                    if pickup == 'Да' or pickup == 'да':
                        auto = Auto.TempAutoHight(True, mark, color,gos_number,start_year)
                    elif pickup == 'Нет' or pickup == 'нет':
                        auto = Auto.TempAutoHight(False, mark, color,gos_number,start_year)
                self.base_hight_auto.append(auto)
            elif fr == '3':
                #Candel
                print("Отмена действия!")
                return
            else:
                print("Команда не найдена!")
    
    def auto_list(self):
        if len(self.base_auto) != 0:
            print("Легковые автомобили: ")
            for idx, auto in enumerate(self.base_auto):
                print("ID ", idx+1, " Марка: ", auto.mark)
        else:
            print("Легковых автомобилей не зарегистрировано")
        if len(self.base_hight_auto) != 0:
            print("Грузовые автомобили: ")
            for idx, auto in enumerate(self.base_hight_auto):
                print("ID ", idx+1, " Марка: ", auto.mark)
        else:
            print("Грузовых автомобилей не зарегистрировано")

    def service_add(self):
        name = input('Введите наименование сервиса >> ')
        about = input('Описание >> ')
        price = float(input('Введите цену >> '))
        service = Services.PriceServices(name, about, price)
        self.price_list.append(service)

    def service_list(self):
        if len(self.price_list) == 0:
            com = input('Услуги отсутствуют!\nХотите добавить услугу? yes/no >>')
            if com == 'yes' or com == 'y':
                self.service_add()
            return
        else:
            for idx, service in enumerate(self.price_list):
                print("ID ", idx+1, " Услуга: ", service.name, " Цена: ", service.price)
