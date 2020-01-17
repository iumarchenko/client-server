# 2. Задание на закрепление знаний по модулю json.
# Есть файл orders в формате JSON с информацией о заказах.
# Написать скрипт, автоматизирующий его заполнение данными.
# Для этого:
# Создать функцию write_order_to_json(), в которую передается 5 параметров —
# товар (item), количество (quantity), цена (price), покупатель (buyer), дата (date).
# Функция должна предусматривать запись данных в виде словаря в файл orders.json.
# При записи данных указать величину отступа в 4 пробельных символа;
# Проверить работу программы через вызов функции write_order_to_json()
# с передачей в нее значений каждого параметра.
import json


def write_order_to_json(item, quantity, price, buyer, date):
    with open('orders.json',encoding='utf-8') as f_n:
        data = json.load(f_n)

    with open('orders.json', 'w',encoding='utf-8') as f_n:
        data['orders'].append({
            'item': item,
            'quantity': quantity,
            'price': price,
            'buyer':buyer,
            'date': date})
        json.dump(data, f_n, indent=4, ensure_ascii=False)


write_order_to_json('printer', '10', '6700', 'Ivanov I.I.', '24.09.2017')
write_order_to_json('scaner', '20', '10000', 'Petrov P.P.', '11.01.2018')
write_order_to_json('computer', '5', '40000', 'Sidorov S.S.', '2.05.2019')
write_order_to_json('принтер', '10', '6700', 'Ivanov I.I.', '24.09.2017')
write_order_to_json('сканер', '20', '10000', 'Petrov P.P.', '11.01.2018')
write_order_to_json('компьютер', '5', '40000', 'Sidorov S.S.', '2.05.2019')