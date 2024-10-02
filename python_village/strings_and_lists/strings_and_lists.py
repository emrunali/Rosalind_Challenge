def splice(filename):
    with open(filename, 'r') as file:
        s = file.readline(200)
        a, b, c, d = map(int, file.readline().split())
    return s[a:b+1] + ' ' + s[c:d+1]

print(splice('rosalind_ini3.txt'))