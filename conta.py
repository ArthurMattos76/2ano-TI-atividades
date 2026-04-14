croasaint = int(input("P:"))
salgado = int(input("D:"))
jujuba = int(input("B:"))

total = croasaint + (salgado * 2) + (jujuba * 3)

if 0 <= croasaint <= 100 and 0 <= salgado <= 100 and 0 <= jujuba <= 100:
    if total >= 150:
        print("B")
    elif total >= 120:
        print("D")
    elif total >= 100:
        print("P")
    else:
        print("N")
else:
    print("N")