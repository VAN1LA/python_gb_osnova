from itertools import zip_longest

class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return str("\n".join(["\t".join([str(i)for i in j]) for j in self.matrix]))

    def __add__(self, other):
        return Matrix([map(sum, zip_longest(*l, fillvalue=0))
                       for l in zip_longest(self.matrix, other.matrix, fillvalue=[])])


list1 = [[2, 3, 4, 5], [5, 7, 4, 7], [4, 7, 7, 6]]
list2 = [[7, 8, 8, 1], [1, 1, 1, 3], [8, 8, 8, 2]]


matrix_1 = Matrix(list1)
matrix_2 = Matrix(list2)

print(matrix_1)
print(matrix_1 + matrix_2)


