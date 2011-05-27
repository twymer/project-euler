count=0
for p1 in range(1,200+1):
	for p2 in range(1,200/2+1):
		for p5 in range(1,200/5+1):
			for p10 in range(1,200/10+1):
				for p20 in range(1,200/20+1):
					for p50 in range(1,200/50+1):
						for P1 in range(1,3):
							for P2 in range(1,2):
								if p1+p2+p5+p10+p20+p50+P1*100+P2*200==200:
									count+=1
print(count)
