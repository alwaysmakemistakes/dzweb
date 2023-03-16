# Создать функцию print_ip_table, которая отображает таблицу доступных и недоступных IP-адресов.
# Функция ожидает как аргументы два списка:
# список доступных IP-адресов
# список недоступных IP-адресов
# Результат работы функции - вывод на стандартный поток вывода таблицы вида:
# Reachable    Unreachable
# -----------  -------------
# 10.1.1.1     10.1.1.7
# 10.1.1.2     10.1.1.8
#              10.1.1.9



from tabulate import tabulate

unreachable_ip = ['10.1.1.7', '10.1.1.8', '10.1.1.9']
reachable_ip = ['10.1.1.1', '10.1.1.2']
ip = [reachable_ip, unreachable_ip]

def print_ip_table(reachable, unreachable):
    IP = {}
    for ip_addr in reachable:
        IP.setdefault('Reachable', []).append(ip_addr)
    for ip_addr in unreachable:
        IP.setdefault('Unreachable', []).append(ip_addr)
    
    print(tabulate(IP, headers='keys'))
    
print_ip_table(reachable_ip, unreachable_ip)