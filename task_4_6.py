# -*- coding: utf-8 -*-
"""
Задание 4.6

Обработать строку ospf_route и вывести информацию на стандартный поток вывода в виде:
Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Для этого использовать шаблон template и подставить в него значения из строки
ospf_route. Значения из строки ospf_route надо получить с помощью Python.

Ограничение: Все задания надо выполнять используя только пройденные темы.

Предупреждение: в разделе 4 тесты можно легко "обмануть" сделав нужный вывод,
без получения результатов из исходных данных с помощью Python.
Это не значит, что задание сделано правильно, просто на данном этапе сложно иначе
проверять результат.
"""

#ospf_route = "      10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"
#template = """
#Prefix                {pref}
#AD/Metric             {adm}
#Next-Hop              {nh}
#Last update           {lu}
#Outbound Interface    {oi}
#"""


ospf_route = "      10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"

t = ospf_route.split()

t_prefix  = t[0]
t_metric = t[1]
t_metric = t_metric[1:-1]
t_next_hop = t[3]
t_next_hop = t_next_hop[:-1]
t_last_upd = t[4]
t_last_upd = t_last_upd[:-1]
t_interface = t[5]

print ('Prefix ','{:>35}'.format(t_prefix))
print ('AD/Metric ','{:>26}'.format(t_metric))
print ('Next-Hop ','{:>30}'.format(t_next_hop))
print ('Last update ','{:>23}'.format(t_last_upd))
print ('Outbound Interface ','{:>26}'.format(t_interface ))








#pr = print('Prefix ' '{ip}/{mask}'.format(ip = '10.0.24.0', mask ='24'))
#adm = print('AD/Metric ' '{ad}/{me}'.format(ad = '110', me='41'))
#nxh = print('Next-Hop ' '{nh}'.format(nh='10.0.13.3'))
#lu = print('Last update ' '{days}''{hours}'.format(days='3d', hours = '18h'))
#oui = print('Outbound Interface ' '{int}'.format(int='FastEthernet0/0'))



#print(
 #   'ospf_route'
 #   '\nPrefix '    '{pref}' 
 #   '\nAD/Metric ' '{ad}'.format(pref = '10.0.24.0/24', ad = '110/41'))


#ip, mask, ad, metric, nhop, days, hours, intf =['10.0.24.0', '24', '110', '41', '10.0.13.3', '3d','18h','FastEthernet0/0']
#'{ip}/{mask}'.format(ip,mask)

#print('ospf_route'
 #     'Prefix ' '{ip}/{mask}'.format(mask=24, ip='10.1.1.1')
  #    'AD/Metric ' '{ad}/{metric}'.format(ad=110, metric='41')






#)