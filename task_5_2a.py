
network = input("Введите адрес сети: ")
ip, mask = network.split("/")
ip_list = ip.split(".")
mask = int(mask)
oct1, oct2, oct3, oct4 = [
    int(ip_list[0]),
    int(ip_list[1]),
    int(ip_list[2]),
    int(ip_list[3]),
]

bin_ip = "{:08b}{:08b}{:08b}{:08b}".format(oct1, oct2, oct3, oct4)
bin_network = bin_ip[:mask] + "0" * (32 - mask)
net1, net2, net3, net4 = [
    int(bin_network[0:8], 2),
    int(bin_network[8:16], 2),
    int(bin_network[16:24], 2),
    int(bin_network[24:32], 2),
]

bin_mask = "1" * mask + "0" * (32 - mask)
m1, m2, m3, m4 = [
    int(bin_mask[0:8], 2),
    int(bin_mask[8:16], 2),
    int(bin_mask[16:24], 2),
    int(bin_mask[24:32], 2),
]

ip_output = """
Network:
{0:<8}  {1:<8}  {2:<8}  {3:<8}
{0:08b}  {1:08b}  {2:08b}  {3:08b}"""

mask_output = """
Mask:
/{0}
{1:<8}  {2:<8}  {3:<8}  {4:<8}
{1:08b}  {2:08b}  {3:08b}  {4:08b}
"""

print(ip_output.format(net1, net2, net3, net4))
print(mask_output.format(mask, m1, m2, m3, m4))