print("Our shop's assortment:\n")
cars = ['','Toyota Corolla','BMW X5','Škoda Octavia','VW Polo']
cars_in_stock = ['BMW X5', 'Škoda Octavia']
k = 1
for b in cars:
	if b == cars[0]:
		continue
	if b in cars_in_stock:
		print("%s. %s - in stock" % (k,b))
	else:
		print("%s. %s - not in stock" % (k,b))
	k = k + 1