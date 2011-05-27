#Runs instant with sets, much slower with lists
items=set()
for a in range(2,101):
	for b in range(2,101):
		c=a**b
		if c not in items:
			items.add(c)
print(len(items))
