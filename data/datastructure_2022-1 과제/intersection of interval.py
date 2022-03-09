a1 = int(input())
a2 = int(input())

# code for ex) 5 2 5 2
if (a1 > a2):
    temp = a2
    a2 = a1
    a1 = temp

b1 = int(input())
b2 = int(input())

# code for ex) 5 2 5 2
if (b1 > b2):
    temp = b2
    b2 = b1
    b1 = temp

if (a1 > b1):
    new_a1 = b1
    new_a2 = b2
    new_b1 = a1
    new_b2 = a2

else:
    new_a1 = a1
    new_a2 = a2
    new_b1 = b1
    new_b2 = b2

if (new_a2 > new_b1):
    overlap_first = new_b1
    if (new_a2 >= new_b2):
        overlap_end = new_b2
    else:
        overlap_end = new_a2
    length = abs(overlap_end - overlap_first)

else:
    length = 0

print(length)
