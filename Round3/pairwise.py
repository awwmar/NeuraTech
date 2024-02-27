import sys

with open(sys.argv[1], 'r') as f:
    seq1 = f.read()

with open(sys.argv[2], 'r') as g:
    seq2 = g.read()
    
m = len(seq1)
n = len(seq2)
matrix = [[0] * (n+1) for _ in range(m+1)]
for i in range(m+1):
    matrix[i][0] = -i
for j in range(n+1):
    matrix[0][j] = -j

for i in range(1, m + 1):
    for j in range(1, n + 1):
        match = matrix[i - 1][j - 1] + (1 if seq1[i - 1] == seq2[j - 1] else -1)
        delete = matrix[i - 1][j] - 1
        insert = matrix[i][j - 1] - 1
        matrix[i][j] = max(match, delete, insert)

aligned_seq1 = ""
aligned_seq2 = ""
i, j = m, n
while i > 0 or j > 0:
    if i > 0 and matrix[i][j] == matrix[i - 1][j] - 1:
        aligned_seq1 = seq1[i - 1] + aligned_seq1
        aligned_seq2 = "-" + aligned_seq2
        i -= 1
    elif j > 0 and matrix[i][j] == matrix[i][j - 1] - 1:
        aligned_seq1 = "-" + aligned_seq1
        aligned_seq2 = seq2[j - 1] + aligned_seq2
        j -= 1
    else:
        aligned_seq1 = seq1[i - 1] + aligned_seq1
        aligned_seq2 = seq2[j - 1] + aligned_seq2
        i -= 1
        j -= 1
        
print("Aligned Sequence 1:", aligned_seq1)
print("Aligned Sequence 2:", aligned_seq2)