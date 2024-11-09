a = int(input("Enter value for a (0 or 1): "))
b = int(input("Enter value for b (0 or 1): "))
c = int(input("Enter value for c (0 or 1): "))

d = a & b
l = b | c
f = b & c
g = d & f
q = d | g

print("d (a & b) = ", d)
print("l (b | c) = ", l)
print("f (b & c) = ", f)
print("g (d & f) = ", g)
print("q (d | g) = ", q)
