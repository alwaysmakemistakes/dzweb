result = []
vlan_input = input("Enter VLAN number: ")
with open('CAM_table.txt') as f:
    for line in f:
        words = line.split()
        template = '{:15} {:15} {:15}'
        if words and words[0].isdigit():
            vlan, mac, _, ports = words
            result.append([int(vlan), mac, ports])
for vlan, mac, intf in sorted(result):
    if int(vlan_input) == vlan:
        print(f"{vlan:<9}{mac:20}{intf}")