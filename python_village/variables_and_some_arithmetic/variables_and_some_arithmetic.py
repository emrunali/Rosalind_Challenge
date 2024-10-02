def c_square(file):
    a,b = map(int, open(file, 'rt').read().split())
    return a**2 + b**2

print(c_square('rosalind_ini2.txt'))