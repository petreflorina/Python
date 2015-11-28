
def pretTVA(n):
	return (n + 17/100 * n)

ana = {"tastatura": 70, "mouse": 50, "casti": 100}

ana["tastatura"] = pretTVA(ana["tastatura"])
ana["mouse"] = pretTVA(ana["mouse"])
ana["casti"] = pretTVA(ana["casti"])

total = 0
for elem in ana:
	total += ana[elem]
print total 
print "lei"