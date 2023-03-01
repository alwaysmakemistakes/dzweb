"Сделать копию скрипта задания 6.2."
"Добавить проверку введенного IP-адреса. Адрес считается корректно заданным, если он:"
"состоит из 4 чисел (а не букв или других символов)"
"числа разделенны точкой"
"каждое число в диапазоне от 0 до 255"
"Если адрес задан неправильно, выводить сообщение: «Неправильный IP-адрес»." 
"Сообщение «Неправильный IP-адрес» должно выводиться только один раз,"
"даже если несколько пунктов выше не выполнены."
"Ограничение: Все задания надо выполнять используя только пройденные темы."


#ввод
ip = input('Введите IP-адрес(например 10.0.1.1): ')
a = ip.count('.')
if a != 3:
    print('неправильный адрес, добавьте точки')
else:
    #проверка на цифры в октетах
    ip = ip.strip().split('.')
    int1 = ip[0].isdigit()
    int2 = ip[1].isdigit()
    int3 = ip[2].isdigit()
    int4 = ip[3].isdigit()
    if int1 is not True and int2 is not True and int3 is not True and int4 is not True:
        print('неправильный адрес, используются только цифры')
    else:
        #проверка на диапазон цифр(0-255)"
        oktet1 = int(ip[0])
        oktet2 = int(ip[1])
        oktet3 = int(ip[2])
        oktet4 = int(ip[3])
        allowed_range = list(range(0, 256))
        if oktet1 not in allowed_range or oktet2 not in allowed_range or oktet3 not in allowed_range or oktet4 not in allowed_range:
            print('неправильный ip, только в 0-255 ренже')
        else:
            #проверка на класс
            unicast = list(range(1, 224))
            multicast = list(range(224, 240))
            broadcast = [255,255,255,255]
            unassigned = [0,0,0,0]

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