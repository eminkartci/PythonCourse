

"""
MATRIX -> 3 x 4

Satir: 3
Stun:  4

[
    [1 2 1 0] => 1.x1 + 2.x2 + 1.x3 + 0.x4 -> Denklem 1,
    [3 3 1 2] => 3.x1 + 3.x2 + 1.x3 + 2.x4 -> Denklem 2,
    [5 2 1 4] => 5.x1 + 2.x2 + 1.x3 + 4.x4 -> Denklem 3
]
1    Integer => Tam Sayilar
1.0  Float   => Kesirli Sayilar
"1"  String  => Yazi 

List / Array => Farkli item'lari tek degiskende tutmak

"""

denklem1x1 = 1
denklem1x2 = 2
denklem1x3 = 1
denklem1x4 = 0

denklem1 = [1, 2, 1, 0]
# 0. index 1
# 1. index 2
# 2. index 1
# 3. index 0

denklem2 = [3,3,1,2]
denklem3 = [5,2,1,4]

matrix = [denklem1,denklem2,denklem3 ]

print("Matrix: ",matrix)

## Tum sayilari toplayan bir fonksiyon yaz
def selamla(isim):
    print("Merhaba",isim)

def sayilari_topla(mat):
    toplam = 0
    for denklem in mat:
        for sayi in denklem:
            toplam += sayi

    print("Toplam: ",toplam)

## Fonksiyonlari Cagir
selamla("Emin")
selamla("Serra")
sayilari_topla(matrix)








