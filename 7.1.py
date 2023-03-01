with open('ospf.txt', 'r') as text:
    ospf = text.readlines()
    for lines in ospf:
        lines = lines.strip().split()
        protocol = lines[0].replace('O', 'OSPF')
        prefix = lines[1]
        ad = lines[2].strip('[]')
        hop = lines[4].strip(',')
        update = lines[5].strip(',')
        interface = lines[6]
        ospf_route = """
        Protocol:             {0:18}
        Prefix:               {1:18}
        AD/Metric:            {2:18}
        Next-Hop:             {3:18}
        Last update:          {4:18}
        Outbound Interface:   {5:18}
        """
        print(ospf_route.format(protocol,prefix,ad,hop,update,interface))