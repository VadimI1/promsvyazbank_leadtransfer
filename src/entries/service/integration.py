from dataclasses import dataclass
from functools import wraps
import requests
import time

from django.conf import settings


from ..service.validation import SkorozvonCall
from .exceptions import UnsuccessfulLeadCreationError

import uuid
import hashlib
import datetime
import base64


def genheaders(user_name, user_key):
    random = str(uuid.uuid4()).encode('ASCII')
    nonce = random
    curdate = datetime.datetime.now().replace(microsecond=0)

    hash_digest = hashlib.sha1()
    hash_digest.update(nonce)
    hash_digest.update(curdate.isoformat().encode())
    hash_digest.update(user_key.encode())

    x_wsse = ', '.join(['UsernameToken Username="{user}"',
                        'PasswordDigest="{digest}"',
                        'Nonce="{nonce}"',
                        'Created="{created}"'])
    x_wsse = x_wsse.format(
        user=user_name,
        digest=base64.b64encode(hash_digest.digest()).decode('utf-8'),
        nonce=base64.b64encode(nonce).decode('utf-8'),
        created=curdate.isoformat(),
    )

    return {
        # 'Authorization': 'WSSE profile="UsernameToken"',
        'X-WSSE': x_wsse,
    }


def time_limit_signalization(func):
    """
    Декоратор для проверки времени выполнения функции
    Если время выполнения превышает TIME_LIMIT_MINUTES,
    То соответствующеесообщение отправляется в чат разработки
    """
    time_limit_minutes = 10

    @wraps(func)
    def wrap(*args, **kw):
        start_time = time.time()
        result = func(*args, **kw)
        end_time = time.time()
        upload_time_minutes = int((end_time - start_time) // 60)
    return wrap



def list_city():
    url = 'https://api.lk.finstar.online/fo/v1.0.0/cities'
    key = {
        "access-token": "gjSI9TDc-YfHjntzoTxXf6LNQz0a8MmYjC6ntxyG5r7fcJnd-xBKomvDwoxQlGeE",
    }
    resp = requests.get(url, params=key)
    print(" -- Status", resp, " -- Message = ", 'list_city')
    return resp.json()
    #{'code': 200, 'data': [{'id': 119, 'city_id': '119-103-5', 'city_name': 'Абакан', 'city_timezone': 'МСК+4', 'region': 'Республика Хакасия', 'specify_id': None, 'fias_id': '42a02e11-a337-4d50-8596-fc76dae7c62a'},


#[{'id': 6, 'title': 'Торговый эквайринг', 'description': 'Условие выплаты - 5000 рублей операций по терминалу, прошедших по расчетному счету в ПСБ в течение 90 дней с момента открытия расчетного счета'},
# {'id': 11, 'title': 'Зарплатный проект', 'description': 'Условие выплаты - зачисление по реестру от 18 000 рублей заработной платы на счет работника в течение 90 дней с момента открытия расчетного счета'},
# {'id': 20, 'title': 'Телефонный доступ к банковскому счету', 'description': 'Условие выплаты - полученная Банком оплата по акции в течение 30 дней с момента открытия счета'},
# {'id': 26, 'title': 'Акция - "Бизнес Крым"', 'description': 'Первый месяц обслуживания бесплатно. Снятие наличных в банкомате 0,5%. Срок проведения акции - до 31 декабря 2025 года. Территория проведения Акции – Республика Крым и Севастополь.'},
# {'id': 27, 'title': 'Акция - "Выгодный старт"', 'description': 'Первые 3 месяца ставка - 0,9% независимо от вида деятельности'},
# {'id': 28, 'title': 'Акция - "Хороший год"', 'description': 'Выгодные условия для компаний, сфера деятельности которых - "Выращивание винограда" или "Производство вина из винограда"'}]}

#[{'id': 1, 'title': 'Бизнес 24/7'},
# {'id': 4, 'title': 'Бизнес Лайт'},
# {'id': 5, 'title': 'Плати меньше'},
# {'id': 8, 'title': 'Бизнес драйв'},
# {'id': 14, 'title': 'Ноль'},
# {'id': 15, 'title': 'Оптимум (Крым)'},
# {'id': 16, 'title': 'Максимум (Крым)'},
# {'id': 17, 'title': 'Всё для бизнеса'}]}

@time_limit_signalization
def create_PSB_deal_by_call(lead_info: SkorozvonCall):
    # id_city = list_city()
    # for i in id_city['data']:
    #     if lead_info.city in i['city_name']:
    #         id = i['city_id']
    #         print(id)
    # print(lead_info)
    data = {
        "inn": lead_info.inn,
        "name": "Скорозвон",###########
        "need_s_schet": True,
        "need_r_schet": True,
        "fio": lead_info.name,
        "phone": lead_info.phone,
        "email": lead_info.email,
        "city_id": id,
        "comment": lead_info.comment,
        "referrer_url": "",
        "cross_products": [
            6
        ],
        "tariff_id": 14
    }

    key = {
        "access-token": "gjSI9TDc-YfHjntzoTxXf6LNQz0a8MmYjC6ntxyG5r7fcJnd-xBKomvDwoxQlGeE",
    }
    print(data)
    #resp = requests.post(url="https://api.lk.finstar.online/fo/v1.0.0/orders", params=key, json=data)
    #print(resp)

@time_limit_signalization
def create_my_business_deal_by_call(lead_info: SkorozvonCall):
    print(lead_info)
    data = {
        "Fio" : lead_info.name,
        "Email" : lead_info.email,
        "Phone" : lead_info.phone,
        "Product" : "Biz",

        "Inn" : lead_info.inn,
        "UtmCampaign": "partner_10067398",
        "UtmSource": "partner.1581.biz"
    }
    print(data)
    #resp = requests.post(url="https://public.moedelo.org/Home/api/Registration/ExternalRegistration/V2", headers=genheaders('Vector', '2FA9D1E7-4290-4277-8580-19CF8C7E50A1'), json=data)
    #print(resp)
