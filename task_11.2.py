# Создать функцию create_network_map, которая обрабатывает вывод команды show cdp neighbors из нескольких файлов и объединяет его в одну общую топологию.
# У функции должен быть один параметр filenames, который ожидает как аргумент список с именами файлов, в которых находится вывод команды show cdp neighbors.
# Функция должна возвращать словарь, который описывает соединения между устройствами. Структура словаря такая же, как в задании 11.1:

# {("R4", "Fa0/1"): ("R5", "Fa0/1"),
#  ("R4", "Fa0/2"): ("R6", "Fa0/0")}

# Cгенерировать топологию, которая соответствует выводу из файлов:

# sh_cdp_n_sw1.txt

# sh_cdp_n_r1.txt

# sh_cdp_n_r2.txt

# sh_cdp_n_r3.txt

# Не копировать код функций parse_cdp_neighbors и draw_topology.
# Если функция parse_cdp_neighbors не может обработать вывод одного из файлов с выводом команды, надо исправить код функции в задании 11.1.
# Ограничение: Все задания надо выполнять используя только пройденные темы.

infiles = [
    "sh_cdp_n_sw1.txt",
    "sh_cdp_n_r1.txt",
    "sh_cdp_n_r2.txt",
    "sh_cdp_n_r3.txt",
]


# from task_11_1 import parse_cdp_neighbors
# import draw_network_graph as draw

# def readfile(file):
#         with open(file, 'r') as config:
#             return config.read()

# def create_network_map(filenames):
#     topology_dict = {}
#     for file in filenames:
#         current_file = readfile(file)
#         topology_dict.update(parse_cdp_neighbors(current_file))
    
#     great_topology = {}
#     tpDict = topology_dict.copy()
#     for k in tpDict.keys():
#         for v in tpDict.values():
#             if k[0] == v[0]:
#                 if k == v:
#                     pass
#                 else:
#                     great_topology.update({k : tpDict.get(k)})

#     return great_topology

# draw.draw_topology(create_network_map(['sh_cdp_n_sw1.txt', 'sh_cdp_n_r1.txt', 'sh_cdp_n_r2.txt', 'sh_cdp_n_r3.txt']))


from task_11_1 import parse_cdp_neighbors
import draw_network_graph as dr

def readfile(file):
        with open(file, 'r') as config:
            return config.read()

def create_network_map(filenames):
    topology_dict = {}
    for file in filenames:
        current_file = readfile(file)
        topology_dict.update(parse_cdp_neighbors(current_file))
    
    great_fucking_topology = {}
    tmpDict = topology_dict.copy()
    for k in tmpDict.keys():
        for v in tmpDict.values():
            if k[0] == v[0]:
                if k == v:
                    pass
                else:
                    great_fucking_topology.update({k : tmpDict.get(k)})

    return great_fucking_topology

dr.draw_topology(create_network_map(['sh_cdp_n_sw1.txt', 'sh_cdp_n_r1.txt', 'sh_cdp_n_r2.txt', 'sh_cdp_n_r3.txt']))