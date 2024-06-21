Kg = int(input("Weight"))
Cm = int(input("Hight"))
bmi = Kg/(Cm/100)**2
print(bmi)
if bmi<18.5:
    print("น้ำหนักน้อย")
elif bmi>=18.50 and bmi<=22.90:
    print("ปกติ")
elif bmi>=23 and bmi<=24.90:
    print("ท้วม/โรคอ้วนระดับ 1")
elif bmi>=25 and bmi<=29.90:
    print("อ้วน/โรคอ้วนระดับ 2")
else:
    print("อ้วนมาก/โรคอ้วนระดับ 3")