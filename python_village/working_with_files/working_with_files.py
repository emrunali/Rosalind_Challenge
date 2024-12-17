def get_lines(file):
    f = open(file, 'r')
    o_content = f.readlines()[1:1001:2]
    o = open('rc_ex4_output.txt', 'w')
    for s in o_content:
        o.write(s)
    return o.close()

output = get_lines('rosalind_ini5.txt')
print(output)