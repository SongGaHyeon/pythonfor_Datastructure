# write compute_tsa function here
def compute_tsa(r,h):
	# pi=3.1416
	TSA=pi*2*(r**2+r*h)
	return TSA

r,h=[float(x) for x in input().split()]
pi=3.1416
tsa= compute_tsa(r,h)
print('%.2f'%(tsa))