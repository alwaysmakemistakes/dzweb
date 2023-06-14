nat = "ip nat inside source list ACL interface FastEthernet0/1 overload"
tan = nat.replace("Fast", "Gigabit")
print(tan)