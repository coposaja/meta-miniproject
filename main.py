import os

file = open('./config.txt', 'r')
configs = file.read().splitlines()
file.close()

source_path = configs[0]
dest_base_path = configs[1]
lookup = {}

for i in range(2, len(configs)):
	cfg = configs[i].split(':')
	lookup[cfg[0]] = cfg[1]

if(not os.path.exists(source_path)):
	os.makedirs(source_path)

for f in os.listdir(source_path):
  if(os.path.isfile(os.path.join(source_path, f))):
		dest = dest_base_path
		from_lookup = lookup.get(f.split('.')[0], '')
		
		if(from_lookup == ''):
			dest = source_path
		else:
			dest = os.path.join(dest, from_lookup)
    
		if(not os.path.exists(dest)):
			os.makedirs(dest)

		os.rename(os.path.join(source_path, f), os.path.join(dest, f))

print("Completed!")