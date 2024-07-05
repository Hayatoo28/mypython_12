def beforMidterm():    
    S = (a + b + c)
    return S

a = int(input("คะแนนเก็บ : "))
if score > 20:
    print("คะแนนเก็บไม่เกิน 20")

    
b = int(input("คะแนนจิตพิสัย : "))
if score > 10:
    print("คะแนนจิตพิสัยไม่เกิน 10")

    
c = int(input("คะแนนกลางภาคไม่เกิน : "))
if score > 30:
    print("คะแนนกลางภาคไม่เกิน 30")


    
    print("คะแนนรวม %2f" %beforMidterm())