ip = input("Введите IP-адрес в формате x.x.x.x: ")
octets = ip.split(".")
valid_ip = len(octets) == 4
for i in octets:
    valid_ip = i.isdigit() and 0 <= int(i) <= 255 and valid_ip
if valid_ip:
    if 1 <= int(octets[0]) <= 223:
        print("unicast")

    elif 224 <= int(octets[0]) <= 239:
        print("multicast")

    elif ip == "0.0.0.0": 
        print("unassigned")

    elif ip == "255.255.255.255": 
        print("local broadcast") 
else:
    print("Неправильный IP-адрес")