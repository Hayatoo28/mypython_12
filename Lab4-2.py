#ชนิดข้อมูล List
person = ["Peerapat",19 ,167 ,58, "peerapat.sinlatham2812@gmail.com"]
print(person)
#person[1] = 40
print("อายุ %s" % person[1])
print("ส่วนสูง %d น้ำหนัก %d"  % (person[2], person[3]))
print("Gmail %s" % person[4])

print(person[0:3])
print(person[2:4])
print(person[2:])
print(person[:4])
print(person[-4:-1])