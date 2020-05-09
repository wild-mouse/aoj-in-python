import fileinput

a_b_c = input().split()

a = a_b_c[0]
b = a_b_c[1]
c = a_b_c[2]

if a < b and a < c:
    print("Yes")
else:
    print("No")
