with open('CAM_table.txt') as f:
    for line in f:
        words = line.split()
        template = '{:15} {:15} {:15}'
        if words and words[0].isdigit():
            vlan, mac, _,ports = words
            print(f"{vlan:9}{mac:20}{ports}")