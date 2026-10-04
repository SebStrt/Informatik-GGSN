#Palidrome detection

wort = str(input("Wort eingeben: "))

n = 0

for char in wort:
    if char == wort[len(wort)-1-n : len(wort)-n]:
        n = n+1
    else:
        exit("Kein Palindrom")
print("Palindrom")