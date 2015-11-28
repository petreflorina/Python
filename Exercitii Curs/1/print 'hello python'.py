a = [1, 3, 20, 1024, 53, 12, 102, 1, 4, 43, 32] 
ok = True
l = len(a)

for elem in range(l):
	
	if a[elem] % 3 != 0:
		ok = False
		break
		
if ok ==False:
	print 'nu toate numerele sunt divizibile cu 3'
else:
	print 'toate numerele sunt divizibile cu 3'