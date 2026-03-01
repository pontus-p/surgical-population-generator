import generator

s = generator.create_patients(100)
for x in s:
    print(x)
    print(len(x))

print(len(s))
