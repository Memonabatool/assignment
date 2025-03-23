p = ["jaranwala" , "faisalabad" , "lahore"]
lp=[]
for x in p:
 p = x[0:1].lower() +x[1:2].upper () +x[2:-2] +x[-2:-1].upper() +x[-1:]
print(p)
p.append("")
print(lp)