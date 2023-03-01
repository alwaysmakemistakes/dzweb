from sys import argv
cfg = argv[1:]
cfg = ''.join(cfg)
ignore = ['duplex', 'alias', 'Current configuration', '!']
with open(cfg, 'r') as file:
    for line in file:
        if line.find(ignore[0]) == -1 and line.find(ignore[1]) == -1 and line.find(ignore[2]) == -1 and line.find(ignore[3]) == -1:
            print(line.strip('\n'))