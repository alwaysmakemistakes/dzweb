"Сделать копию скрипта задания 6.2a."
"Дополнить скрипт: Если адрес был введен неправильно, запросить адрес снова."
"Ограничение: Все задания надо выполнять используя только пройденные темы."


#ввод
ip = input('Введите IP-адрес(например 10.0.1.1): ')
#если ошиька
status = False
while not status:
    #точки
    if ip.count('.') != 3:
        print('неправильный адрес, добавьте точки')
    #цифры
    elif ip.strip().split('.')[0].isdigit() is False or ip.strip().split('.')[1].isdigit() is False or ip.strip().split('.')[2].isdigit() is False or ip.strip().split('.')[3].isdigit() is False:
        print('неправильный адрес, используются только цифры')
    #ренж
    elif int(ip.strip().split('.')[0]) not in list(range(0, 256)) or int(ip.strip().split('.')[1]) not in list(range(0, 256)) or int(ip.strip().split('.')[2]) not in list(range(0, 256)) or int(ip.strip().split('.')[3]) not in list(range(0, 256)):
        print('неправильный ip, только в 0-255 ренже')
    else:
    #основная проверка
        ip = ip.strip().split('.')
        oktet1 = int(ip[0])
        oktet2 = int(ip[1])
        oktet3 = int(ip[2])
        oktet4 = int(ip[3])
        unicast = list(range(1, 224))
        multicast = list(range(224, 240))
        broadcast = [255,255,255,255]
        unassigned = [0,0,0,0]
    #классы
        if oktet1 in unicast:
            print('This is unicast IP')
        elif oktet1 in multicast:
            print('This is multicast')
        elif oktet1 in broadcast and oktet2 in broadcast and oktet3 in broadcast and oktet4 in broadcast:
            print('This is broadcast IP')
        elif oktet1  in unassigned and oktet2 in unassigned and oktet3 in unassigned and oktet4 in unassigned:
            print('This is unassigned IP')
        else:
            print('This is unused IP')
        status = True
        continue
    ip = input('Введите IP-адрес ещё раз: ')