access_template = [
    "switchport mode access", "switchport access vlan {}",
    "switchport nonegotiate", "spanning-tree portfast",
    "spanning-tree bpduguard enable"
]

trunk_template = [
    "switchport trunk encapsulation dot1q", "switchport mode trunk",
    "switchport trunk allowed vlan {}"
]

mode = input('Enter interface mode (access/trunk ): ')
interface = input('Enter interface type and number: ')

mode = mode.count('trunk')

modes = [
['Enter VLAN number: '],
['Enter allowed VLANs: ']
]

vlans = input (' '.join(modes[mode]))

config_template = [
['switchport mode access',
 'switchport access vlan {}',
 'switchport nonegotiate',
 'spanning-tree portfast',
 'spanning-tree bpduguard enable'],
['switchport trunk encapsulation dot1q',
 'switchport mode trunk',
 'switchport trunk allowed vlan {}']
]

print('\n' * 2)
print('interface {}'.format(interface))
print('\n'.join(config_template[mode]).format(vlans))