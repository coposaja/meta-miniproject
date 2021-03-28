import os

file = open('./config.txt', 'r')
configs = file.read().splitlines()
file.close()

source_path = configs[0]
files = []

for i in range(2, len(configs)):
  cfg = configs[i].split(':')
  files.append(cfg[0])

for i in files:
  if(not os.path.exists(os.path.join(source_path, i+'.txt'))):
    if(not os.path.exists(source_path)):
      os.makedirs(source_path)
    open(os.path.join(source_path, i+'.txt'), 'a').close()

print('seeded')
