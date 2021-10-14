s='referd'
a,l=1,len(s)
for i in range(1,l+1):
    t=s[:i]
    if t==t[::-1]:
        a=i
print(l-a)