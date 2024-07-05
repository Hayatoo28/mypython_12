def Fa(C):
    F = (9/5)*C+32
    return F

def Ke(C):
    K = C+273.15
    return K

C = int(input("Celsius: "))
print("ฟาเรนไฮธ์ %.2f" % Fa(C))

C = int(input("Celsius: "))
print("เคลวิน %.2f" % Ke(C))


