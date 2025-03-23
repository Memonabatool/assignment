ls = ["lahore","faisalabad","jaranwala"]
lp = []
for x in ls:
  p = x[0:1].upper() +x [1:-1].lower() +x[:-1].upper()
  lp.append(p)
  print(p)
print(lp)