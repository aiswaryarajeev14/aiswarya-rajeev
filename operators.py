x=["abc","123","234.980"]
y=["abc","123","234.980"]
z=x
print(x is z)
print(x is not z)
print(z==y)
print(x!=y)
print(y is z)
print(y is not z)

x=["abc","123","2.56"]
y=["adfc","1273","2.5096"]
print("abc" in x)
print("abc" not in y)
print("123" in y)
print("123" not in y)