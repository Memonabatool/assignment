ls = ["lahore","karachi","multan","peshawar","karor","layyah","jaranwala","islamabad","faisalabad","bhawalpur"]
a = []
for x in ls:
    a.insert(0,x)
print(a)

for x in ls:
    a= x[0:1].upper() +x[1:]
    print(a)



