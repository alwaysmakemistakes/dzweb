def get_int_vlan_map(config_filename):
    access_dict = {}
    trunk_dict = {}

    with open(config_filename) as cfg:
        for line in cfg:
            line = line.rstrip()
            if line.startswith("interface"):
                intf = line.split()[1]
            elif "access vlan" in line:
                vlan = line.split()[-1]
                if vlan.isdigit():
                    access_dict[intf] = int(vlan)
                else:
                    access_dict[intf] = 1
            elif "trunk allowed" in line:
                trunk_dict[intf] = [int(v) for v in line.split()[-1].split(",")]
            elif "switchport mode access" in line:
                access_dict[intf] = 1
        return access_dict, trunk_dict

access_ports, trunk_ports = get_int_vlan_map("config_sw2.txt")

print("Access Ports:")
for interface, vlan in access_ports.items():
    print(f"{interface}: {vlan}")

print("\nTrunk Ports:")
for interface, vlans in trunk_ports.items():
    print(f"{interface}: {', '.join(str(vlan) for vlan in vlans)}")