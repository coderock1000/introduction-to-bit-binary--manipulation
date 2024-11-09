a = int(input("Enter value for a (0 or 1): "))
b = int(input("Enter value for b (0 or 1): "))
c = int(input("Enter value for c (0 or 1): "))

d = a & b
l = b | c
f = b & c
g = d & f
q = d | g

print(f"d (a & b) = ", d)
print(f"l (b | c) = ", l)
print(f"f (b & c) = ", f)
print(f"g (d & f) = ", g)
print(f"q (d | g) = ", q)
