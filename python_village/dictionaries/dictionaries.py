def word_count(file):
    with open(file, 'r') as f:
        words = f.read().split()
        word_counts = {}
        for word in words:
            if word in word_counts:
                word_counts[word] += 1
            else:
                word_counts[word] = 1
    
    output_file = 'rc_ex6_output.txt'
    with open(output_file, 'w') as o:
        for word, count in word_counts.items():
            o.write(f'{word} {count}\n')
    
    return output_file

output = word_count('rosalind_ini6.txt')
print(f'Word counts written to {output}')