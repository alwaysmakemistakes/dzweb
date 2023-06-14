from task_11_2 import create_network_map
from draw_network_graph import draw_topology


infiles = [
    "sh_cdp_n_sw1.txt",
    "sh_cdp_n_r1.txt",
    "sh_cdp_n_r2.txt",
    "sh_cdp_n_r3.txt",
]

def unique_network_map(topology_dict):
    network_map = {}
    for key, value in topology_dict.items():
        if not network_map.get(value) == key:
            network_map[key] = value

    for key, value in network_map.items():
        print("{0}: {1}".format(key, value))
    print()

    return network_map

if __name__ == "main":
    topology = create_network_map(infiles)
    new_topology = unique_network_map(topology)

    draw_topology(new_topology)