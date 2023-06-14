def get_int_vlan_map(config_filename):
    access_dict = {}
    trunk_dict = {}

    with open(config_filename) as cfg:
        for line in cfg:
            line = line.rstrip()
            if line.startswith("interface"):
                intf = line.split()[1]
            elif "access vlan" in line:
                access_dict[intf] = int(line.split()[-1])
            elif "trunk allowed" in line:
                trunk_dict[intf] = [int(v) for v in line.split()[-1].split(",")]
    return access_dict, trunk_dict

access_ports, trunk_ports = get_int_vlan_map("config_sw1.txt")

print("Access Ports:")
for interface, vlan in access_ports.items():
    print(f"Interface: {interface}, VLAN: {vlan}")

print("\nTrunk Ports:")
for interface, vlans in trunk_ports.items():
    print(f"Interface: {interface}, Allowed VLANs: {', '.join(str(vlan) for vlan in vlans)}")