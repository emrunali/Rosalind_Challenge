def sum_odd(file):
  a, b = map(int, open(file, 'rt').read().split())
  if not a < b < 10000:
    return "Invalid input"
  
  sum = 0
  for i in range(a,b+1):
    if i%2 != 0:
      sum = sum + i
  return sum

print(sum_odd("rosalind_ini4.txt"))