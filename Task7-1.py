class Matrix:
    def __init__(self, list_1, list_2):
        self.list_1 = list_1
        self.list_2 = list_2

    def __str__(self):

        return str('\n'.join([self.list_1, self.list_2]))

    def __add__(self):
        matr = [[self.list_1], [self.list_2]]

        for i in range(len(self.list_1)):

            for j in range(len(self.list_2[i])):
                matr[i][j] = self.list_1[i][j] + self.list_2[i][j]

        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in matr]))


my_matrix = Matrix([1, 2, 3], [4, 5, 6])
print(my_matrix)