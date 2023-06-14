['1', '3', '10', '20', '30', '100']

config = "switchport trunk allowed vlan 1,3,10,20,30,100"
gifnoc = config.split()[-1].split(",")
print (gifnoc)