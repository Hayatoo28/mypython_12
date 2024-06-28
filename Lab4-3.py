#ชนิดข้อมูล Dictionaly
x = {
    "name": "Peerapat",
    "age": 19,
    "wt": 58,
    "h": 167
    }
print(x)
print("สวัสดีครับคุณ %s" % x["name"])
print("พ.ศ.เกิด %d อายุ %d" % (2567-x["age"], x["age"]))
print("น้ำหนัก %d ส่วนสูง %d" % (x["wt"], x["h"]))

