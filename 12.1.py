# Создать функцию ping_ip_addresses, которая проверяет пингуются ли IP-адреса. Функция ожидает как аргумент список IP-адресов.
# Функция должна возвращать кортеж с двумя списками:
# список доступных IP-адресов
# список недоступных IP-адресов
# Для проверки доступности IP-адреса, используйте команду ping.
# Ограничение: Все задания надо выполнять используя только пройденные темы.


import subprocess

def ping_ip_addresses(ip_addr):
    dead_ip = []
    alive_ip = []
    result = ()
    for ip in ip_addr:
        result = subprocess.run(['ping', '-c', '1', '-n', '-i', '0.2', ip], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        if result.returncode==0:
            print('Yeah,', ip, 'is alive.')
            alive_ip.append(ip)
        else:
            print('Oh noo,', ip, 'is dead.')
            dead_ip.append(ip)
        result = (alive_ip, dead_ip)
    return result

print(ping_ip_addresses(['192.168.56.1', '257.1.1.1', '1.1.1.1', '10.10.10.10.', 'asd']))