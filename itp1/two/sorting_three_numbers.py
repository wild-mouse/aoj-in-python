import fileinput

a_b_c = list(map(int, input().split()))

a, b, c = sorted(a_b_c)

print(a, b, c)
