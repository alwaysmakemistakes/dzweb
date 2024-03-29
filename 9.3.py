# Создать функцию get_int_vlan_map, которая обрабатывает конфигурационный файл коммутатора и возвращает кортеж из двух словарей:

# словарь портов в режиме access, где ключи номера портов, а значения access VLAN (числа):

# {"FastEthernet0/12": 10,
#  "FastEthernet0/14": 11,
#  "FastEthernet0/16": 17}
# словарь портов в режиме trunk, где ключи номера портов, а значения список разрешенных VLAN (список чисел):

# {"FastEthernet0/1": [10, 20],
#  "FastEthernet0/2": [11, 30],
#  "FastEthernet0/4": [17]}
# У функции должен быть один параметр config_filename, который ожидает как аргумент имя конфигурационного файла.

# Проверить работу функции на примере файла config_sw1.txt

# Ограничение: Все задания надо выполнять используя только пройденные темы.


def get_int_vlan_map(config):
    with open(config, 'r') as file:
            access_config = {}
            trunk_config = {}
            for line in file:
                if line.find('FastEthernet') != -1:
                    interface = line.split()[-1]
                elif line.find('access vlan') != -1:
                    access_vlan = line.split()[-1]
                    access_config[interface] = access_vlan
                elif line.find('trunk allowed vlan') != -1:
                    trunk_vlan = line.split()[-1]
                    trunk_config[interface] = trunk_vlan
                else:
                    pass
            print('access interfaces: \n', access_config)
            print('trunk interfaces: \n', trunk_config)
    return access_config, trunk_config
print(get_int_vlan_map('config_sw1.txt'))




#⎝⧹⧸⎠⎝ ⎝⧹╲⎝⧹⧸⎠╱⧸⎠╱╲⎝⧹╲⎝