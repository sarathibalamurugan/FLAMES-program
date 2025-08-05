a = "aaf"           #Add name1
b = "sfbaEFaSF"     #Add name2
al = list(a.replace(" ", "").lower())
bl = list(b.replace(" ", "").lower())

# Remove common characters
for ch in al[:]:
    if ch in bl:
        al.remove(ch)
        bl.remove(ch)

c = len(al) + len(bl)  # Total count after removing common letters
f = ['friend', 'lover', 'affection', 'marriage', 'enemy', 'sister']

i = 0
while len(f) > 1:
    i = (i + c - 1) % len(f)
    f.pop(i)
print(a)
print(b)
print(f[0].upper())
