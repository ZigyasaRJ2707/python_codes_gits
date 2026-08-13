def genAP(a, b):
        diff = (b-a)/3
        term2 = a + diff*1
        term3 = a + diff*2
        return a, term2, term3, b

print(genAP(4,8))