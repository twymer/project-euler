from decimal import *
maxLength=0
maxDivisor=0
maxPattern=0
for i in range(1,10):
	#i = 9
	getcontext().prec = 50
	getcontext().rounding=ROUND_FLOOR
	val = Decimal(1) / Decimal(i)
	val=str(val)
	print(val)
	found=False
print(maxLength)            
print(maxDivisor)
