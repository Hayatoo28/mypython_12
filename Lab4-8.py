#โปรแกรมหาพื้นที่วงกลม 22/7*(r**2)
def BMI(w,h):
    h1  = h / 100
    b = w / (h1 * h1)
    print("Your BMI is %.2f" %b)
    return b


w = float(input("น้ำหนัก(KG) >>> "))
h = float(input("ส่วนสูง(CM) >>> "))
    
b = BMI(w,h)
    
if b < 18.50:              
    print('น้ำหนักต่ำกว่าเกณฑ์')
elif b >= 18.50 and b <= 22.99:
    print('อยู่ในเกณฑ์ปกติ')
elif b >= 23 and b <= 24.99:
    print('อ้วนขั้นที่ 1')
elif b >= 25 and b <= 29.99:
    print('อ้วนขั้นที่ 2')
elif b >= 30:                        
    print('อ้วนขั้นสูงสุด')
