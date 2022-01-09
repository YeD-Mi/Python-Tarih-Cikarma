aylar = [31, 28, 31, 30, 31, 30,31, 31, 30, 31, 30, 31]
def artikyil(d):
    yil = d.y
    if (d.m <= 2):
        yil -= 1
    ans = int(yil / 4)
    ans -= int(yil / 100)
    ans += int(yil / 400)
    return ans
def farkal(dt1, dt2):
    n1 = dt1.y * 365 + dt1.d
    for i in range(0, dt1.m - 1):
        n1 += aylar[i]
    n1 += artikyil(dt1)
    n2 = dt2.y * 365 + dt2.d
    for i in range(0, dt2.m - 1):
        n2 += aylar[i]
    n2 += artikyil(dt2)
    return (n2 - n1)
class tarih:                         
   def __init__(self, d, m, y, s): 
     self.d = d   #gün                        
     self.m = m   #ay
     self.y = y   #yil
     self.s = s   #saat
tarih_1 = tarih(1, 9, 2014, 23)
tarih_2 = tarih(3, 9, 2020, 22)
farkgun=farkal(tarih_1,tarih_2)
if(tarih_1.s>tarih_2.s):
    farkgun=farkgun-1
    tarih_2.s=tarih_2.s+24
print("Iki tarih arasindaki fark: ",farkgun,"gun.")
print("Iki tarih arasindaki saat: ",(farkgun*24)+(tarih_2.s-tarih_1.s),"saat.")