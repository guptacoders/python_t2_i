# WAP to rotate matrix 90deg Clockwise
# i/p: 1 2 3 
#      4 5 6
#      7 8 9
        
# o/p: 7 4 1 
#      8 5 2
#      9 6 3

matrix = [
    [1, 2, 3,9],
    [4, 5, 6,1],
    [7, 8, 9,2],
    [10, 11, 12,3]
]

# Rotate the matrix by 90 degrees clockwise
rotated_matrix = [list(reversed(col)) for col in zip(*matrix)]

for row in rotated_matrix:
    print(*row)
