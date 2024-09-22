"""
4) Descubra a lógica e complete o próximo elemento:
a) 1, 3, 5, 7, ___ R = 9
b) 2, 4, 8, 16, 32, 64, ____ R =
c) 0, 1, 4, 9, 16, 25, 36, ____
d) 4, 16, 36, 64, ____
e) 1, 1, 2, 3, 5, 8, ____
f) 2,10, 12, 16, 17, 18, 19, ____

"""
a = 1
b = 2
c, cc, dd = 0, 0, 0

for _ in range(4):
    a += 2
print(f"A respota da letra A é {a}")

for _ in range(6):
    b *=  2
print(f"A respota da letra B é {b}")    

for _ in range(7):
        cc += 1
        c = cc ** 2
print(f"A respota da letra C é {c}")   

for _ in range(5):
        dd += 2
        d = dd ** 2
print(f"A respota da letra D é {d}")   

fibo_a, fibo_b = 1, 1
for _ in range(5):
        fibo_a, fibo_b = fibo_b, fibo_a + fibo_b
print(f"A respota da letra E é {fibo_b}")   

print("A respota da letra F é 200")  
