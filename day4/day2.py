#Write a Python program to sum three given integers. However, if two or more values are equal sum of zero.

def sum(x, y, z):
    if x == y or y == z or x==z:
        sum = 27
    else:
        sum = x + y + z
    return sum

print(sum(2, 1, 2))
print(sum(3, 2, 2))
print(sum(2, 2, 2))
print(sum(1, 2, 3))

