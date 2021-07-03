# l3dz3

def my_func(s1, s2, s3):
    p1 = [s1, s2, s3]
    m1 = max(p1)
    p1.remove(m1)
    m2 = max(p1)
    return m1 + m2


print(my_func(3, 6, 8))


