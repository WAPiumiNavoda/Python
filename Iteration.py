# dicsorany itoration

d = {
    "A":10,
    "B":20,
    "C":30,
    "D":40
}

# for name in d:
#     heigth = d[name]
#     print(name, heigth)

for name,heigth in d.items():
    print(name,heigth)
    print(type(name))

# Set itoration
print("\n......Set itoration.......\n")
t = ("Piumi" , 120 ,"Gampaha" ,"Sri Lanka" )
for i, name in enumerate(t):
    print(i, name)

