x= [10,20,300,40,50,60]

# total = 0
# max = max =  x[0]

# for i in x:
#     total += i


# for i in x:
#     if max < i:
#         max = i

# print("Total: ", total)
# print("Avarage", total/len(x))

# print("Max: ", max)

# while --------
max = min =x[0]
count = 0
while count < len(x):
    item = x[count]

    if item > max:
        max = item

    if item < min:
        min = item
    
    count += 1

print("Max: " , max)
print("Min: ", min)
