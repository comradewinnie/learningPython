print("Our shop's assortment:\n")
cars = ['','Toyota Corolla','BMW X5','Škoda Octavia','VW Polo']
cars_in_stock = ['BMW X5', 'Škoda Octavia']
n=1
for i in cars:
	if i == cars[0]:
		continue
	print("%s." % n,i)
	n = n + 1
request = int(input("\nWrite the car number you want to check: "))
if cars[request] in cars_in_stock:
	print("\n%s is in stock. You can buy it right now!" % cars[request])
else:
	print("\n%s is not in stock." % cars[request])