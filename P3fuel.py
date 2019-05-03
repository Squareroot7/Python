fuelCapacity = float(input('Inserisci la capienza del serbatoio: '))
fuelAmount = float(input('Inserisci la quantità di carburante nel serbatoio: '))

if fuelAmount<(fuelCapacity/100*10):
	print("red")
else :
	print("green")
