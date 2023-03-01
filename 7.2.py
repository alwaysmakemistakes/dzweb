from sys import argv
cfg = argv[1:]
cfg = ''.join(cfg)
with open(cfg, 'r') as file:
    for line in file:
        if line.find('!') == -1:
            print(line.strip('\n'))