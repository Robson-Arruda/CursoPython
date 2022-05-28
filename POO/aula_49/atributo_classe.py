class A:
    vc = 123


a1 = A()
a2 = A()

A.vc = 321
a1.vc = 123

print(a1.vc)
print(a2.vc)
print(A.vc)

