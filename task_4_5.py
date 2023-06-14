command1 = "switchport trunk allowed vlan 1,2,3,5,8"
command2 = "switchport trunk allowed vlan 1,3,8,9"
command1 = command1.split()[-1]
command2 = command2.split()[-1]
command1 = set(command1)
command2 = set(command2)
command1.remove(',')
command2.remove(',')
result =  command1.intersection(command2)
result = list(result)
result = sorted(result)

print(result)