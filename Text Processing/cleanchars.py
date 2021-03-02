

with open('bushisms.txt') as f:
    data = f.read()

ok = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYV\n" .,-;?!\'1234567890:’'
clean = ''

for c in data:
	if c not in ok:
		print(c)
		clean += ' '
	else:
		clean += c

with open('bushtextprocessed.txt', 'w') as f:
	f.write(clean)
